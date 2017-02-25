#!/usr/bin/env python3
# this won't run on GNU/Linux systems without py3, than again it won't run on
# GNU/Linux systems at all :^)
# DIDEY THE FIRST

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import pyautogui

while(True):
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        audio_string = r.recognize_google(audio)
        print("Google Speech Recognition thinks you said " + audio_string)
        check_string = audio_string.lower()
        check_string = check_string.replace(".", "")
        print("final toCheck: " + check_string)
        if check_string == "xbox record" or check_string == "xbox record that" or check_string == "xbox, record that" or check_string == "xbox, record":
            pyautogui.hotkey('alt', 'f10')
            print("Recording...")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
