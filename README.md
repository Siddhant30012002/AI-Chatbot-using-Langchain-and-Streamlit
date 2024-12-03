# AI Chatbot using Falcon 7B

## Description
This AI chatbot uses the **Falcon 7B instruct** pre-trained language model from **Hugging Face** using the **Langchain Framework** to generate intelligent, human-like responses. Built with Streamlit and Langchain, it allows users to interact with the chatbot through a simple, user-friendly interface.

## Features
- **Powered by Falcon 7B instruct**: Leverages a state-of-the-art language model.
- **Interactive UI**: Built with Streamlit for seamless user interaction.
- **Customizable**: Easily modify the chatbot’s behavior by adjusting the model settings.

## Installation

To run the chatbot locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Siddhant30012002/AI-Chatbot-using-Langchain-and-Streamlit.git
    ```

2. Navigate to the project directory:
    ```bash
    cd falcon-chatbot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the Hugging Face API key:
    - Create an account at [Hugging Face](https://huggingface.co/) and obtain an API key.
    - Set the API key in your environment variables:
      ```bash
      export API_KEY="your_huggingface_api_key"
      ```

5. Run the chatbot:
    ```bash
    streamlit run app.py
    ```

## Usage

Once running, visit the Streamlit app in your browser and interact with the chatbot. Type your questions, and the chatbot will respond using the Falcon 7B instruct model.

## Technologies Used
- **Falcon 7B**: A pre-trained language model from Hugging Face.
- **Streamlit**: For the interactive frontend.
- **Langchain**: For chaining model prompts.
- **Python**: Backend code.


## Contact
For inquiries, reach me at [siddhantkadiyal08@gmail.com].
