from gtts import gTTS

import os

languages = ["en", "fr", "zh-CN", "pt", "es"]
language_name = ["English", "French", "Chinese", "Portuguese", "Spanish"]

print("In Which language Karal will talk?  ")
for i in range(len(language_name)):
    print(str(i+1), str(language_name[i]))
lang = int(input("Enter your choice (1-5)? "))
language_choice = language_name[lang-1]
language = languages[lang-1]

print(language_choice)
try:
    f = open("text.txt", "r")
    mytext = f.read()
except:
    mytext = 'File is not found in location, please keep it properly'
    language = languages[0]

myobj = gTTS(text=mytext, lang=language, slow=False)


myobj.save("welcome.mp3")


os.system("start welcome.mp3")
