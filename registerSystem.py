#Tkinter Register System
from tkinter import *
from tkinter import messagebox

def passwordCheck():
    try:
        with open('users.txt', 'r') as usersFile:
            content = usersFile.readlines()
            for line in content:
                editedLines = line.strip('\n').split(',')
                if usernameEntry.get() == editedLines[0]:
                    messagebox.showerror('ERROR', 'USERNAME TAKEN')
                    exit()
                    
    except FileNotFoundError:
        messagebox.showerror('ERROR', 'USERS.TXT WAS NOT FOUND')
        exit()

    if usernameEntry.get().strip('\n') == '':
        messagebox.showerror('ERROR', 'USERNAME CANNOT BE EMPTY')
        exit()
    elif passwordEntry.get().strip('\n') == '':
        messagebox.showerror('ERROR', 'PASSWORD CANNOT BE EMPTY')
        exit()
    elif passwordEntry.get() == confirmPasswordEntry.get():
        try:
            with open('users.txt', 'a') as usersFile:
                usersFile.write(usernameEntry.get())
                usersFile.write(',')
                usersFile.write(passwordEntry.get())
                usersFile.write('\n')
                messagebox.showinfo('SUCCESS', 'REGISTERED')
                exit()
        except FileNotFoundError:
            messagebox.showerror('ERROR', 'USERS.TXT WAS NOT FOUND')
            exit()
    elif passwordEntry.get() != confirmPasswordEntry.get():
        messagebox.showerror('ERROR', 'PASSWORDS DO NOT MATCH')
        exit()

root = Tk()
root.title('REGISTER SYSTEM')

usernameLabel = Label(root, text = 'USERNAME:')
usernameLabel.grid(column = 0, row = 0)
usernameEntry = Entry(root)
usernameEntry.grid(column = 1, row = 0)

passwordLabel = Label(root, text = 'PASSWORD:')
passwordLabel.grid(column = 0, row = 1)
passwordEntry = Entry(root)
passwordEntry.grid(column = 1, row = 1)

confirmPasswordLabel = Label(root, text = 'CONFIRM PASSWORD:')
confirmPasswordLabel.grid(column = 0, row = 2)
confirmPasswordEntry = Entry(root)
confirmPasswordEntry.grid(column = 1, row = 2)

submitButton = Button(root, text = 'SUBMIT', command = passwordCheck)
submitButton.grid(column = 2, row = 2)

root.mainloop()
