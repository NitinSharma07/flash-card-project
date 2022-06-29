from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

#########Reading Datafile######
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    data_dict = data.to_dict(orient='records')



#
def word_change():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    new_word = current_card['French']
    canvas.itemconfig(Title_text, text='French', fill='Black')
    canvas.itemconfig(Word_text, text=new_word, fill='black')
    canvas.itemconfig(canvas_image, image=Front_image)
    flip_timer = window.after(3000, func=flip_card)


#
#
# ##############Flipping the cards#########

def flip_card():
    canvas.itemconfig(Title_text, text='English', fill='white')
    canvas.itemconfig(Word_text, text=current_card['English'], fill='white')
    canvas.itemconfig(canvas_image, image=back_image)

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv('data/words_to_learn.csv', Index = False)


    word_change()



####################### UI setup############

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

back_image = PhotoImage(file='images/card_back.png')
Front_image = PhotoImage(file='images/card_front.png')
canvas = Canvas(width=800, height=526)
canvas_image = canvas.create_image(400, 263, image=Front_image)
Title_text = canvas.create_text(400, 150, text='', font=('Arial', 48, 'italic'))
Word_text = canvas.create_text(400, 250, text='', font=('Arial', 65, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = PhotoImage(file='images/wrong.png')
button = Button(image=wrong_button, highlightthickness=0, command=word_change)
button.grid(row=1, column=0)
right_button = PhotoImage(file='images/right.png')
button2 = Button(image=right_button, highlightthickness=0, command=is_known)
button2.grid(row=1, column=1)

word_change()

window.mainloop()
