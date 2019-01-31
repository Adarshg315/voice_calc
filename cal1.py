import speech_recognition as sr 
from win32com.client import Dispatch
import numpy as np

r = sr.Recognizer()

speak = Dispatch("SAPI.SpVoice")
speak.Volume = 100
speak.Rate = 3

speak.Speak('''This is the voice calculator,Speak out the operation like 
					   first number, operation to be performed and then the second number.
					   For example, for 1 + 2 say one, plus, two and so on....
					   Speak the operation''')
	
while(True):
	with sr.Microphone() as source:
		audio1 = r.listen(source)
		
		
		inputString = r.recognize_google(audio1, language= "en-IN")
		#speak.Speak(" You said {} " + inputString)
		
		inputString = inputString.replace("into", "*")
		inputString = inputString.replace("add ", "")
		inputString = inputString.replace("product of", "")
		inputString = inputString.replace("x", "*")
		inputString = inputString.replace("X", "*")
		inputString = inputString.replace("addition of", "")
		inputString = inputString.replace("division of", "")
		inputString = inputString.replace("from", "")
		inputString = inputString.replace("point", ".")
		inputString = inputString.replace("dot", ".")
		inputString = inputString.replace("divided by", "/")
		inputString = inputString.replace("multiplied by", "*")
		inputString = inputString.replace("equal", "")
		inputString = inputString.replace("=", "")
		inputString = inputString.replace("minus", "-")
		inputString = inputString.replace("plus", "+")
		inputString = inputString.replace("one", "1 ")
		inputString = inputString.replace("two", "2")
		inputString = inputString.replace("three", "3")
		inputString = inputString.replace("four", "4")
		inputString = inputString.replace("five", "5")
		inputString = inputString.replace("six", "6")
		inputString = inputString.replace("seven", "7")
		inputString = inputString.replace("eight", "8")
		inputString = inputString.replace("nine", "9")
		inputString = inputString.replace("ten", "10")
		inputString = inputString.replace("do", "")
		inputString = inputString.replace("evaluate", "")
			
		print("You said :", inputString)
		
		speak.Speak("output is {} " + str(eval(inputString))) 
		print("output is : ", eval(inputString))
		
		speak.Speak("Do you want to continue or exit")
		audio2 = r.listen(source)
		inputString = r.recognize_google(audio2, language= "en-US")
		
		if inputString == "continue":
			speak.Speak("speak another operation")
			continue
		elif inputString == "exit":
			print("Terminating")
			speak.Speak("Terminating")
			break
