#QUIZ GAME
import random
import tkinter as tk
from tkinter import messagebox

class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.questions = [
            {
                'question': 'What is the capital of France?',
                'choices': ['London', 'Berlin', 'Paris', 'Madrid'],
                'answer': 'Paris'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'choices': ['Earth', 'Mars', 'Venus', 'Jupiter'],
                'answer': 'Mars'
            },
            # Add more questions in the same format
        ]
        self.score = 0
        self.current_question_idx = 0

        self.label = tk.Label(root, text="Welcome to the Quiz Game!", font=("Helvetica", 16, "bold"), fg="darkblue")
        self.label.pack(pady=20)

        self.question_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.question_label.pack()

        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Helvetica", 10), command=lambda idx=i: self.check_answer(idx))
            self.choice_buttons.append(button)
            button.pack(pady=5)

        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 10))
        self.feedback_label.pack()

        self.next_button = tk.Button(root, text="Next Question", font=("Helvetica", 10), command=self.next_question, bg="green", fg="white")
        self.next_button.pack(pady=10)
        self.next_button["state"] = "disabled"

        if self.questions:
            self.load_question(0)

    def load_question(self, idx):
        self.current_question_idx = idx
        question = self.questions[idx]
        self.question_label.config(text=question['question'])

        for i, choice in enumerate(question['choices']):
            self.choice_buttons[i].config(text=choice, bg="lightblue")

        self.next_button["state"] = "disabled"

    def check_answer(self, choice_idx):
        question = self.questions[self.current_question_idx]
        selected_choice = question['choices'][choice_idx]
        correct_answer = question['answer']

        if selected_choice == correct_answer:
            self.score += 1
            self.show_feedback("Correct!", "green")
        else:
            self.show_feedback(f"Incorrect. The correct answer is: {correct_answer}", "red")

    def show_feedback(self, message, color):
        self.feedback_label.config(text=message, fg=color)
        self.next_button["state"] = "normal"

    def next_question(self):
        if self.current_question_idx < len(self.questions) - 1:
            self.load_question(self.current_question_idx + 1)
        else:
            self.display_final_results()

    def display_final_results(self):
        final_message = f"Quiz completed! Your score: {self.score}/{len(self.questions)}"
        messagebox.showinfo("Quiz Results", final_message)

    # ... (rest of the methods remain the same)

def main():
    root = tk.Tk()
    root.configure(bg="white")
    app = QuizGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
