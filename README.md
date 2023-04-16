# Discord Chatbot using ChatGPT

This is a Discord bot that uses OpenAI's GPT-3.5 language model through the ChatGPT API to generate responses to messages sent in a Discord server. The bot is built with Python and uses the `discord.py` library.

## Requirements

- `discord.py==2.1.0`
- `openai==0.27.0`
- `python-dotenv==0.21.0`
- `requests==2.25.1`

You will also need to set up an OpenAI account and API key to use the ChatGPT API. Refer to the OpenAI documentation for more information.

## Installation

1. Clone this repository
2. Install the required packages by running `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your Discord bot token and ChatGPT API key as environment variables:
```
DISCORD_TOKEN = <your Discord bot token>
CHATGPT_API_KEY = <your ChatGPT API key>
```

4. Run `python run.py` to start the bot

## Usage

Once the bot is running and added to your Discord server, it will automatically listen for messages and respond using the ChatGPT API. The bot will only respond to messages that begin with a specified prefix `('/ai', '/bot', '/chatgpt')` (which can be changed in the `dicord_api.py` file).

## Acknowledgements

This project was built with the help of the `discord.py` library and the OpenAI API. Special thanks to the developers of these tools for making this project possible.
