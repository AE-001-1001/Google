import speech_recognition as sr
import time as t
import intents as it


r = sr.Recognizer()

sr.Microphone.list_microphone_names()

mic = sr.Microphone(device_index=1)


def speech(synth):
    # if user says statement
    if synth == "hello":
        print(it.statements[0])
    if synth == "hi":
        print(it.statements[1])
    if synth == "hey":
        print(it.statements[2])
    if synth == "hullo":
        print(it.statements[3])
    # if user asks a question
    if synth == "how are you":
        print(it.questions)
    if synth == "whats up":
        print(it.questions)
    if synth == "what are you doing":
        print(it.questions)
    if synth == "what are you up to":
        print(it.questions)
    # if user says a statement and then asks a question
    if synth == "Hi how are you":
        print(it.statements[1] , " " , it.questions)
    if synth == "hello whats up":
        print(it.statements[0] , " " , it.questions)
    if synth == "hey what are you doing":
        print(it.statements[2] , " " , it.questions)
    if synth == "hullo what are you up to":
        print(it.statements[3] , " " , it.questions)
    print(synth)
    print(t.process_time())
    return synth

# use the function speech() to get the user's input
# and then use the function speech() to compare the user's input
# to the statements and questions in intents.py
# and then print the appropriate response

while True:
    with mic as source:
        print("Say something")
        audio = r.listen(source)
        # wait for 300 milliseconds before listening again
        r.pause_threshold = 0.54
        print("Time Over, thanks")
        synth = r.recognize_google(audio)
        speech(synth)
