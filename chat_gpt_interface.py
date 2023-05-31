import openai
import openai
from json_utils import save_to_json

def send_query(api_key, query):
    openai.api_key = api_key

    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=query,
        max_tokens=100,
        temperature=0.7
    )

    reply = response.choices[0].text.strip()

    # Create a dictionary to store the query and response
    data = {
        'query': query,
        'response': reply
    }

    save_to_json(data, 'response.json')

    return reply

