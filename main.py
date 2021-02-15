# Using Tkinter and what you have learnt about building GUI applications with Python, build a desktop app that assesses your typing speed. Give the user some sample text and detect how many words they can type per minute.

# The average typing speed is 40 words per minute. But with practice, you can speed up to 100 words per minute.


# You can try out a web version here:

# https: // typing-speed-test.aoeu.eu/


# If you have more time, you can build your typing speed test into a typing trainer, with high scores and more text samples. You can design your program any way you want.
import tkinter as tk
from tkinter import *
from datetime import datetime, timedelta


FONT1 = "Helvetica"
MIDNIGHTBLUE = "#191970"

with open("small-text.txt", 'r') as test_text_file:
    test_text = test_text_file.read()
        
with open("small-text.txt", 'r') as test_text_filezz:
    text_lines = test_text_filezz.readlines()

words_in_test_text = []
test_text_lines = test_text.split("\n")
for line in test_text_lines:
    temp_words = line.split(" ")
    for word in temp_words:
        if word != " " and word != "":
            words_in_test_text.append(word)

# print(words_in_test_text)

test_started = False


class Timer:
    def __init__(self, parent):
        # variable storing time
        self.seconds = 0
        # label displaying time
        self.label = tk.Label(parent, text="0 s",
                              font=("Arial 30"), width=10, bg='#d3e0fa', fg='green')
        self.label.place(relx=0.8, rely=0.04, relwidth=0.2, relheight=0.1)
        # start the timer

        self.label.after(1000, self.refresh_label)

    def refresh_label(self):
        """ refresh the content of the label every second """
        # increment the time
        self.seconds += 1
        # display the new time
        if self.seconds < 11:
            self.label.configure(text="%i s" % self.seconds)
        # request tkinter to call self.refresh after 1s (the delay is given in ms)
            self.label.after(1000, self.refresh_label)
        if self.seconds == 10:
            self.label.configure(fg='red')
            text.configure(state='disabled')
            window_popup()
        
def window_popup():
    global test_text
    global words_in_test_text
    mistakes_counter = 0

    def start_again():
        global test_started
        test_started = False
        text.configure(state='normal')
        text.delete("1.0", "end")
        print('deleted!!!')
        popup_window.destroy()
        timer.label.destroy()

    user_text = text.get("1.0", "end")
    user_text_lines = user_text.split("\n")
    user_text_words = []
    user_text_chars = []

    #counting amount of words and characters in user-entered text omitting spaces and new line chars
    for line in user_text_lines:
        line_s = line.split(" ")
        for word in line_s:
            if word != " " and word != "":
                user_text_words.append(word)
            for char in word:
                if char != " " and char != "":
                    user_text_chars.append(char)
    
    # print(user_text_words)

    print(f'WPM: {len(user_text_words)}')
    print(f'CPM: {len(user_text_chars)}')
    
    #In order to find mistakes we need to compare only a portion of the test text against
    #User's input (only those words that user was able to type during 60s time frame)
    #Therefore we define test_text_part to be only the same amount of words that user typed.

    test_text_part = words_in_test_text[:len(user_text_words)]

    #The nested for loops below compare word-with-word. So if the test word was 5 chars and user entered 4 chars, only the first 4 will be compared
    for i in range(0, len(user_text_words)):
        mistakes_counter += abs(len(user_text_words[i])-len(test_text_part[i])) #accounting for mistakes when user types more/less characters for a corresponding word in the test text.
        for char_t, char_u in zip(test_text_part[i], user_text_words[i]):
            if char_t != char_u:
                mistakes_counter += 1
    
    print(f'MISTAKES: {mistakes_counter}')
        
    # print(test_text_part)

    user_text += f'WPM: {len(user_text_words)} |' + f' CPM: {len(user_text_chars)} |' + f' MISTAKES: {mistakes_counter}'
    popup_window = Tk()
    popup_window.title("typingTest results")
    popup_window.minsize(width=700, height=200)
    popup_window.config(bg='#d3e0fa')
    popup_ok_btn = Button(popup_window, text="Start Again",
                command=start_again, width=12, bg=MIDNIGHTBLUE, fg='white')
    popup_ok_btn.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.1)
    
    popup_result_text = Label(popup_window, text=user_text, justify='left', font=(
        FONT1, 10, "bold"))
    popup_result_text.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.6)

    




def onKeyPress(event):
    global start
    global test_started
    global timer
    if test_started == False:
        test_started = True
        timer = Timer(frame)

window = Tk()
window.title("typingTest.by_Greg")
window.minsize(width=700, height=750)
window.config(bg='white')

frame = Frame(window, bg='#d3e0fa', bd=0.03)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


title_label = Label(frame, text="typingTest.by_Greg", font=(
    FONT1, 30, "bold"), fg=MIDNIGHTBLUE, bg='white')
title_label.place(relx=0, rely=0.04, relwidth=0.8, relheight=0.1)

printed_text = Label(frame, text=test_text, justify='left', font=(
    FONT1, 10, "bold"))
printed_text.place(
    relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

text = Text(frame, background='#2F5B9F', foreground='white',
               font=('Arial', 12), insertbackground='white')
text.place(relx=0.1, rely=0.82, relwidth=0.8, relheight=0.1)
text.focus()
text.bind('<KeyPress>', onKeyPress)

# timer = Timer(frame)

window.mainloop()
