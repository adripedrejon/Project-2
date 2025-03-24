# AI-Powered Marketing Strategy Creator
## Overview
This application is an AI-powered marketing strategy creator that helps users generate comprehensive marketing plans for their product ideas. Users can input a product description, and the AI will provide a tailored marketing plan, including:
- A product name
- A target audience
- Marketing ideas
- A slogan
- A logo

## Available Options
Users can choose between the following actions:
1. **Generate a new product idea** – Create an entirely new marketing plan from scratch.
2. **Generate a new marketing plan for the last idea** – Get a different marketing approach for the same product idea.
3. **Generate a new logo** – Keep the marketing plan but get a fresh logo design.
   
Additionally, users can:
- Share their marketing plan on Twitter.
- Customize the generated logo by selecting its color and font.
- Download the logo image for further use.

## Getting Started
Follow these steps to set up and run the application locally:

### Installation
1. Get a free API Key at [OpenRouter.ai](https://openrouter.ai).
2. Clone the repository:
   ```bash
   git clone https://github.com/adripedrejon/Project-2
3. Navigate to the project folder:
   cd Project-2
4. Enter your API key in main.py:
   client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="ENTER_YOUR_API_KEY_HERE",
)
5. Run the application using Streamlit:
   streamlit run main.py
6. Enter your API key in the sidebar of the application to authenticate and use the AI services.


Enjoy using the AI Marketing Strategy Creator!
