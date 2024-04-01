import tkinter as tk
from tkinter import messagebox
import os

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the entered username and password match the stored credentials
    if username in users and users[username] == password:
        message_label.config(text="Login successful")
        # Open the home page after successful login
        open_home_page()
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

def open_signup_page():
    # Create a new window for the signup page
    signup_window = tk.Toplevel(root)
    signup_window.title("Signup")
    signup_window.geometry("300x200")  # Set window size
    
    # Create labels and entry widgets for signup
    reg_username_label = tk.Label(signup_window, text="New Username:")
    reg_username_label.grid(row=0, column=0, padx=10, pady=5)
    reg_username_entry = tk.Entry(signup_window)
    reg_username_entry.grid(row=0, column=1, padx=10, pady=5)

    reg_password_label = tk.Label(signup_window, text="New Password:")
    reg_password_label.grid(row=1, column=0, padx=10, pady=5)
    reg_password_entry = tk.Entry(signup_window, show="*")
    reg_password_entry.grid(row=1, column=1, padx=10, pady=5)

    def register():
        new_username = reg_username_entry.get()
        new_password = reg_password_entry.get()

        # Check if the username is already taken
        if new_username in users:
            messagebox.showerror("Signup Error", "Username already exists. Please choose another one.")
        else:
            # Add the new user to the dictionary and update the storage file
            users[new_username] = new_password
            with open("user_credentials.txt", "a") as file:
                file.write(f"{new_username}:{new_password}\n")
            messagebox.showinfo("Signup Success", "Registration successful. You can now log in.")
            signup_window.destroy()

    register_button = tk.Button(signup_window, text="Register", command=register)
    register_button.grid(row=2, columnspan=2, padx=10, pady=5)

def open_home_page():
    # Create a new window for the home page
    home_window = tk.Toplevel(root)
    home_window.title("Home")
    home_window.geometry("300x200")  # Set window size
    # Add widgets and layout for the home page
    welcome_label = tk.Label(home_window, text=f"Welcome, {username_entry.get()}!")
    welcome_label.pack(padx=10, pady=5)
    # You can add more widgets to the home page as needed

# Check if the user_credentials.txt file exists, if not, create an empty file
if not os.path.exists("user_credentials.txt"):
    open("user_credentials.txt", "w").close()

# Load existing user credentials from the storage file
users = {}
with open("user_credentials.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(":")
        users[username] = password

# Create GUI window
root = tk.Tk()
root.title("Login")
root.geometry("300x400")  # Set window size

# Create labels and entry widgets for login
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

message_label = tk.Label(root, text="")
message_label.grid(row=2, columnspan=2, padx=10, pady=5)

login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=3, columnspan=2, padx=10, pady=5)

# Link to register a new account
register_label = tk.Label(root, text="Don't have an account? Register an account.", fg="blue", cursor="hand2")
register_label.grid(row=4, columnspan=2, padx=10, pady=5)

def open_signup_page_callback(event):
    open_signup_page()

register_label.bind("<Button-1>", open_signup_page_callback)

# Run the GUI application
root.mainloop()
