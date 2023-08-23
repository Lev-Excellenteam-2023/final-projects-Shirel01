import openai
import asyncio


async def send_query(questions: str) -> list:

    file = open('api_key.txt', 'r')
    my_api_key = file.read()
    openai.api_key = my_api_key
    messages = [{'role': 'user', 'content': "Explain this slide of PowerPoint: " + ' '.join(questions)}]

    # Generate the completion
    completion = await openai.ChatCompletion.acreate(
        messages=messages,
        model="gpt-3.5-turbo"
    )
    return completion.choices[0].message.content
