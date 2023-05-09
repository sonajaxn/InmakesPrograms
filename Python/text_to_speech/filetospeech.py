from gtts import gTTS
import os
text=open('audio_file.txt','r',encoding='utf-8').read()
language='hi'
output=gTTS(text=text,lang=language,slow=False)
output.save('file.mp4')
os.system('start file.mp4')