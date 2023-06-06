import openai

def send_query(questions: str) -> list:
    # Set up your OpenAI API credentials

    file = open ('api_key.txt', 'r')
    my_api_key = file.read()
    openai.api_key = my_api_key

    # Define the parameters for the completion
    model = 'gpt-3.5-turbo'
    max_tokens = 100
    temperature = 0.8
    # Define the messages input in the chat format
    messages = [
        {'role': 'system', 'content': 'You are a helpful assistant.'},
        {'role': 'user', 'content': questions}
    ]
    # Generate the completion
    response = openai.ChatCompletion.create(
        messages=messages,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        stop=None,
        model="gpt-3.5-turbo"
    )
    # Retrieve the generated completion text
    completions = response.choices[0].message.content# .strip().split('\n')

    return completions






