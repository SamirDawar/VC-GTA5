import speech_recognition as sr
import pyttsx3
import pyautogui as pg
import time

#GLOBAL
FinalText = ""

words = ["skedaddle", "halt", "yonder", "launder", "f sharp", "f flat", "pardon me", "excuse me", "jump"]

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command) 
    engine.runAndWait()

while(1): 
    try:
        # use the microphone as source for input.
        with sr.Microphone() as source2:
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
                    for _ in range(3):  # Repeat 3 times (1 second each)
                        pg.press("w")
                        
                case "halt":
                    pg.press("s")
                    time.sleep(2)
                        
                case "yonder":
                    pg.press("d")
                    time.sleep(3)
                        
                case "launder":
                    pg.press("a")
                    time.sleep(3)
                        
                case "f sharp":
                    pg.press("d")
                    time.sleep(3)
                        
                case "f flat":
                    pg.press("a")
                    time.sleep(3)
                        
                case "pardon me":
                    pg.press("d")
                    
                case "excuse me":
                    pg.press("a")
                    
                case "jump":
                    pg.press("l")
                    
                case "fuck":
                    pg.press("p")
                    
                case "ass":
                    pg.press("p")
                    
                case "like":
                    pg.press("p")
                    
                case _:
                    print("Word Invalid")

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        
    except sr.UnknownValueError:
        print("Unknown error occurred")
