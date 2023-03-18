import os
import openai

openai.api_key = 'apikey'

input_str = 'init'
messages=[]

while True:
    input_str = input("chatgpt君に申したい事:")
    if input_str == 'end':
        break

    messages.append({"role": "user", "content": input_str})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = messages
    )
    res_message = response.choices[0]["message"]["content"].strip()
    print(res_message)
    messages.append({"role": "assistant", "content": res_message})
    print(messages)
