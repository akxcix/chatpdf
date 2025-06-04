from openai import OpenAI

base_url = 'http://localhost:11434/v1'
api_key = 'ollama'
model = "gemma3:4b"

client = OpenAI(
    base_url=base_url,
    api_key=api_key,
)

def get_completion_ollama(messages, model=model):
    """
    Given the prompt messages in OpenAI protocol format, runs this as a client to Ollama
    and returns the results.
    :param messages: list of messages constituting a prompt (following OpenAI chat format)
    :param model: model to invoke
    :return: response (results) as a string
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.0,
        # stream=True,
    )
    output = response.choices[0].message.content
    return output
