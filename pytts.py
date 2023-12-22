import pyttsx3
import os



def create_voice_over(fileName, text):
    filePath = "E://test.mp3"
    engine = pyttsx3.init('nsss')
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 0.9)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[14].id)
    engine.say(text)
    file = engine.save_to_file(text, 'F:\\Audio Video Creator\\output\\test.mp3')
    engine.runAndWait()
    return file


file = create_voice_over("test.mp3", "hello world")

print(file)

