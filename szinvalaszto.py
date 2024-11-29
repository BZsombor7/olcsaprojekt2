from tkinter import *
import time
import random

# Initialize the main window
root = Tk()
root.title("Színválasztó")
root.geometry("500x600")  # Set a larger window size
root.config(bg="#2e2e2e")  # Set background color to dark gray

szin_hatar = 10
first = True  # Change to True so the first time it will update the record

running = False
time_in_centiseconds = 0

# Update timer function
def update_timer(root, display_label):
    global running, time_in_centiseconds
    if running:
        time_in_centiseconds += 1
        seconds = time_in_centiseconds // 100
        centiseconds = time_in_centiseconds % 100
        display_label.config(text=f"{seconds}.{centiseconds:02d} s")
        root.after(10, update_timer, root, display_label)


# Start the timer
def start():
    global running, lbl_szamlalo
    if not running:
        running = True
        update_timer(root, lbl_szamlalo)


# Stop the timer
def stop():
    global running
    running = False


# Reset the game
def reset():
    global running, time_in_centiseconds, vlb_szinek, vlb_hex, lbl_color, ent_color
    vlb_szinek = random_color()
    vlb_hex = random_color()
    lbl_color.configure(text=f"{szinek[vlb_szinek - 1]}", fg=f"{hex_kodok[vlb_hex - 1]}")
    ent_color.delete(0, END)
    running = False
    time_in_centiseconds = 0


# Function to check if the color is correct
def szin_ellenoriz(event=None):
    global szin_hatar, first
    stop()
    szin_hatar = int(clicked.get())

    if ent_color.get() == szinek[vlb_hex - 1]:
        if first:  # If it's the first correct answer
            # Set record with the current time
            lbl_high.configure(text=f"Rekord: {lbl_szamlalo['text']}")
            first = False  # Prevent it from running again
        else:
            # Compare current time with the high score (not the first time)
            current_time = float(lbl_szamlalo['text'][:4])  # Get the current time in seconds
            high_score_text = lbl_high['text'].split(":")[1].strip()  # Extract high score from the label text
            high_score = float(high_score_text[:4])  # Convert the high score to float

            # If the current time is better (lesser) than the high score, update the record
            if current_time < high_score:
                lbl_high.configure(text=f"Rekord: {lbl_szamlalo['text']}")  # Update record

        lbl_back.configure(text="Helyes!", fg="Green")
    else:
        lbl_back.configure(text="Helytelen!", fg="Red")

    root.after(1000, reset_and_restart)


# Reset and restart the game
def reset_and_restart():
    reset()
    start()


# Generate random color index
def random_color():
    x = random.randint(1, szin_hatar)
    return x


# List of colors and hex codes
szinek = ["Piros", "Kék", "Zöld", "Sárga", "Narancssárga", "Lila", "Barna", "Fekete", "Fehér", "Rózsaszín"]
hex_kodok = ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Brown", "Black", "White", "Pink"]

# Initial random colors
vlb_szinek = random_color()
vlb_hex = random_color()

# Labels and entry widgets
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

# Dropdown menu for color difficulty
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

# Make all columns and rows expand to fit the window
for i in range(3):
    root.grid_columnconfigure(i, weight=1, uniform="equal")
for i in range(7):  # Reduced rows to 7 to match new layout
    root.grid_rowconfigure(i, weight=1, uniform="equal")

# Bind the Enter key to check the color
root.bind("<Return>", szin_ellenoriz)

# Start the game
if __name__ == "__main__":
    start()
    root.mainloop()
