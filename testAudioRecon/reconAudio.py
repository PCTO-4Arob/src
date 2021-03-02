from google.cloud import speech
import os
import io

client = speech.SpeechClient()

file_name = os.path.join(os.path.dirname(__file__), "recording0.wav")

with io.open(file_name, "rb") as audio_file:
    content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    audio_channel_count=2,
    language_code="ita-EU",
)

response = client.recognize(request={"config":config, "audio":audio})

for result in response.result:
    print("Trasnscript: {}".format(result.alternatives[0].transcript))