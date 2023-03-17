import openai

# Your DALL-E API key
openai.api_key = "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"

# The text prompt you want to use to generate an image
prompt = "High quality photo of a jindo astronaut"

# Generate an image
response = openai.Image.create(
    prompt=prompt, # text prompt used to generate the image
    model="image-alpha-001", # DALL-E model to use for image generation.
    size="1024x1024",
    response_format="url"
)

# Print the URL of the generated image
print(response["data"][0]["url"])
