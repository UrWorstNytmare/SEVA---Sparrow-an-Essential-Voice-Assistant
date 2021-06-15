import os
import datetime
import time
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import pyttsx3
import speech_recognition as sr
from speech_files import tc
from sparrow import response

engine = pyttsx3.init('sapi5')
voice= engine.getProperty('voices')
engine.setProperty('voice', 'voice[0].id')

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 12"
FONT_BOLD = "Helvetica 11 bold"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
img_path1 = os.path.join(BASE_DIR, "voice.png")
img_path2 = os.path.join(BASE_DIR, "sparrow.ico")

global greet

hour = datetime.datetime.now().hour
if hour>=0 and hour<12:
    greet = "Good Morning!"
elif hour>=12 and hour<18:
    greet = "Good Afternoon!"
else:
    greet = "Good Evening!"

class Assist_GUI:

    def __init__(self):
        self.root = Tk()
        self._setup_main_window()

    def run(self):
        self.root.mainloop()
    
    def speak(self, text):
        engine.say(text)
        engine.runAndWait()
    
    def _setup_main_window(self):
        self.root.title("SEVA - Sparrow an Essential Voice Assistant")
        self.root.iconbitmap(img_path2)
        self.root.resizable(width=False, height=False)
        self.root.configure(width=520, height=700, bg=BG_COLOR)

        # head label
        head_label = Label(self.root, bg=BG_COLOR, fg=TEXT_COLOR, text=greet, font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)

        # tiny divider
        line = Label(self.root, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.008)

        # text area
        self.text_widget = Text(self.root, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)

        # scroll bar
        scroll_widget = Scrollbar(self.text_widget)
        scroll_widget.place(relheight=1, relx=0.970)
        scroll_widget.configure(command=self.text_widget.yview)

        # bottom label
        bottom_label= Label(self.root)
        bottom_label.place(relwidth=1, relheight=1, rely=0.825)

        # send button
        img1 = Image.open(img_path1)
        img2 = ImageTk.PhotoImage(img1)
        label1 = Label(image=img2)
        label1.image = img2
        send_button = Button(bottom_label, borderwidth = 0, image=img2, command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.39, rely=0.01)
        '''self.time_counter()'''

    '''def time_counter(self):
        begin = time.time()
        self._on_enter_pressed(None)
        end = time.time()

        print(f"Total time took to complete 1 function {end - begin}\n")'''

    def _on_enter_pressed(self, event):
        #self.wishme()
        response.Process_r()
        try:
            msg = tc.query
        except Exception:
            msg2 = f"Sparrow: You are not connected to the Internet\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(state=DISABLED)
        
        self._insert_msg(msg, "You")            

    def _insert_msg(self, msg, sender):
        if not msg:
            return
        
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        try:
            msg2 = f"Sparrow: {response.say}\n\n"
            self.text_widget.configure(state=NORMAL)
            self.text_widget.insert(END, msg2)
            self.text_widget.configure(state=DISABLED)
        except Exception:
            return

app = Assist_GUI()
app.run()