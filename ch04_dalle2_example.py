import openai
import urllib

openai.api_key = "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"

response = openai.Image.create(
    prompt="A futuristic city at night",
    n=1,
    size="512x512"
)

image_url = response['data'][0]['url']
print(image_url)
urllib.request.urlretrieve(image_url, "test.jpg")