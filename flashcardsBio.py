import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import json

def load_flashcards():
    with open('flashcards.json', 'r') as file:
        return json.load(file)

def save_flashcards():
    with open('flashcards.json', 'w') as file:
        json.dump(flashcards, file)

def search_flashcards(query):
    global current_flashcard
    results = [card for card in flashcards if query.lower() in card['question'].lower() or query.lower() in card['answer'].lower()]
    if results:
        current_flashcard = flashcards.index(results[0])
        update_gui()
    else:
        tk.messagebox.showinfo("Search Result", "No flashcards found for the search query.")

def create_flashcard():
    question = simpledialog.askstring("Create Flashcard", "Enter the question:")
    answer = simpledialog.askstring("Create Flashcard", "Enter the answer:")
    if question and answer:
        flashcards.append({'question': question, 'answer': answer})
        save_flashcards()
        next_flashcard()

def update_flashcard():
    new_question = simpledialog.askstring("Update Flashcard", "Update the question:", initialvalue=flashcards[current_flashcard]['question'])
    new_answer = simpledialog.askstring("Update Flashcard", "Update the answer:", initialvalue=flashcards[current_flashcard]['answer'])
    if new_question is not None:
        flashcards[current_flashcard]['question'] = new_question
    if new_answer is not None:
        flashcards[current_flashcard]['answer'] = new_answer
    save_flashcards()
    update_gui()

def delete_flashcard():
    confirmation1 = messagebox.askyesno("Delete Flashcard", "Are you sure you want to delete this flashcard?")
    if confirmation1:
        confirmation2 = messagebox.askyesno("Delete Flashcard", "Are you really, really sure?")
        if confirmation2:
            flashcards.pop(current_flashcard)
            save_flashcards()
            next_flashcard()

def next_flashcard():
    global current_flashcard
    current_flashcard = (current_flashcard + 1) % len(flashcards)
    update_gui()

def show_answer():
    answer_label.config(text=flashcards[current_flashcard]['answer'])

def update_gui():
    question_label.config(text=flashcards[current_flashcard]['question'])
    answer_label.config(text="")

flashcards = load_flashcards()
random.shuffle(flashcards)
current_flashcard = 0

root = tk.Tk()
root.title("Biology Flashcards")
root.configure(bg="lightpink")

content_frame = tk.Frame(root, bg="pink", padx=10, pady=10)
content_frame.pack(pady=20)

question_label = tk.Label(content_frame, text=flashcards[current_flashcard]['question'], wraplength=300, font=("Helvetica", 14), bg="pink", fg="black")
question_label.pack(pady=5)

answer_label = tk.Label(content_frame, text="", wraplength=300, font=("Helvetica", 14), bg="pink", fg="green")
answer_label.pack(pady=5)

update_gui()

next_button = tk.Button(root, text="Next", command=next_flashcard, font=("Helvetica", 12, "bold"), bg="hotpink", fg="black", relief="ridge")
next_button.pack(side="left")

create_button = tk.Button(root, text="Create", command=create_flashcard, font=("Helvetica", 12, "bold"), bg="hotpink", fg="black", relief="ridge")
create_button.pack(side="left")

update_button = tk.Button(root, text="Update", command=update_flashcard, font=("Helvetica", 12, "bold"), bg="hotpink", fg="black", relief="ridge")
update_button.pack(side="left")

delete_button = tk.Button(root, text="Delete", command=delete_flashcard, font=("Helvetica", 12, "bold"), bg="hotpink", fg="black", relief="ridge")
delete_button.pack(side="left")

show_answer_button = tk.Button(root, text="Show Answer", command=show_answer, font=("Helvetica", 12, "bold"), bg="hotpink", fg="black", relief="ridge")
show_answer_button.pack(side="left")

search_entry = tk.Entry(root, font=("Helvetica", 12), bg="lightpink", fg="black")
search_entry.pack(side="left")

search_button = tk.Button(root, text="Search", command=lambda: search_flashcards(search_entry.get()), font=("Helvetica", 12, "bold"), bg="hotpink", fg="black", relief="ridge")
search_button.pack(side="left")

root.mainloop()












