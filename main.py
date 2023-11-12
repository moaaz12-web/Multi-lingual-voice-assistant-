import os
import openai
import random
import sounddevice as sd

from record import new_record_audio, generate_random_name
from whisper import transcribe_audio

from tts_elevenLabs import generate_audio
from elevenlabs import generate, play


from openai import OpenAI
client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])


# Set your OpenAI API key here
import time
from dotenv import load_dotenv
load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# Global variable to store audio data
audio = []


def main():

    language = input("What langauge you want to learn: ")
    print("Let's get started! Speak into the microphone.")


    while True:

        print("Press 's' to stop recording and transcribe the audio.")
        
        #! Start recording live voice input
        recorded_audio_path = new_record_audio()
        print("Recording stopped. Transcribing audio...")
        
        #! Save the recorded audio as a WAV file
        # print("Recorded audio saved to:", recorded_audio_path)
        # print("----end----")
        
        #! Transcribe the audio
        transcript = transcribe_audio(recorded_audio_path)
        
        #! Create a list of messages with the user's input
        messages = [
            {"role": "system", "content": f"You are a helpful assistant that only responds in {language}. Do not speak in any other language except than {language}"},
            {"role": "user", "content": transcript}
        ]

        # print("Transcript:")
        print("Audio to text output: ", transcript)
        
        #! Make the API call for gpt AI
        completion = client.chat.completions.create(
            messages=messages,
            model="gpt-3.5-turbo",
        )
        response = completion.choices[0].message.content
        print("Assistant:", response)
        
        #! Convert output to voice
        audio = generate_audio(response)
        play(audio)

        #! Ask whether to continue or stop
        user_choice = input("Continue? (y/n): ")
        if user_choice.lower() != "y":
            recordings_folder = "./recordings"
            for file_name in os.listdir(recordings_folder):
                file_path = os.path.join(recordings_folder, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")
            audio = generate_audio("Ok. Good bye!")
            play(audio)
            break 



if __name__ == "__main__":
    main()









# import speech_recognition as sr

# # Initialize the recognizer
# r = sr.Recognizer()

# while True:
#     # Use the microphone as source for input.
#     with sr.Microphone() as source:
#         # Adjust the energy threshold based on the surrounding noise level
#         r.adjust_for_ambient_noise(source, duration=0.5)

#         print("Speak!! ")
#         audio = r.listen(source)

#         try:
#             # text = r.recognize_google(audio, language = "fr-FR")
#             text = r.recognize_google(audio, language = 'en-US')
#             print(text)

#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))

        