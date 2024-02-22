from openai import OpenAI
client = OpenAI()

audio_file= open("C:/Users/User/Downloads/New Recording 7.m4a", "rb")
transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file
)