import tkinter as tk
import random
import time

# Function to start the typing test
def start_test():
    global start_time
    global current_text
    start_time = time.time()
    current_text = random_text()
    text_label.config(text=current_text)
    input_entry.delete(0, tk.END)
    input_entry.focus_set()
    start_button.config(state=tk.DISABLED)

# Function to calculate typing speed
def calculate_speed():
    end_time = time.time()
    total_time = end_time - start_time
    typed_text = input_entry.get()
    words_typed = len(typed_text.split())
    typing_speed = words_typed / (total_time / 60)  # Words per minute
    result_label.config(text=f"Typing speed: {typing_speed:.2f} WPM")
    start_button.config(state=tk.NORMAL)

# Function to generate random text for typing test
def random_text():
    texts = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a versatile programming language.",
        "Coding is fun and challenging.",
        "Hello, World! This is a typing test.",
        "OpenAI's GPT-3.5 is an amazing language model.",
    ]
    return random.choice(texts)

# Create the main window
root = tk.Tk()
root.title("Typing Speed Test")

# Create and configure widgets
text_label = tk.Label(root, text="", font=("Arial", 14))
text_label.pack(pady=20)

input_entry = tk.Entry(root, font=("Arial", 12))
input_entry.pack()

start_button = tk.Button(root, text="Start Test", command=start_test, font=("Arial", 12))
start_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

check_button = tk.Button(root, text="Check Speed", command=calculate_speed, font=("Arial", 12))
check_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
