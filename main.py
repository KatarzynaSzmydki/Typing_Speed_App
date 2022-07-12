'Typing speed app'

from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter import messagebox, ttk, colorchooser
import time
import json
import random


THEME_COLOR = "#375362"
SEC = 60
with open('texts.txt') as f:
    texts = f.read()
    TEXTS = json.loads(texts)



class Typing_Speed_App:

    def __init__(self):
        self.window = Tk()
        self.window.title("Typing Speed App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.window.geometry("900x900")
        self.secs = int(time.time())
        self.secs_counter=SEC
        self.counter_start = False

        self.time_label = Label(text=f'{str(SEC)} s',font=('Aerial 17'))
        self.time_label.grid(row=0, column=1)

        self.button1 = Button(text='Start', command=self.countdown_time,font=('Aerial 15'), bg='crimson',fg='white')
        self.button1.grid(row=2, column=1)

        self.text_index = random.randint(0,len(TEXTS)-1)
        # TEXTS[str(self.text_index)]['title']
        self.text_label_title = Label(text='Hit Start button and type below text' , font='Aerial 15 bold',bg=THEME_COLOR,fg='white')
        self.text_label_title.grid(row=4, column=0)

        self.text_body = Text(width = 90)
        self.text_body.grid(row=6, column=0, columnspan=5)
        self.text_body.insert(END, TEXTS[str(self.text_index)]['body'])

        self.written_text_label = Label(text="Your written text", font='Aerial 15 bold',bg=THEME_COLOR,fg='white')
        self.written_text_label.grid(row=8, column=0)

        # self.written_text_body = Text(width = 90)
        # self.written_text_body.insert(END, TEXTS[str(self.text_index)]['body'])

        self.entry_text = StringVar()
        self.written_text_body = Entry(textvariable=self.entry_text, width=120)
        self.written_text_body.grid(row=10, column=0, columnspan=5)

        self.written_text_words = Label(font='Aerial 15 bold',bg=THEME_COLOR,fg='yellow')
        self.written_text_words_lbl = Label(text='Written words: ',font='Aerial 12',bg=THEME_COLOR,fg='yellow')
        self.completeness_pct = Label(font='Aerial 15 bold',bg=THEME_COLOR,fg='yellow')
        self.completeness_pct_lbl = Label(text='% Text: ',font='Aerial 12',bg=THEME_COLOR,fg='yellow')
        self.words_per_minute = Label(font='Aerial 15 bold',bg=THEME_COLOR,fg='yellow')
        self.words_per_minute_lbl = Label(text='Words/min: ', font='Aerial 12', bg=THEME_COLOR, fg='yellow')

        self.written_text_words_lbl.grid(row=3, column=0)
        self.written_text_words.grid(row=3, column=1)
        self.words_per_minute_lbl.grid(row=3, column=2)
        self.words_per_minute.grid(row=3, column=3)
        self.completeness_pct_lbl.grid(row=3, column=4)
        self.completeness_pct.grid(row=3, column=5)

        self.countdown()


    def everysecond(self):
        self.secs_counter -= 1
        if self.secs_counter > 10:
            self.time_label.configure(text=f'{str(self.secs_counter)} s')
        else:
            self.time_label.configure(text=f'{str(self.secs_counter)} s', fg='white', bg='crimson',font=('Aerial 19 bold'))

        # Put here the code to reduce the tkinter counter by one.
        # For example, modify the label.

    def countdown(self):
        while True:
            self.window.update()
            self.window.update_idletasks()

            if int(time.time()) > self.secs:
                self.secs = int(time.time())
                if self.counter_start:
                    if self.secs_counter > 0:
                        self.everysecond()
                    if self.secs_counter == 0:
                        self.written_text_body.configure(state='disable')
                        self.calc_results()


    def countdown_time(self):
        self.counter_start = True
        self.secs_counter = SEC


    def calc_results(self):
        text = TEXTS[str(self.text_index)]['body']
        written_text = self.written_text_body.get()
        written_text_words = len(written_text.split(' '))
        provided_text_words = len(text.split(' '))
        completeness_pct = written_text_words/provided_text_words*100
        words_per_minute = written_text_words*(60/SEC)

        self.written_text_words.configure(text=str("{:.0f}".format(written_text_words)))
        self.completeness_pct.configure(text=f'{str("{:.0f}".format(completeness_pct))}%' )
        self.words_per_minute.configure(text=str("{:.0f}".format(words_per_minute)))


app = Typing_Speed_App()