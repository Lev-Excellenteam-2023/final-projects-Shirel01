import openai
import asyncio


def send_query(questions: str) -> list:
    # Set up your OpenAI API credentials

    file = open('api_key.txt', 'r')
    my_api_key = file.read()
    openai.api_key = my_api_key
    # Define the messages input in the chat format
    messages = [{'role': 'user', 'content': questions}]
    # Generate the completion
    completion =  openai.ChatCompletion.create(
        messages=messages,
        model="gpt-3.5-turbo"
    )
    return completion


def extract_response(completion):
    # Retrieve the generated completion text
    response = completion.choices[0].message.content
    return response



