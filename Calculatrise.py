from tkinter import *
from tkinter.font import Font

def clique(event):
    v = event.widget['text']
    if v == "E":
        expression["text"] = ""
        resultat["text"] = "0"
    else:
        expression["text"] += v

def calcule():
    try:
        v = eval(expression["text"])
    except (SyntaxError, ZeroDivisionError):
        v = "Erreur"
    resultat["text"] = str(v)

window = Tk()
window.title("Super Calculatrice")
window.geometry("280x280")
window.minsize(280, 300)

police = Font(family='Baskerville', size=16, weight='normal', slant='italic')

expression = Label(window, text="", fg="black", bd=1, font=police)
expression.grid(row=0, column=0, columnspan=5, sticky=NSEW)
resultat = Label(window, text="0", bg="white", fg="red", bd=1, font=police)
resultat.grid(row=1, column=0, columnspan=5, sticky=NSEW)

symboles = "+-*/E0123456789()"
bouton = []
r, c = 2, 0
for i, e in enumerate(symboles):
    bouton.append(Button(window, text=e))
    bouton[-1].bind("<Button-1>", clique)
    # bouton[-1].config(height=2, width=2)
    bouton[-1].grid(row=r, column=c, sticky=NSEW)
    c = c + 1
    if c == 5:
        c = 0
        r = r + 1

egal = Button(window, text="=", command=calcule)
egal.grid(row=5, column=2, columnspan=3, sticky=NSEW)

for i in range(5):
    Grid.columnconfigure(window, index=i, weight=1)
for i in range(6):
    Grid.rowconfigure(window, index=i, weight=1)

window.mainloop()