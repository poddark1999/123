
# Importing tkinter module'
from tkinter import *

def main():
	# Create a new window
	window = Tk()

	# Set the window title
	window.title("Registration Form")

	# Set the window size
	window.geometry("400x300")

	# Create a label for the username field
	username_label = Label(window, text="Username:")
	username_label.pack()

	# Create an entry field for the username
	username_entry = Entry(window)
	username_entry.pack()

	# Create a label for the password field
	password_label = Label(window, text="Password:")
	password_label.pack()

	# Create an entry field for the password
	password_entry = Entry(window, show="*")
	password_entry.pack()

	# Create a label for the email field
	email_label = Label(window, text="Email:")
	email_label.pack()

	# Create an entry field for the email
	email_entry = Entry(window)
	email_entry.pack()

	# Create a button to submit the form
	submit_button = Button(window, text="Submit")
	submit_button.pack()

	# Run the window
	window.mainloop()


if __name__ == '__main__':
	main()
