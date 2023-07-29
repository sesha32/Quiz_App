import tkinter as tk
from tkinter import messagebox
import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer == self.correct_answer


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.questions = []
        self.current_question = 0
        self.score = 0

        # Sample Car-related Questions
        q1 = Question("Which car manufacturer produces the Mustang?", ["Ford", "Chevrolet", "Toyota", "Honda"], 0)
        q2 = Question("What is the top speed of the Bugatti Chiron?", ["200 mph", "300 mph", "400 mph", "500 mph"], 2)
        q3 = Question("Which car brand has a logo featuring a prancing horse?", ["Ferrari", "Lamborghini", "Porsche", "Audi"], 0)

        self.questions.extend([q1, q2, q3])
        random.shuffle(self.questions)  # Randomize the order of questions

        self.label_question = tk.Label(root, text="", wraplength=600, font=("Arial", 16), fg="black", bg="lightyellow")
        self.label_question.pack(pady=20)

        self.button_options = []
        for i in range(4):
            btn = tk.Button(root, text="", command=lambda idx=i: self.check_answer(idx), font=("Arial", 14), fg="black", bg="lightblue")
            btn.pack(pady=10)
            self.button_options.append(btn)

        self.display_question()

    def display_question(self):
        if self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.label_question.config(text=question.question)
            for i, option in enumerate(question.options):
                self.button_options[i].config(text=option)
        else:
            self.show_score()

    def check_answer(self, user_answer):
        question = self.questions[self.current_question]
        if question.is_correct(user_answer):
            self.score += 1
        self.current_question += 1
        self.display_question()

    def show_score(self):
        score_window = tk.Toplevel(self.root)
        score_window.title("Quiz Score")
        score_window.geometry("400x200")
        score_label = tk.Label(score_window, text=f"Your score: {self.score}/{len(self.questions)}", font=("Arial", 18), fg="green")
        score_label.pack(pady=20)
        ok_button = tk.Button(score_window, text="OK", command=self.root.quit, font=("Arial", 14), fg="black", bg="lightgreen")
        ok_button.pack(pady=20)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Car Quiz App")
    root.geometry("800x600")  # Set the initial size of the GUI window
    root.configure(bg="lightcyan")
    app = QuizApp(root)
    root.mainloop()

