import speech_recognition as sr
import time as t
import intents as it


r = sr.Recognizer()

sr.Microphone.list_microphone_names()

mic = sr.Microphone(device_index=1)

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    synth = r.recognize_google(audio)
    # if user says something
    if synth == "hello":
        print(it.intent[0])
    if synth == "how are you":
        print(it.intent[1])
    if synth == "whats up":
        print(it.intent[2])
    
    print(t.process_time())