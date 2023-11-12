from scipy.io.wavfile import write
import sounddevice as sd
import random

# Adjectives to generate random names for voices
adjectives = ["beautiful", "sad", "mystical", "serene", "whispering", "gentle", "melancholic"]
nouns = ["sea", "love", "dreams", "song", "rain", "sunrise", "silence", "echo"]
 
def generate_random_name():
    # to generate random unique names for the audio voice recordings
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

def new_record_audio():
    # to record audio as wav file
    print("Recording... Press 's' to stop.\n")
    fs = 44100
    seconds = 6
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    audio_name = generate_random_name()
    write(f'./recordings/{audio_name}.wav', fs, myrecording)  # Save as WAV file 
    print("Recording stopped.\n")
    return f'./recordings/{audio_name}.wav'