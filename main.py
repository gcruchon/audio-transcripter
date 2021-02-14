# This is a sample Python script.

import speech_recognition as sr
from os import path
from pydub import AudioSegment

# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio/test-francais.m4a")
FLAC_FILE = path.join(path.dirname(path.realpath(__file__)), "tmp/audio.flac")

print("--- Start reading file '" + AUDIO_FILE + "'")
audio = AudioSegment.from_file(AUDIO_FILE)
print("End reading file")

print("--- Start encoding to FLAC")
audio.export(FLAC_FILE, format="flac")
print("End encoding to FLAC '" + FLAC_FILE + "'")


r = sr.Recognizer()
print("--- SpeechRecognition reading FLAC...")
with sr.AudioFile(FLAC_FILE) as source:
    audio = r.record(source)  # read the entire audio file
print("SpeechRecognition read FLAC.")

# recognize speech using Sphinx
print("--- Start audio file transcription...")
try:
    print("### Sphinx thinks you said: " + r.recognize_sphinx(audio, language="fr-FR"))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))