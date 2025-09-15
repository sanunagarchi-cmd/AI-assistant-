from tkinter import*
from PIL import Image, ImageTk

root=Tk()
root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="#6F8FAF")

import speech_to_text
import action

def ask():
    user_val = speech_to_text.speech_to_text()   # call function, not reference
    text.insert(END, 'User ---> ' + str(user_val) + "\n")
    bot_val = action.act(user_val)   # call act()
    if bot_val is not None:
        text.insert(END, "BOT <--- " + str(bot_val) + "\n")
    if bot_val and "shutdown" in bot_val.lower():
        root.destroy()

def send():
    user_msg = entry.get()   # get user input
    text.insert(END, "User ---> " + user_msg + "\n")
    bot = action.act(user_msg)   # call act()
    if bot is not None:
        text.insert(END, "BOT <--- " + str(bot) + "\n")
    if bot and "shutdown" in bot.lower():
        root.destroy()

def del_text():
    text.delete('1.0',"end")

frame=LabelFrame(root, padx=95,pady=7,borderwidth=3,relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0,column=0,padx=55,pady=10)

text_label=Label(frame,text="AI Assistant",font=("comic Sans ms",14,"bold"),bg="#356696")
text_label.grid(row=0,column=0,padx=15,pady=10)

image=ImageTk.PhotoImage(Image.open("boyimage.png"))
image_label=Label(frame,image=image)
image_label.grid(row=1,column=0,pady=20)

text=Text(root,font=("courior 10 bold"),bg="#356696")
text.grid(row=2,column=0)
text.place(x=80,y=375,width=375,height=100)

entry=Entry(root,justify=CENTER)
entry.place(x=90,y=500,width=350,height=30)

button1=Button(root,text="ASK", bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=70,y=575)

button2=Button(root,text="Send", bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
button2.place(x=400,y=575)

button3=Button(root,text="Delete", bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=del_text)
button3.place(x=225,y=575)

root.mainloop()