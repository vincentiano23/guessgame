import tkinter as tk
from tkinter import messagebox
import os

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    # Check if the entered username and password match the stored credentials
    if username in users and users[username] == password:
        message_label.config(text="Login successful")
        show_page(home_page)
    else:
        messagebox.showerror("Login Error", "Invalid username or password")

def open_signup_page():
    show_page(signup_page)

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
        show_page(login_page)

def show_page(page):
    # Hide all pages
    login_page.grid_forget()
    signup_page.grid_forget()
    home_page.grid_forget()

    # Show the requested page
    page.grid(row=0, column=0, padx=10, pady=5)

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

# Create login page
login_page = tk.Frame(root)

username_label = tk.Label(login_page, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5)
username_entry = tk.Entry(login_page)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(login_page, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(login_page, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

message_label = tk.Label(login_page, text="")
message_label.grid(row=2, columnspan=2, padx=10, pady=5)

login_button = tk.Button(login_page, text="Login", command=login)
login_button.grid(row=3, columnspan=2, padx=10, pady=5)

register_label = tk.Label(login_page, text="Don't have an account? Register an account.", fg="blue", cursor="hand2")
register_label.grid(row=4, columnspan=2, padx=10, pady=5)

register_label.bind("<Button-1>", lambda event: open_signup_page())

# Create signup page
signup_page = tk.Frame(root)
signup_page.grid(row=0, column=0, padx=10, pady=5)

reg_username_label = tk.Label(signup_page, text="New Username:")
reg_username_label.grid(row=0, column=0, padx=10, pady=5)
reg_username_entry = tk.Entry(signup_page)
reg_username_entry.grid(row=0, column=1, padx=10, pady=5)

reg_password_label = tk.Label(signup_page, text="New Password:")
reg_password_label.grid(row=1, column=0, padx=10, pady=5)
reg_password_entry = tk.Entry(signup_page, show="*")
reg_password_entry.grid(row=1, column=1, padx=10, pady=5)

register_button = tk.Button(signup_page, text="Register", command=register)
register_button.grid(row=2, columnspan=2, padx=10, pady=5)

# Create home page
home_page = tk.Frame(root)
home_page.grid(row=0, column=0, padx=10, pady=5)

welcome_label = tk.Label(home_page, text="Welcome to the Home Page!")
welcome_label.pack(padx=10, pady=5)

# Show login page initially
show_page(login_page)

# Run the GUI application
root.mainloop()
