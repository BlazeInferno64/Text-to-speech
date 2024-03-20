# Introduction
Ever wanted to make your PC speak?
Fortunately its possible now :)
|-----|
# About

This program needs python to work,
So if you don't have it download from here -
<br>

<a href="https://python.org/download">
https://python.org/download
</a>
<br>
<br>
This example will show you how you can make your PC say,whatever you want!
<br>
But-but it wont happen until you install the required Python libraries for that!
<br>

Paste the following commands in your terminal before running the program -


```
pip install pyttsx3 pyaudio
```

or 

```
pip install requirements.txt
```

# Basic breakdown

Let me give you some brief breakdown details about the program!
<br>
So, basically first of all lets import some libraries into the script

```
import pyttsx3
```

Then we gotta setup the voice otherwise our PC wont be able to speak!

```
engine = pyttsx3.init()
voices = engine.getProperty("voices") 
# If you want to see all the available voices on your device
# Use print(voices)
engine.setProperty("voice",voices[0].id) # For example if you want another voices, Set it to voices[1].id 
```

As we have setup the voice, now lets create some basic functions

```
# This function would allow our pc to speak
def speak(input):
    engine.say(input)
    engine.runAndWait()
```
And then -

```
# Function for user input
def inputCommand():
    textInput = input("What do you want me to speak?:\n")
    text = textInput.lower()
    speak(text)
```

Lastly lets finish this with -

```
# Main function setup
if __name__ == "__main__":
    while True:
        inputCommand()
```


Alright that's it!
<br>
Also, you can run the executables made for the scripts from the `app` directory
There are 2 executables
1. TextToSpeech-1 (Its the executable for the first voice)
2. TextToSpeech-2 (Its the executable for the second voice)

`
Thanks for reading :)
`
<br>
`
Have an absolutely fantastic day ahead :D
`




