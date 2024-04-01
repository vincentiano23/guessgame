import random
import tkinter as tk
from tkinter import messagebox
import os

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Vocabulary Builder")
        self.geometry("400x600")  # Set window size

        # Check if the user_credentials.txt file exists, if not, create an empty file
        if not os.path.exists("user_credentials.txt"):
            open("user_credentials.txt", "w").close()

        # Load existing user credentials from the storage file
        self.users = {}
        with open("user_credentials.txt", "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                self.users[username] = password

        self.create_login_page()

    def create_login_page(self):
        self.login_page = tk.Frame(self)
        self.login_page.pack(padx=10, pady=5)

        username_label = tk.Label(self.login_page, text="Username:")
        username_label.grid(row=0, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.login_page)
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = tk.Label(self.login_page, text="Password:")
        password_label.grid(row=1, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.login_page, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        login_button = tk.Button(self.login_page, text="Login", command=self.login)
        login_button.grid(row=2, columnspan=2, padx=10, pady=5)

        register_label = tk.Label(self.login_page, text="Don't have an account? Register an account.", fg="blue", cursor="hand2")
        register_label.grid(row=3, columnspan=2, padx=10, pady=5)
        register_label.bind("<Button-1>", lambda event: self.open_signup_page())

    def open_signup_page(self):
        self.signup_page = tk.Frame(self)
        self.signup_page.pack(padx=10, pady=5)

        reg_username_label = tk.Label(self.signup_page, text="New Username:")
        reg_username_label.grid(row=0, column=0, padx=10, pady=5)
        self.reg_username_entry = tk.Entry(self.signup_page)
        self.reg_username_entry.grid(row=0, column=1, padx=10, pady=5)

        reg_password_label = tk.Label(self.signup_page, text="New Password:")
        reg_password_label.grid(row=1, column=0, padx=10, pady=5)
        self.reg_password_entry = tk.Entry(self.signup_page, show="*")
        self.reg_password_entry.grid(row=1, column=1, padx=10, pady=5)

        register_button = tk.Button(self.signup_page, text="Register", command=self.register)
        register_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the entered username and password match the stored credentials
        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login", "Login successful")
            self.create_home_page()
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def register(self):
        new_username = self.reg_username_entry.get()
        new_password = self.reg_password_entry.get()

        # Check if the username is already taken
        if new_username in self.users:
            messagebox.showerror("Signup Error", "Username already exists. Please choose another one.")
        else:
            # Add the new user to the dictionary and update the storage file
            self.users[new_username] = new_password
            with open("user_credentials.txt", "a") as file:
                file.write(f"{new_username}:{new_password}\n")
            messagebox.showinfo("Signup Success", "Registration successful. You can now log in.")
            self.create_login_page()

    def create_home_page(self):
        self.login_page.pack_forget()

        self.home_page = tk.Frame(self)
        self.home_page.pack(padx=10, pady=5)

        welcome_label = tk.Label(self.home_page, text="Welcome to Vocabulary Builder!")
        welcome_label.pack(padx=10, pady=5)

        # Add buttons for different functionalities
        word_games_button = tk.Button(self.home_page, text="Word Games", command=self.open_word_games_page)
        word_games_button.pack(padx=10, pady=5)

        quizzes_button = tk.Button(self.home_page, text="Quizzes", command=self.open_quizzes_page)
        quizzes_button.pack(padx=10, pady=5)

        word_repository_button = tk.Button(self.home_page, text="Word Repository", command=self.open_word_repository_page)
        word_repository_button.pack(padx=10, pady=5)

    def open_word_games_page(self):
        self.home_page.pack_forget()

        self.word_games_page = tk.Frame(self)
        self.word_games_page.pack(padx=10, pady=5)

        # Add "Add Words" button
        add_words_button = tk.Button(self.word_games_page, text="Add Words", command=self.open_add_words_page)
        add_words_button.pack(padx=10, pady=5)

        # Add "Guess Individual Words" button
        guess_words_button = tk.Button(self.word_games_page, text="Guess Individual Words", command=self.open_guess_words_page)
        guess_words_button.pack(padx=10, pady=5)

        # Add "Match Words with Definitions" button
        match_words_button = tk.Button(self.word_games_page, text="Match Words with Definitions", command=self.open_match_words_page)
        match_words_button.pack(padx=10, pady=5)

    def open_add_words_page(self):
        add_words_page = tk.Toplevel(self)
        add_words_page.title("Add Words")
        add_words_page.geometry("300x200")

        word_label = tk.Label(add_words_page, text="Word:")
        word_label.grid(row=0, column=0, padx=10, pady=5)
        word_entry = tk.Entry(add_words_page)
        word_entry.grid(row=0, column=1, padx=10, pady=5)

        def save_word():
            word = word_entry.get()
            if word:
                with open("add_words.txt", "a") as file:
                    file.write(word + "\n")
                messagebox.showinfo("Word Saved", "Word added successfully.")
                word_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a word.")

        save_button = tk.Button(add_words_page, text="Save", command=save_word)
        save_button.grid(row=1, columnspan=2, padx=10, pady=5)

    def open_guess_words_page(self):
        guess_words_page = tk.Toplevel(self)
        guess_words_page.title("Guess Individual Words")
        guess_words_page.geometry("400x300")

        # Initialize the WordGuessGame instance
        game = WordGuessGame(guess_words_page, "add_words.txt")

    def open_quizzes_page(self):
        self.home_page.pack_forget()

        self.quizzes_page = tk.Frame(self)
        self.quizzes_page.pack(padx=10, pady=5)

        # Add quizzes functionality here

        back_button = tk.Button(self.quizzes_page, text="Back", command=lambda: [self.quizzes_page.destroy(), self.create_home_page()])
        back_button.pack(padx=10, pady=5)

    def open_word_repository_page(self):
        self.home_page.pack_forget()

        self.word_repository_page = tk.Frame(self)
        self.word_repository_page.pack(padx=10, pady=5)

        add_word_button = tk.Button(self.word_repository_page, text="Add Word", command=self.open_add_word_page)
        add_word_button.pack(padx=10, pady=5)

        # Add categories buttons
        categories = ["Maths", "Science", "History", "Art", "Computer Science"]
        for category in categories:
            category_button = tk.Button(self.word_repository_page, text=category, command=lambda c=category: self.open_word_definition_page(c))
            category_button.pack(padx=10, pady=5)

    def open_add_word_page(self):
        add_word_page = tk.Toplevel(self)
        add_word_page.title("Add Word")
        add_word_page.geometry("300x200")

        word_label = tk.Label(add_word_page, text="Word:")
        word_label.grid(row=0, column=0, padx=10, pady=5)
        word_entry = tk.Entry(add_word_page)
        word_entry.grid(row=0, column=1, padx=10, pady=5)

        definition_label = tk.Label(add_word_page, text="Definition:")
        definition_label.grid(row=1, column=0, padx=10, pady=5)
        definition_entry = tk.Entry(add_word_page)
        definition_entry.grid(row=1, column=1, padx=10, pady=5)

        save_button = tk.Button(add_word_page, text="Save", command=lambda: self.save_word(word_entry.get(), definition_entry.get()))
        save_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def save_word(self, word, definition):
        with open("word_repository.txt", "a") as file:
            file.write(f"{word}:{definition}\n")
        messagebox.showinfo("Word Saved", "Word and definition saved successfully.")

    def open_word_definition_page(self, category):
        word_definition_page = tk.Toplevel(self)
        word_definition_page.title(f"{category} Words")
        word_definition_page.geometry("400x300")

        # Add functionality to display words and definitions for the selected category
        # You can retrieve the words and definitions from the repository text file
        # Display them in a list or any suitable widget

        add_word_button = tk.Button(word_definition_page, text="Add Word", command=lambda: self.open_add_word_page_in_category(word_definition_page, category))
        add_word_button.pack(padx=10, pady=5)

    def open_add_word_page_in_category(self, parent_window, category):
        add_word_page = tk.Toplevel(parent_window)
        add_word_page.title("Add Word")
        add_word_page.geometry("300x200")

        word_label = tk.Label(add_word_page, text="Word:")
        word_label.grid(row=0, column=0, padx=10, pady=5)
        word_entry = tk.Entry(add_word_page)
        word_entry.grid(row=0, column=1, padx=10, pady=5)

        definition_label = tk.Label(add_word_page, text="Definition:")
        definition_label.grid(row=1, column=0, padx=10, pady=5)
        definition_entry = tk.Entry(add_word_page)
        definition_entry.grid(row=1, column=1, padx=10, pady=5)

        save_button = tk.Button(add_word_page, text="Save", command=lambda: self.save_word(word_entry.get(), definition_entry.get(), category))
        save_button.grid(row=2, columnspan=2, padx=10, pady=5)

    def save_word(self, word, definition, category):
        with open("word_repository.txt", "a") as file:
            file.write(f"{category}:{word}:{definition}\n")
        messagebox.showinfo("Word Saved", "Word and definition saved successfully.")


class WordGuessGame:
    def __init__(self, master, word_repository_file):
        self.master = master
        self.word_repository_file = word_repository_file
        self.word = self.select_word()
        self.guesses_remaining = 5
        self.display_word = ["_" for _ in self.word]

        self.create_widgets()

    def create_widgets(self):
        self.word_label = tk.Label(self.master, text=" ".join(self.display_word))
        self.word_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack(pady=5)

    def select_word(self):
        with open(self.word_repository_file, "r") as file:
            words = file.readlines()
        return random.choice(words).strip()

    def make_guess(self):
        guess = self.guess_entry.get().lower().strip()  # Strip whitespace from guessed word
        self.guess_entry.delete(0, tk.END)

        # Check if the guessed word matches the word in the repository
        with open(self.word_repository_file, "r") as file:
            words = [word.strip().lower() for word in file.readlines()]
        if guess in words:
            # Correct guess logic
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.display_word[i] = guess
            self.word_label.config(text=" ".join(self.display_word))

            if "_" not in self.display_word:
                messagebox.showinfo("Congratulations!", f"You guessed the word '{self.word}' correctly!")
                self.reset_game()
        else:
            # Incorrect guess logic
            self.guesses_remaining -= 1
            if self.guesses_remaining == 0:
                messagebox.showinfo("Game Over", f"Sorry, you ran out of guesses. The word was '{self.word}'.")
                self.reset_game()
            else:
                messagebox.showinfo("Incorrect Guess", f"Sorry, '{guess}' is not in the word. You have {self.guesses_remaining} guesses remaining.")

    def reset_game(self):
        self.word = self.select_word()
        self.display_word = ["_" for _ in self.word]
        self.guesses_remaining = 5
        self.word_label.config(text=" ".join(self.display_word))


if __name__ == "__main__":
    app = Application()
    app.mainloop()
