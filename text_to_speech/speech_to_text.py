import speech_recognition as sr
import pyttsx3
# from nlpprogs import *

# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


# Loop infinitely for user to
# speak


while (1):

    # Exception handling to handle exceptions at the runtime
    try:

        print("Please speak = ")
        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)

            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ", MyText)
            SpeakText(MyText)

            # nlpwords = text_parser_synonym_antonym_finder(MyText)
            # print(nlpwords)

            if('stop' in MyText.lower()):
                SpeakText("Thanks for using voice service Have a good day")
                break

            if('politics' in MyText.lower()):
                SpeakText("I will read the politics news")

            if('sports' in MyText.lower()):
                SpeakText("I will read the sports news")

            if('movies' in MyText.lower()):
                SpeakText("I will read the film news")


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")