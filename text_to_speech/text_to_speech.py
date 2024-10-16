import pyttsx3 as p

def textToSpeech():

    text_speech = p.init()

    #var = input("enter the input =   " )

    fvar = open('news.txt' , 'r')
    var = fvar.read()
    fvar.close()

    voices = text_speech.getProperty('voices')
    print("\n ========================================== \n")
    for x in voices:
        print(x.id,x.name,x.languages)
    print("\n ========================================== \n")
        

    """SPEAKING RATE"""
    # getting details of current speaking rate
    rate = text_speech.getProperty('rate')   
    print (rate)
    # Changing the voice rate less the value more the time taken to convey the message 
    text_speech.setProperty('rate', 100)


    """VOLUME"""
    #getting to know current volume level (min=0 and max=1)
    volume = text_speech.getProperty('volume')
    #printing current volume level
    print (volume)
    # setting up volume level  between 0 and 1
    text_speech.setProperty('volume',1.0)



    """VOICE"""
    #getting details of current voice
    voices = text_speech.getProperty('voices')
    print(voices)
    #changing index, changes voices. 0 for male
    #engine.setProperty('voice', voices[0].id)
    #changing index, changes voices. 1 for female
    text_speech.setProperty('voice', voices[0].id)


    """SAVING VOICE TO FILE"""
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    # text_speech.save_to_file(var , 'test2.mp3')
    # print(" Saaved the file ")


    # Speaking the scentence.
    text_speech.say(var)

    text_speech.save_to_file(var, 'test2.mp3')
    print(" Saaved the file ")

    text_speech.runAndWait()
    text_speech.stop()



textToSpeech()
