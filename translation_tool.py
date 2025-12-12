import tkinter as tk
from deep_translator import GoogleTranslator
import pyttsx3  # For text-to-speech
import pyperclip  # For copy to clipboard

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to translate text
def translate_text():
    src_lang = src_lang_var.get()
    dest_lang = dest_lang_var.get()
    text = text_entry.get("1.0", tk.END).strip()
    if text == "":
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "Please enter some text.")
        return
    try:
        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, translated)
    except Exception as e:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"Error: {e}")

# Function to copy translated text
def copy_text():
    pyperclip.copy(result_text.get("1.0", tk.END))

# Function to speak translated text
def speak_text():
    text = result_text.get("1.0", tk.END)
    engine.say(text)
    engine.runAndWait()

# GUI Setup
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("500x400")

# Input Text
tk.Label(root, text="Enter Text:").pack()
text_entry = tk.Text(root, height=5)
text_entry.pack(pady=5)

# Source Language
tk.Label(root, text="Source Language (e.g., en):").pack()
src_lang_var = tk.StringVar()
tk.Entry(root, textvariable=src_lang_var).pack(pady=5)

# Target Language
tk.Label(root, text="Target Language (e.g., es):").pack()
dest_lang_var = tk.StringVar()
tk.Entry(root, textvariable=dest_lang_var).pack(pady=5)

# Buttons
tk.Button(root, text="Translate", command=translate_text, bg="lightblue").pack(pady=5)
tk.Button(root, text="Copy Translated Text", command=copy_text, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Speak Translated Text", command=speak_text, bg="lightyellow").pack(pady=5)

# Output Text
tk.Label(root, text="Translated Text:").pack()
result_text = tk.Text(root, height=5)
result_text.pack(pady=5)

root.mainloop()
