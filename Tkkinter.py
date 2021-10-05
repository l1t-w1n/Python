from tkinter import *
from webbrowser import open
def go():
    adresse=entre.get()
    open(adresse)
window=Tk()
window.title("Ma première application")
window.geometry("400x300")
window.minsize(300,200)
window.config(bg="#00CC00")
interieur=Frame(bg="#00CC00")
message=Label(interieur, text="Entrez une URL", fg="white", bg="#00CC00", font=
('Helvetica', '20', 'bold italic'))
message.pack(side=TOP, pady=20)
entre=Entry(interieur, bg="white", fg="#00CC00", font= ('Helvetica', '16'))
entre.pack(fill=X, pady=20)
lance=Button(interieur, text="Go !!!!", bg="white", fg="#00CC00", relief=FLAT)
lance.pack(pady=20)
lance['command']=go
interieur.pack(expand=YES, fill=X)
window.mainloop()