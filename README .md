
# Autocorrect Model with Python

📖 About:

The Autocorrect Model is a Natural Language Processing (NLP) based project that corrects misspelled words by suggesting the closest matching words from a vocabulary.
This project uses similarity metrics and word frequency to generate accurate corrections and includes an interactive Tkinter GUI for user-friendly spell checking.

It works similarly to the autocorrect systems used in smartphone keyboards and search bars.

✨Key Highlights:

•Built with Python, NLP, and textdistance

•Uses text from a book to create vocabulary and frequency tables

•Suggests the top closest words for each misspelling

•Includes a clean Black & White GUI (Tkinter)

•Lightweight, fast, and easy to extend

•Works fully offline

🔍How It Works:

•The autocorrect system follows these steps:

•Reads a large text file (book.txt)

•Extracts all words and builds a vocabulary

•Calculates frequency of each word

•Uses Jaccard similarity (Q-grams) to find closest matches

•Sorts suggestions based on similarity + frequency

•Displays top 5 corrected words in the GUI

•If the entered word already exists in the vocabulary, it is marked as correct.

💡Features:

📌Core Autocorrect Engine:

•Vocabulary creation using regex

•Word frequency using Python Counter

•Similarity calculation using Jaccard distance

•Clean top-word suggestions (without probability/similarity in output)

📌GUI Application

•User-friendly Tkinter interface

•Minimal black-and-white theme

•Input box for typing words

•“Check Spelling” button

•Suggestions displayed in a listbox

•Handles empty input gracefully

📌No External APIs Required

•Everything runs locally using pure Python.


## Tech Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming language |
| Pandas       | Data handling             |
| NumPy        | Numerical operations      |
| textdistance | Similarity calculations   |
| Regex (re)   | Word extraction           |
| Counter      | Word frequency table      |
| Tkinter      | GUI development           |


## Project Structure

```
Autocorrect-Model/
├── autocorrect_gui.py      # GUI version
├── autocorrect_core.py     # Core logic (if separated)
├── book.txt                # Vocabulary source text
├── README.md               # Documentation
└── requirements.txt        # Required dependencies

```

## Installation

1.Clone the Repository

```bash
git clone https://github.com/ayushx07-web/AutoCorrect-Model.git
cd AutoCorrect-Model


```

2.Install Dependencies

```bash
  pip install textdistance pandas numpy


```

3.Run The Script

```bash
 python script.py

```

🖥️Interactive Usage:

Type any word in the input box

Click Check Spelling

The GUI shows the top suggestions

If the word is correct, the app informs you directly











## Acknowledgements:

•Python community

•textdistance library

•Tkinter for GUI

•NLP concepts used for building autocorrect

•Open-source datasets used for vocabulary
## Contact

Ayush

•GitHub: @ayushx07-web

•Project Link: https://github.com/ayushx07-web/AutoCorrect-Model