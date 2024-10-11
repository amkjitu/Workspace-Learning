import openai
import os
import time

openai.organization = "org-1OfzC0w4XfBp398Cr5vmXMIi"
openai.api_key = "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"
#print(openai.Model.list())


completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)

# completion = openai.ChatCompletion.create(model="curie-search-query", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
# print(completion.choices[0].message.content)
# time.sleep(2)
