from openai import OpenAI
import base64
import requests

import urllib3  
# or if this does not work with the previous import:
# from requests.packages import urllib3  

# Suppress only the single warning from urllib3.
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

api_key = ""

client = OpenAI(api_key="")

# OpenAI.api_key = ""

# set image path
image_path = r"./image.jpg"

# create image encode function
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

base64_image = encode_image(image_path)

# set headers
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

# create payload
payload = {
  "model": "gpt-4o",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "What items are on the tray?"
        },
        {
          "type": "image_url",
          "image_url": { "url": f"data:image/jpeg;base64,{base64_image}"}
        }
      ]
    }
  ],
  "max_tokens": 600
}

# make api request
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# print response
print(response.json()["choices"][0]["message"]["content"])



# response = client.chat.completions.create(
#   model="gpt-4o-mini",
#   messages=[
#     {
#       "role": "user",
#       "content": [
#         {"type": "text", "text": "What’s in this image?"},
#         {
#           "type": "image_url",
#           "image_url": {
#             "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
#           },
#         },
#       ],
#     }
#   ],
#   max_tokens=300,
# )

# print(response.choices[0])