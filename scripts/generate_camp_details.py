import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Create a fictional GenAI Summer Camp including offerings, values, policies, location, dates, pricing, and age range in about 4060 words."
    }
  ],
  temperature=0.5,
  max_tokens=4060,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)