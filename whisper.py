
import openai
import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# def transcribe_audio(audio_path):
#     print ("entered transcribe", "./recordings/"+audio_path)
#     audio_file= open(audio_path, "rb")
#     transcript = openai.Audio.transcribe("whisper-1", audio_file)
#     # print(transcript)
#     return transcript['text']

# res= transcribe_audio("./266634952-778fd3ed-0a3a-4d66-8f73-faee099dfdd6.webm")
# print(res)


from openai import OpenAI
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# audio_file= open("/path/to/file/audio.mp3", "rb")
# transcript = client.audio.transcriptions.create(
#   model="whisper-1", 
#   file=audio_file
# )

def transcribe_audio(audio_path):
    audio_file= open(audio_path, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
    )
    return transcript.text
