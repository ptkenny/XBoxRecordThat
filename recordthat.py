#!/usr/bin/env python3
# this won't run on GNU/Linux systems without py3, than again it won't run on
# GNU/Linux systems at all :^)
# DIDEY THE FIRST

import speech_recognition as sr
import pyautogui

while(True):
	# Sets mic to record from to default device...
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for input...")
        audio = r.listen(source)
    try:
        audio_string = r.recognize_google(audio)
        print("you said: " + audio_string)
		# Lowers the string here so I don't have to do .lower on all comparisons later.
        check_string = audio_string.lower()
		# I do this here because google likes to add periods to the end of voice commands.
        check_string = check_string.replace(".", "")
        print("final toCheck: " + check_string)
        if check_string == "xbox record" or check_string == "xbox record that" or check_string == "xbox, record that" or check_string == "xbox, record":
            pyautogui.hotkey('alt', 'f10')
            print("Triggering Shadowplay...")
    except sr.UnknownValueError:
        print("ERROR: Couldn't understand audio, did you say anything?")
    except sr.RequestError as e:
        print("Google speech recognition isn't working, check if it's down! error; {0}".format(e))
