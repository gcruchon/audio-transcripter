# This is a sample Python script.

import speech_recognition as sr
from os import path
from pydub import AudioSegment

AUDIO_LANGUAGE = "fr-FR"

# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio/mc4.mp3")
TRANSCRIPT_FILE = path.join(path.dirname(path.realpath(__file__)), "audio/mc4.txt")
WAV_FILE = path.join(path.dirname(path.realpath(__file__)), "tmp/audio.wav")
CHUNK_SIZE = 5 #seconds
AZURE_SPEECH_KEY = "xxx"
AZURE_LOCATION = "westeurope"
USE_AZURE = True

transcript_file = open(TRANSCRIPT_FILE, "w")
print("--- Start reading file '" + AUDIO_FILE + "'")
audio = AudioSegment.from_file(AUDIO_FILE)
print("End reading file")

print("--- Start transcripting chunks")

r = sr.Recognizer()

for i in range(12):
    chunk = audio[(i * CHUNK_SIZE * 1000):((i+1) * CHUNK_SIZE * 1000)]
    chunk.export(WAV_FILE, format="wav", bitrate="16k")

    prefix = "[" + str(i * CHUNK_SIZE) + "s to " + str((i+1) * CHUNK_SIZE) + "s]: "
    with sr.AudioFile(WAV_FILE) as source:
        audio_to_transcript = r.record(source)  # read the entire audio file
    try:
        if USE_AZURE:
            transcript_chunk = r.recognize_azure(audio_to_transcript, key=AZURE_SPEECH_KEY, location=AZURE_LOCATION, language=AUDIO_LANGUAGE)
        else:
            transcript_chunk = r.recognize_sphinx(audio_to_transcript, language=AUDIO_LANGUAGE)

        transcript_file.write(prefix + transcript_chunk + "\n")
        print(prefix + transcript_chunk)
    except sr.UnknownValueError:
        if USE_AZURE:
            print(prefix + "Microsoft Azure Speech could not understand audio")
        else:
            print(prefix + "Sphinx could not understand audio")
    except sr.RequestError as e:
        print(prefix + "Could not request results; {0}".format(e))

transcript_file.close()
print("Finished")