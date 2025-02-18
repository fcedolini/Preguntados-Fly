import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

# Mostrar pregunta actual y opciones


def show_question():
    # tomar la pregunta desde quiz_data
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    # mostrar buton de opciones
    choices = question["choices"]
    for i in range(4):
        # resetear botón
        choice_btns[i].config(text=choices[i], state="normal")

    # crear el campo de feedback y deshabilita los botones
    feedback_label.config(text="")
    next_btn.config(state="disabled")

# chequear la selección y dar feed


def check_answer(choice):
    # Get the current question from the quiz_data list
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    # Check if the selected choice matches the correct answer
    if selected_choice == question["answer"]:
        # Update the score and display it
        global score
        score += 1
        score_label.config(text="Puntage: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correcto!", foreground="green")
    else:
        feedback_label.config(text="Incorrecto!", foreground="red")

    # Disable all choice buttons and enable the next button
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

# Function to move to the next question


def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        # If there are more questions, show the next question
        show_question()
    else:
        # If all questions have been answered, display the final score and end the quiz
        messagebox.showinfo("Trivia Completada",
                            "Trivia Completada! Puntaje final: {}/{}".format(score, len(quiz_data)))
        root.destroy()


# Create the main window
root = tk.Tk()
root.title("Trivia App")
root.geometry("600x530")
style = Style(theme="flatly")

# Configure the font size for the question and choice buttons
style.configure("TLabel", font=("Helvetica", 20))
style.configure("TButton", font=("Helvetica", 16))

# Create the question label
qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=10
)
qs_label.pack(pady=10)

# Create the choice buttons
choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i)
    )
    button.pack(pady=5)
    choice_btns.append(button)

# Create the feedback label
feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10
)
feedback_label.pack(pady=10)

# Initialize the score
score = 0

# Create the score label
score_label = ttk.Label(
    root,
    text="Puntaje: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10
)
score_label.pack(pady=10)

# Create the next button
next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled"
)
next_btn.pack(pady=10)

# Initialize the current question index
current_question = 0

# Show the first question
show_question()

# Start the main event loop
root.mainloop()
