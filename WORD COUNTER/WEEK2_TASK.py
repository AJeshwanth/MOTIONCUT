import tkinter as tk
from tkinter import messagebox
def wordcount():
    entered_text = output.get("1.0", "end-1c")
    words = entered_text.split()
    word_count = len(words)
    if word_count == 0:
        messagebox.showinfo("Word Count", "Please Provide Sentence")
    else:
        messagebox.showinfo("Word Count", f"Number of words: {word_count}")
window=tk.Tk()
window.title("Count Characters")
window.geometry("300x250")
button=tk.Button(window,text="Count words",command=wordcount)
label2=tk.Label(window,text="Couting Words")
word_count_label=tk.Label(window)
output=tk.Text(window,width=30,height=8,font=("Helvetica",10),wrap="word")
label2.pack(pady=15)
output.pack(pady=10)
button.pack()
window.mainloop()