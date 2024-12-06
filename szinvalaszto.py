from tkinter import *
import time
import random

root = Tk()
root.title("Színválasztó")
root.geometry("500x600")
root.config(bg="#2e2e2e")

szin_hatar = 10
first = True 

running = False
time_in_centiseconds = 0

def update_timer(root, display_label):
    global running, time_in_centiseconds
    if running:
        time_in_centiseconds += 1
        seconds = time_in_centiseconds // 100
        centiseconds = time_in_centiseconds % 100
        display_label.config(text=f"{seconds}.{centiseconds:02d} s")
        root.after(10, update_timer, root, display_label)

def start():
    global running, lbl_szamlalo
    if not running:
        running = True
        update_timer(root, lbl_szamlalo)

def stop():
    global running
    running = False


def reset():
    global running, time_in_centiseconds, vlb_szinek, vlb_hex, lbl_color, ent_color
    vlb_szinek = random_color()
    vlb_hex = random_color()
    lbl_color.configure(text=f"{szinek[vlb_szinek - 1]}", fg=f"{hex_kodok[vlb_hex - 1]}")
    ent_color.delete(0, END)
    running = False
    time_in_centiseconds = 0


def szin_ellenoriz(event=None):
    global szin_hatar, first
    stop()
    szin_hatar = int(clicked.get())

    if ent_color.get() == szinek[vlb_hex - 1]:
        if first:
            lbl_high.configure(text=f"Rekord: {lbl_szamlalo['text']}")
            first = False
        else:
            current_time = float(lbl_szamlalo['text'][:4])
            high_score_text = lbl_high['text'].split(":")[1].strip()
            high_score = float(high_score_text[:4])

            if current_time < high_score:
                lbl_high.configure(text=f"Rekord: {lbl_szamlalo['text']}") 

        lbl_back.configure(text="Helyes!", fg="Green")
    else:
        lbl_back.configure(text="Helytelen!", fg="Red")

    root.after(1000, reset_and_restart)



def reset_and_restart():
    reset()
    start()

def random_color():
    x = random.randint(1, szin_hatar)
    return x


szinek = ["Piros", "Kék", "Zöld", "Sárga", "Narancssárga", "Lila", "Barna", "Fekete", "Fehér", "Rózsaszín"]
hex_kodok = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Brown", "Black", "White", "Pink"]

vlb_szinek = random_color()
vlb_hex = random_color()

lbl_color = Label(root, text="Milyen színű a szöveg?", font=("Arial", 16), bg="#2e2e2e", fg="white")
lbl_color.grid(row=0, column=0, columnspan=3, pady=10, sticky="nsew")

lbl_color = Label(root, text=f"{szinek[vlb_szinek - 1]}", fg=f"{hex_kodok[vlb_hex - 1]}", font=("Arial", 40),bg="#2e2e2e")
lbl_color.grid(row=1, column=0, columnspan=3, pady=10, sticky="nsew")

ent_color = Entry(root, justify='center', font=("Arial", 16))
ent_color.grid(row=2, column=0, columnspan=3, pady=20, sticky="nsew")

lbl_szamlalo = Label(root, text="0.00 s", font=("Arial", 20), bg="#2e2e2e", fg="white")
lbl_szamlalo.grid(row=3, column=0, columnspan=3, pady=20, sticky="nsew")

lbl_high = Label(root, text="Rekord: 0.00", font=("Arial", 16), bg="#2e2e2e", fg="white")
lbl_high.grid(row=4, column=0, columnspan=3, pady=20, sticky="nsew")

lbl_back = Label(root, text=" ", font=("Arial", 16), bg="#2e2e2e", fg="black")
lbl_back.grid(row=5, column=0, columnspan=3, pady=20, sticky="nsew")

options = [
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10"
]

clicked = StringVar()
clicked.set("10")
opt_szinek = OptionMenu(root, clicked, *options)
opt_szinek.config(font=("Arial", 14), bg="#4c4c4c", fg="white")
opt_szinek.grid(row=6, column=0, columnspan=3, pady=20, sticky="nsew")

for i in range(3):
    root.grid_columnconfigure(i, weight=1, uniform="equal")
for i in range(7):
    root.grid_rowconfigure(i, weight=1, uniform="equal")

root.bind("<Return>", szin_ellenoriz)

if __name__ == "__main__":
    start()
    root.mainloop()
