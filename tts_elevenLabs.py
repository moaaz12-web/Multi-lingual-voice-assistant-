
from elevenlabs import generate, play
import os
from elevenlabs import set_api_key
from dotenv import load_dotenv
load_dotenv()
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

def generate_audio(text):
    audio = generate(
        text=text,
        voice="Bella",
        model="eleven_multilingual_v2"
    )
    return audio

# audio = generate_audio("现在用中文写一句话：太阳在蓝天中照耀")
# play(audio)