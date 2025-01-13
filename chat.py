import os
import openai

openai.api_key = "API KEY"
def get_completion_and_token_count(messages,
                                   model="gpt-4o-mini",
                                   temperature=0,
                                   max_tokens=500):

    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = response.choices[0].message["content"]

    token_dict = {
'prompt_tokens':response['usage']['prompt_tokens'],
'completion_tokens':response['usage']['completion_tokens'],
'total_tokens':response['usage']['total_tokens'],
    }
    return content, token_dict
messages = [
{'role':'system',
 'content':"""You are an assistant who responds\
 in the style of Dr Seuss."""},
{'role':'user',
 'content':"""write me a very short poem \
 about a happy carrot"""},
]
response, token_dict = get_completion_and_token_count(messages)

print(token_dict)