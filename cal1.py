import time 
import re
import speech_recognition as sr
from win32com.client import Dispatch


r = sr.Recognizer()

speak = Dispatch("SAPI.SpVoice")
speak.Volume = 100
speak.Rate = 4

# speak.Speak('''This is the voice calculator,Speak out the operation like 
# 					   first number, operation to be performed and then the second number.
# 					   For example, for 1 + 2 say one, plus, two and so on....
# 					   Speak''')
	
while(True):
	with sr.Microphone() as source:
		audio1 = r.listen(source)
		inputString = r.recognize_google(audio1, language= "en-IN")
		
		speak.Speak(" You said {} " + inputString)
		print("You said :", inputString)
		

		speak.Speak("output is {} " + str(eval(inputString)))
		print("output is : ", eval(inputString))
		
		speak.Speak("Do you want to continue or exit")
		audio2 = r.listen(source)
		inputString = r.recognize_google(audio2, language= "en-US")
		
		if inputString == "continue":
			print("You said :" , inputString,)
			speak.Speak("now speak another operation")
			continue
		elif inputString == "exit":
			print("Terminating")
			speak.Speak("Terminating")
			break
			
		
	
