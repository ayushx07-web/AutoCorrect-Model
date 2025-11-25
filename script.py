import pandas as pd
import numpy as np
import textdistance
import re
from collections import Counter
import tkinter as tk
from tkinter import messagebox, ttk

# ---------------------- Load and Process File ----------------------

words = []

with open('book.txt', 'r', encoding='utf-8', errors='ignore') as f:
    file_name_data = f.read().lower()
    words = re.findall(r'\w+', file_name_data)

V = set(words)
word_freq_dict = Counter(words)

probs = {}
Total = sum(word_freq_dict.values())
for k in word_freq_dict.keys():
    probs[k] = word_freq_dict[k] / Total


# ---------------------- Autocorrect Function -----------------------

def my_autocorrect(input_word):
    input_word = input_word.lower()

    if input_word in V:
        return ['Your word seems to be correct']

    similarities = [
        1 - (textdistance.Jaccard(qval=2).distance(v, input_word))
        for v in word_freq_dict.keys()
    ]

    df = pd.DataFrame.from_dict(probs, orient='index').reset_index()
    df = df.rename(columns={'index': 'Word', 0: 'Prob'})
    df['Similarity'] = similarities

    top_words = df.sort_values(
        ['Similarity', 'Prob'],
        ascending=False
    ).head()['Word'].tolist()

    return top_words


# ---------------------------- GUI --------------------------------

def check_word():
    word = entry.get().strip()
    if word == "":
        messagebox.showwarning("Warning", "Please enter a word!")
        return

    suggestions = my_autocorrect(word)
    listbox.delete(0, tk.END)

    for s in suggestions:
        listbox.insert(tk.END, s)


# Main Window
root = tk.Tk()
root.title("Autocorrect Tool")
root.geometry("480x420")
root.config(bg="#FFFFFF")   # pure white background

# Title Label
title = tk.Label(
    root,
    text="Autocorrect Application",
    font=("Helvetica", 20, "bold"),
    bg="#FFFFFF",
    fg="#000000"   # pure black
)
title.pack(pady=20)

# Input Frame
frame = tk.Frame(root, bg="#FFFFFF")
frame.pack(pady=10)

label = tk.Label(
    frame,
    text="Enter a word:",
    font=("Arial", 13),
    bg="#FFFFFF",
    fg="#000000"
)
label.grid(row=0, column=0, padx=10)

entry = tk.Entry(
    frame,
    font=("Arial", 14),
    width=22,
    bg="#FFFFFF",
    fg="#000000",
    relief="solid",
    bd=1
)
entry.grid(row=0, column=1, padx=10)

# Pure black button
btn = tk.Button(
    root,
    text="Check Spelling",
    font=("Arial", 14, "bold"),
    command=check_word,
    bg="#000000",
    fg="#FFFFFF",
    activebackground="#333333",
    width=20,
    relief="raised",
    bd=3
)
btn.pack(pady=15)

# Suggestions Label
listbox_label = tk.Label(
    root,
    text="Suggestions:",
    font=("Arial", 15, "bold"),
    bg="#FFFFFF",
    fg="#000000"
)
listbox_label.pack(pady=5)

# Suggestions Listbox
listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    width=32,
    height=8,
    bg="#FFFFFF",
    fg="#000000",
    relief="solid",
    bd=1
)
listbox.pack(pady=10)

root.mainloop()
