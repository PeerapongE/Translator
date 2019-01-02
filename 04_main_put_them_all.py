# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 15:48:43 2018

@author: PeerapongE
"""
# Audio recorder
import speech_recognition as sr 
# Translator
from py_translator import Translator 
# Text to Speech
from gtts import gTTS
import os

# language selection
# https://py-googletrans.readthedocs.io/en/latest/

# fix input language to be only Thai in this workshop

dest_lang = 'en'    # English (Default)
#dest_lang = 'zh-cn' # Chinese
#dest_lang = 'fr'    # French
#dest_lang = 'vi'    # Vietnamese


#'vi': 'vietnamese'
#'zh-cn': 'chinese (simplified)'
#'fr': 'french' #OK

#%% Step-1: Voice recording
print('----- Step-1 Recording -----')

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print('Please speaking in Thai') 
    audio = r.listen(source) # , duration=4
    print("Time's up")
    
print('Speech to text in progress')
#r.recognize_google(audio) # default language is english
InputText = r.recognize_google(audio, language="th")

print(InputText)

#%% Step-2: Translation
print('----- Step-2 Translating -----')

translator = Translator()

translations = translator.translate(text = InputText,
                                    src  = 'th',
                                    dest = dest_lang)

OutputText  =  translations.text

print('Translated Text : ' + OutputText)

#%% Step-3: Text to speech

OutputAudioFileName = 'AudioTranslate.mp3'

# Text to speech
tts = gTTS(text= OutputText, lang = dest_lang)
# Save file as filename
tts.save(OutputAudioFileName)
# Play the file
os.system(OutputAudioFileName)
