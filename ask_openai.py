from openai import OpenAI

import urllib3  
# or if this does not work with the previous import:
# from requests.packages import urllib3  

# Suppress only the single warning from urllib3.
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

API_KEY = "sk-vtyvGev7fk5oTcEuwF1ha6Q_YKvH8RCysht9cxkDO0T3BlbkFJ7PAiOFKYJCHpaaTMvASXFtC9OPTkVeeM48efx5nmgA"

client = OpenAI(api_key="sk-vtyvGev7fk5oTcEuwF1ha6Q_YKvH8RCysht9cxkDO0T3BlbkFJ7PAiOFKYJCHpaaTMvASXFtC9OPTkVeeM48efx5nmgA")

OpenAI.api_key = "sk-vtyvGev7fk5oTcEuwF1ha6Q_YKvH8RCysht9cxkDO0T3BlbkFJ7PAiOFKYJCHpaaTMvASXFtC9OPTkVeeM48efx5nmgA"

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What’s in this image?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])