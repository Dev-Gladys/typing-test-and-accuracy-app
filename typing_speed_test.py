import random
import time
from tkinter import *
from tkinter import messagebox
from sentences import *

x = 0

texts = texts
word = random.randint(0, len(texts)-1)



root = Tk()
root.title("Typing Speed and Accuracy Test")
root.geometry("700x500")
root.config(padx=20, pady=20)


window = Tk()
window.title("Typing Speed and Accuracy Test")
window.geometry("1200x1000")
window.withdraw()


def game():
    global x   ## to access and use the outside variable x  inside the function declare it as global
    if x == 0:
        window.withdraw()
        x = x + 1
    window.deiconify() ## restores the window
    root.destroy()



def result():

    count=0
    answer = text_input.get("1.0","end-1c")  # this gets the text input from the first character to the end(-1c means substract the last character which is space)
    for i, c in enumerate(texts[word]):
        try:
            if answer[i] == c:
                count += 1
        except:
            pass

    print(count)
    wpm = len(answer) * 60
    wpm =wpm /(5*60)
    accuracy = int((count / len(texts[word])) * 100)
    messagebox.showinfo(f"Your WPM :{wpm} \n "
                        f"Your Accuracy:{accuracy}%")
    print(f"wpm :{wpm}")
    print(f"accuracy:{accuracy}")


def countdown(count=60):
    # change text in label
    #root.withdraw()
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        root.after(1000, countdown, count-1)

label = Label(root)
label.place(x=35, y=15)



def play_again():
    text_input.delete("1.0", "end-1c")
    display_text.config(text=random.choice(texts))
    time.sleep(100)
    countdown()


def finish():
    window.destroy()
    root.destroy()



window_frame = Frame(window, highlightbackground="#EDF6F9", highlightthickness=2, width=700,
                     height=800, bg="#E3D5CA", relief=SUNKEN)
window_frame.grid(padx=50, pady=20)

display_text= Label(window_frame , text=texts[word] ,width=80,font=("Ariel", 15, "bold"), bg="#EDF6F9",wraplength=700)
display_text.grid(row=2,columnspan=3, pady=10, padx=10)

text_input = Text(window_frame, font=("Ariel", 15), bg="#EDEDE9", height=8, width=70, fg="black", padx=30, pady=30)
text_input.grid(row=4,column=0, columnspan=2, padx=10, pady=10)


start_typing = Button(window_frame, text="Start Game", bg="#F5F0BB",font=("Ariel", 10, "bold"),command=countdown,
                      width=10, padx=10, pady=5)
start_typing.grid(row=6, column=0)

submit_button = Button(window_frame, text="Submit", bg="#FBC5C5",command=result, font=("Ariel", 10, "bold"),
                       width=5, padx=15, pady=5,
                       )
submit_button.grid(row=7, column=0)

next_text_button = Button(window_frame, text="Play Again", bg="#FBC5C5", font=("Ariel", 10, "bold"), padx=5, pady=5,
                          width=10,command=play_again)
next_text_button.grid(row=7, column=1,columnspan=1)


exit_button = Button(window_frame, text="Exit", bg="#90C8AC", font=("Ariel", 10, "bold"),
                     width=5,padx=10, pady=5, command=finish)
exit_button.grid(row=8, column=1,columnspan=1)

#timer_text=Label(, text="", font=("Ariel", 15, "bold")).grid(column=4, row=0)
label = Label(window_frame, text="00:00", font=("Ariel", 30, "bold"), bg="#EDF6F9")
label.grid(row=0,column=1,columnspan=2, pady=10, padx=10)





##MAIN WINDOW
root_frame = Frame(root,highlightbackground="#EDF6F9", highlightthickness=2, width=450,
             height=450,bg="#E3D5CA", relief=SUNKEN, padx=20, pady=20)
root_frame.pack(padx=20, pady=20)

text_label = Label(root_frame , text="Test Your Typing Speed", font=("Ariel", 30, "bold"), bg="#F0EBE3")
text_label.grid(row=0,columnspan=3, pady=50, padx=40)

start_button= Button(root_frame ,text= "Start", bg="#FBC5C5",font=("Ariel", 15, "bold"),
                     width=15,command=game).grid(row=2, column=1)



root.mainloop()


































#
# def update_timer(self, s_time) -> None:
#     current_time = time.time()
#
#     if(int(current_time - s_time) >= 0):
#         seconds += 1
#     elif seconds == 60:
#         seconds = 0
# 		minutes += 1
#
# 	min_p = '{:0>2d}'.format(int(self.minutes))
# 	sec_p = '{:0>2d}'.format(int(self.seconds))
#
# 	time_count.config(text= f'{min_p}:{sec_p}')
# 	time_count.after(1000, lambda: self.update_timer(s_time))
#
#
#
#
# def start_test():
#     while True:
#         start_time = time.time()   #the starting time
#
#         text_input = Text(frame, font=("Ariel", 15), bg="#EDEDE9", height=8, width=70, fg="black", padx=30, pady=30)
#         text_input.grid(row=4, columnspan=4, padx=10, pady=10)
#
#         end_time = time.time()
#
#
#
#     # place_holder = Message(window_frame, text=text, fg='black', bg="#EDEDE9", width=600,
#     #                        justify='center', font=("Ariel", 15))
#     # place_holder.grid(row=2, column=0, columnspan=3, padx=20, pady=10)
#     #
#
#     #
#     # global timer
#     # timer = Label(window_frame, text="00:00", fg="red", font=("Ariel", 20, "bold"))
#     # timer.grid(column=3, row=0, padx=20, pady=10)
#
#

# def exit():
#     window.destroy() # closes current page
#
#
# window = Tk()
# window.title("Typing Speed and Accuracy Test")
# window.geometry("1000x1000")
# window.config(padx=20, pady=20)
#
# frame = Frame( highlightbackground="#EDF6F9", highlightthickness=2, width=700,
#              height=500,bg="#E3D5CA", relief=SUNKEN, padx=20, pady=20)
# frame.pack(padx=20, pady=10)
#
# label = Label(frame, text="Paragraph for Test", font=("Ariel", 30, "bold"), bg="white")
# label.grid(column=1, row=0,padx=20, pady=20)
#
# #The text will be displayed very well
# place_holder = Message(frame, text=texts, fg='black', bg="#EDEDE9", width=600,
#                        justify='center', font=("Ariel", 15))
# place_holder.grid(row=2, column=0, columnspan=3, padx=20, pady=10)
#
#
#
# start_button= Button(frame,text= "Start Test", font=("Ariel", 10, "bold"), command= start_test).grid(row=5,columnspan=4,padx=10, pady=10)
#
# exit_button= Button(frame,text= "Exit", font=("Ariel", 10, "bold"),command=exit).grid(row=6,columnspan=5)
#
#
#
#
#
#
#
# window.mainloop()
#
# #previous_button = Button( window_frame, text="<<<", command=previous_text).grid(row=4,column=0)
#
# #next_button = Button( window_frame, text=">>>", command=next_text).grid(row=4,column=3)
#
# # title_label= Label(window_frame,text="History",font=("Ariel", 20, "bold"),bg="white")
# # title_label.grid(column=1, row=1,padx=20, pady=10)


#window.mainloop()