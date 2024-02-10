import tkinter as tk
from tkinter import messagebox
import random
class PassGen:
    # using Random class to pick the characters randomly
    # this methods picks the characters with given length and returns
    def upper(n):
        rand = random.Random()
        c = ""
        for _ in range(n):
            j = rand.randint(65, 90)
            c += chr(j)
        return c
    def lower(n):
        rand = random.Random()
        c = ""
        for _ in range(n):
            j = rand.randint(97, 122)
            c += chr(j)
        return c
    def number(n):
        rand = random.Random()
        c = ""
        for _ in range(n):
            j = rand.randint(0, 9)
            c += str(j)
        return c
    def special(n):
        rand = random.Random()
        c = ""
        spec = "#$%&()!"
        for _ in range(n):
            j = rand.randint(0, len(spec) - 1)
            c += spec[j]
        return c
    # this method shuffle the given string and returns it
    def shuffle(input_str):
        characters = list(input_str)
        random.shuffle(characters)
        return ''.join(characters)
def displaypass():
    # getting the text from textboxes and storing it
    u=upper.get("1.0", "end-1c")
    l=lower.get("1.0", "end-1c")
    n=number.get("1.0", "end-1c")
    s=special.get("1.0", "end-1c")
    try:
        # if all values are null clearing strength label and pasdisplay textbox
        if u=="" and l=="" and n=="" and s=="":
            strel.config(text="")
            pasdisplay.config(state=tk.NORMAL)
            pasdisplay.delete("1.0", tk.END)
            pasdisplay.config(state=tk.DISABLED)
            return
        # if any one value is null setting it to 0
        if u == "":
            u=0
        if l=="":
            l=0
        if n=="":
            n=0
        if s=="":
            s=0
        # calling methods in the passgen class and storing the retured string in passw variable
        passw=PassGen.upper(int(u))
        passw+=PassGen.lower(int(l))
        passw+=PassGen.number(int(n))
        passw+=PassGen.special(int(s))
        # suffling the passw string and storing in password variable
        password=PassGen.shuffle(passw)
        # deleting the previous password and writing the new password
        pasdisplay.config(state=tk.NORMAL)
        pasdisplay.delete("1.0", tk.END)
        pasdisplay.insert("1.0", password)
        pasdisplay.config(state=tk.DISABLED)
        strength=""
        # if length is easy then strength is set to easy or greater than 8 and less than 12 then strength is set to moderate else it is set to hard
        if len(password) < 8:
            strength="Easy"
        elif len(password) < 12:
            strength="Moderate"
        else:
            strength="Hard"  
        strel.config(text=f"strength-{strength}")
    # if any exception is raised in the above code it is caught here
    except Exception:
        messagebox.showinfo("Message Box", "Please provide correct values")
# creating window
root = tk.Tk()
# setting title, width and height to window
root.title("Checkbox Example")
root.geometry("360x300")
# creating labels and textbox placing in window
l1=tk.Label(text="Password Generator")
l1.pack(pady=10)
uppl = tk.Label(root, text="Uppercase")
uppl.place(x=30, y=50)
upper=tk.Text(root, width=5, height=1)
upper.place(x=90, y=50)
lowl = tk.Label(root, text="Lowercase")
lowl.place(x=30, y=80)
lower=tk.Text(root, width=5, height=1)
lower.place(x=90, y=80)
numl = tk.Label(root, text="Numbers")
numl.place(x=30, y=110)
number=tk.Text(root, width=5, height=1)
number.place(x=90, y=110)
specl = tk.Label(root, text="Special")
specl.place(x=30, y=140)
special=tk.Text(root, width=5, height=1)
special.place(x=90, y=140)
pasdisplay = tk.Text(root, width=22, height=7)
pasdisplay.place(x=160,y=50)
# creating button and placing in window, when it is clicked displaypass function is called
button = tk.Button(root, text="Generate Password", command=displaypass)
button.place(x=120, y=200)
strel=tk.Label(root)
strel.place(x=160, y=165) 
root.mainloop()
