# Lets import the pyttsx3 package here
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices") 
# If you want to see all the available voices on your device
# Use print(voices)

engine.setProperty("voice",voices[0].id) # For example if you want another voices, Set it to voices[1].id 

# This function would allow our pc to speak
def speak(input):
    engine.say(input)
    engine.runAndWait()


# Now lets create some basic function for our input
def inputCommand():
    textInput = input("What do you want me to speak?:\n")
    text = textInput.lower()
    speak(text)



# Main function setup
if __name__ == "__main__":
    while True:
        inputCommand()