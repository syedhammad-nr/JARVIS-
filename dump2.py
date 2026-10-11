from google import genai
import box

client = genai.Client(api_key=box.geminikey)

interaction = client.interactions.create(
    model="gemini-3.8-flash",
    input="Say hello in one sentence."
)

print(interaction.output_text)