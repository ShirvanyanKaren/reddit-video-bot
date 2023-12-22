from gtts import gTTS 

def getVoiceover(fileName, text):
    print("here")
    tts = gTTS(text=text, lang='en', slow=False, tld="co.uk")
    filePath = f"{fileName}"
    print(filePath)
    tts.save(filePath)
    print("done")
    return filePath