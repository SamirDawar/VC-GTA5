# Python program to translate
# speech to text and text to speech


#TODO INSTALL AND IMPORT PIP KEYBOARD
import speech_recognition as sr
import pyttsx3
import pyautogui as pg

#GLOBAL
FinalText = ""

words = ["skedaddle", "halt", "yonder", "launder", "f sharp", "f flat", "pardon me", "excuse me", "jump"]



# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command) 
	engine.runAndWait()

			





# Loop infinitely for user to
# speak

#TODO change to push to talk
while(1): 
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input 
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()
			FinalText = MyText
			print(FinalText)
			match FinalText:
				case "skedaddle":
					pg.keyDown("w")
			
        
            
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")
	