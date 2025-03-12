import streamlit as st
from openai import OpenAI
from imageGeneration import generate_logo
from utils import validate_product_description, set_sidebar_css

with st.sidebar:
    openai_api_key = st.text_input("Enter Your API Key", key="chatbot_api_key", type="password")

# App title
st.title("MarketMind 🔥 - Your Marketing Strategy Partner")

# Ensure API key is provided
if not openai_api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.stop()

client = OpenAI(
 base_url="https://openrouter.ai/api/v1",
 api_key="",
)

# Apply custom CSS for the sidebar
set_sidebar_css()

predefined_colors = {
    "Red": "#FF6347",
    "Green": "#32CD32",
    "Blue": "#1E90FF",
    "Purple": "#8A2BE2",
    "Orange": "#FFA500",
    "Yellow": "#FFD700",
    "Pink": "#FF1493",
    "Black": "#000000",  # Black color
    "White": "#FFFFFF" 
}

# Step 1: Display custom sidebar components with colors and font options
st.sidebar.subheader("🎨 Customize Your Logo")
selected_color_name = st.sidebar.selectbox("Pick a logo color", list(predefined_colors.keys()))
logo_color = selected_color_name
font_options = ["Arial", "Helvetica", "Times New Roman", "Courier New", "Verdana"]
font_style = st.sidebar.selectbox("Select logo font", font_options)
st.sidebar.write(f"### Selected Logo Color: {logo_color}")
st.sidebar.write(f"### Selected Font Style: {font_style}")

# Session state initialization
if "product_description" not in st.session_state:
    st.session_state["product_description"] = ""
if "button_clicked" not in st.session_state:
    st.session_state["button_clicked"] = None
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "marketing_responses" not in st.session_state:
    st.session_state["marketing_responses"] = []
if "generated_logo" not in st.session_state:
    st.session_state["generated_logo"] = None

# Step 1: Product description input
if not st.session_state["product_description"]:
    product_description = st.text_area(
        "Describe your product:",
        value="",
        placeholder="E.g., A fresh, all-natural juice made from organic fruits."
    )
    if st.button("Submit Description") and product_description.strip():
        if not validate_product_description(product_description):
            st.error("The description seems unclear or nonsensical. Please provide a valid product idea.")
        else:
            st.session_state["product_description"] = product_description
            st.session_state["messages"].append({"role": "user", "content": product_description})
            st.session_state["button_clicked"] = "generate_ideas"

# Step 2: Generate marketing ideas (DeepSeek)
if st.session_state["button_clicked"] == "generate_ideas":
    deepseek_prompt = f"""
    You are a creative marketing assistant. Based on the product description, generate a marketing strategy with:
    1. **Product Name**: A catchy and creative name.
    2. **Target Audience**: Describe the ideal customer.
    3. **Marketing Ideas**: At least 3 creative strategies.
    4. **Slogan**: A short, persuasive tagline.
    **Product Description**: {st.session_state['product_description']}
    """
    response_ds1 = client.chat.completions.create(
        model="mistralai/pixtral-12b",
        messages=[{"role": "system", "content": deepseek_prompt}]
    )
    deepseek_response = response_ds1.choices[0].message.content
    if deepseek_response:
        st.session_state["messages"].append({"role": "assistant", "content": deepseek_response})
        st.session_state["marketing_responses"].append(deepseek_response)
    st.session_state["button_clicked"] = "generate_refinement"

# Step 3: Refine marketing plan (DeepSeek again)
if st.session_state["button_clicked"] == "generate_refinement":
    deepseek_refine_prompt = f"""
    Refine and expand the marketing strategy for the following product. Ensure the response follows this structured format:
    1. **Product Name**: A catchy and creative name.
    2. **Target Audience**: Describe the ideal customer in detail, including demographics, interests, and pain points.
    3. **Marketing Ideas**: Provide at least three creative and actionable strategies that align with the product's strengths and audience preferences.
    4. **Slogan**: A short, persuasive tagline that effectively communicates the product's unique value.
    **Product Description**: {st.session_state['product_description']}
    **Current Marketing Plan (DeepSeek Output)**:
    {st.session_state['marketing_responses']}
    Enhance the strategy by making it more detailed, engaging, and compelling. Use persuasive language, highlight key selling points, and ensure all sections are well-structured and insightful. Keep just your plan.
    """
    response_ds2 = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[{"role": "system", "content": deepseek_refine_prompt}]
    )
    deepseek_refined_response = response_ds2.choices[0].message.content
    if deepseek_refined_response:
        st.session_state["messages"].append({"role": "assistant", "content": deepseek_refined_response})
        st.session_state["marketing_responses"].append(f"**Refined Plan:**\n\n{deepseek_refined_response}")
    st.session_state["button_clicked"] = "generate_logo"

# Step 4: Generate logo (using your function)
if st.session_state["button_clicked"] == "generate_logo":
    product_name = st.session_state["product_description"].split()[0]
    st.session_state["generated_logo"] = generate_logo(st.session_state["product_description"],
                                                        logo_color,
                                                        font_style,
                                                        max_width=300)
    st.session_state["button_clicked"] = None

# Step 5: Display results
if st.session_state["marketing_responses"]:
    st.write("### 📢 Marketing Plans")
    st.write(st.session_state["marketing_responses"][-1])
    if st.session_state["generated_logo"]:
        st.write("### 🎨 Suggested Logo Concept")
        st.image(st.session_state["generated_logo"], caption="Generated Logo")
    # Next steps buttons
    st.write("What would you like to do next?")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("New Product Idea"):
            st.session_state.clear()
            st.rerun()
    with col2:
        if st.button("New Marketing Plan"):
            st.session_state["button_clicked"] = "generate_ideas"
            st.rerun()
    with col3:
        if st.button("Restart App"):
            st.session_state.clear()
            st.rerun()