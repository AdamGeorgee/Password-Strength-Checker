import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    #password length
    characters = 0
    for character in password:
        characters += 1
    if characters < 8:
        return "Password Strength: Weak -- Password should be at least 8 characters."

    #letters
    letters = 0
    for character in password:
        if character.isalpha() == True:
            letters += 1
    if letters == 0:
        return "Password Strength: Weak -- Password should include at least 1 letter."
    
    #numbers
    numbers = 0
    for character in password:
        if character.isnumeric() == True:
            numbers += 1
    if numbers == 0:
        return "Password Strength: Weak -- Password should include at least 1 number."

    #special characters
    spec_char = 0
    chars = '[^a-zA-Z0-9]+'
    if not(re.search(chars, password)):
        return "Password Strength: Moderate -- Password should include at least 1 special character."

    #upper and lower case letters
    upper_case_letters = 0
    lower_case_letters = 0
    for character in password:
        if character.isupper() == True:
            upper_case_letters += 1
        if character.islower() == True:
            lower_case_letters += 1
    if upper_case_letters == 0 or lower_case_letters == 0:
        return "Password Strength: Moderate -- Password should include at least 1 uppercase and 1 lowercase letter."
    
    #strong password
    return "Password Strength: Strong!"

def check_white_spaces(password):
    whitespaces = 0
    for character in password:
        if character == ' ':
            whitespaces += 1
    if whitespaces > 0:
        return True
    else:
        return False

def check_password():
    password = password_entry.get()
    if check_white_spaces(password) == True:
        messagebox.showerror("Error", "Password cannot contain white spaces.")
    else:
        password_strength = check_password_strength(password)
        messagebox.showinfo("Password Strength", password_strength)

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x250")

title = tk.Label(root, text="Password Strength Checker", font=("Arial, 20"))
password_label = tk.Label(root, text="Enter Password: ")
password_entry = tk.Entry(root, show="*")
check_password_button = tk.Button(root, text ="Check Strength", command=check_password)

title.pack()
password_label.pack()
password_entry.pack()
check_password_button.pack()

root.mainloop()