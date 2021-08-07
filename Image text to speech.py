
import easyocr

image_path = 'b.jpg'
reader = easyocr.Reader(['en'],  gpu=False)  # need to run only once to load model into memory
result = reader.readtext(image_path, detail=0)

print(result)

import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 178)
engine.say('The Character is ')
engine.say(result)
engine.runAndWait()