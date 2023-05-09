from tkinter import *
from gtts import gTTS
import os
root=Tk()
Label(root,text="enter your name").pack()
entry = Entry(root)
entry.pack()

def button_click():
   
    a=entry.get()
    print(a)
    output=gTTS(text=a,lang="en",slow=False)
    output.save('trial.mp4')
    os.system('start trial.mp4')


Button(root,text="play",command=button_click).pack()

root.mainloop()