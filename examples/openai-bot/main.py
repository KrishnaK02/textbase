from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"  # Replace with your API key

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with a recipe instruction chatbot. You can ask for recipe instructions by providing the name of a dish, such as "How do I make spaghetti bolognese?"
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Extract user input from the last message
    user_input = message_history[-1].content if message_history else ""

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, 
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }
