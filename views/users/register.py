from style import set_stylesheet
import re
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout, QWidget, QMessageBox
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Set window title
        self.setWindowTitle('User Registration Form')

        # Create widgets
        self.first_name_label = QLabel('First Name:')
        self.first_name_edit = QLineEdit()

        self.last_name_label = QLabel('Last Name:')
        self.last_name_edit = QLineEdit()

        self.username_label = QLabel('Username:')
        self.username_edit = QLineEdit()

        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.confirm_password_label = QLabel('Confirm Password:')
        self.confirm_password_edit = QLineEdit()
        self.confirm_password_edit.setEchoMode(QLineEdit.Password)

        self.submit_button = QPushButton('Submit')
        self.cancel_button = QPushButton('Cancel')

        self.message_label = QLabel('')

        self.password_requirements_label = QLabel(
            '''<font size="3">
            Password Requirements:<br>
            &bull; 1 uppercase<br>
            &bull; 1 lowercase<br>
            &bull; 1 number<br>
            &bull; 1 special character<br>
            &bull; 8-30 characters long
            </font>'''
        )

        # Set up layouts
        self.grid_layout = QGridLayout()
        self.grid_layout.addWidget(self.first_name_label, 0, 0)
        self.grid_layout.addWidget(self.first_name_edit, 0, 1)
        self.grid_layout.addWidget(self.last_name_label, 1, 0)
        self.grid_layout.addWidget(self.last_name_edit, 1, 1)
        self.grid_layout.addWidget(self.username_label, 2, 0)
        self.grid_layout.addWidget(self.username_edit, 2, 1)
        self.grid_layout.addWidget(self.password_label, 3, 0)
        self.grid_layout.addWidget(self.password_edit, 3, 1)
        self.grid_layout.addWidget(self.confirm_password_label, 4, 0)
        self.grid_layout.addWidget(self.confirm_password_edit, 4, 1)

        self.hbox_layout = QHBoxLayout()
        self.hbox_layout.addWidget(self.submit_button)
        self.hbox_layout.addWidget(self.cancel_button)

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addLayout(self.grid_layout)
        self.vbox_layout.addWidget(self.password_requirements_label)
        self.vbox_layout.addLayout(self.hbox_layout)
        self.vbox_layout.addWidget(self.message_label)

        self.setLayout(self.vbox_layout)


        # Connect signals and slots
        self.submit_button.clicked.connect(self.check_passwords)

    def check_passwords(self):
        password = self.password_edit.text()
        confirm_password = self.confirm_password_edit.text()

        if password != confirm_password:
            self.message_label.setText('Passwords do not match.')
        elif not self.validate_password(password):
            self.message_label.setText('Password does not meet requirements.')
        else:
            self.message_label.setText('Registration successful.')
            self.show_success_message()

    def show_success_message(self):
        success_message = QMessageBox(self)
        success_message.setWindowTitle('Success')
        success_message.setText('User registered successfully!')
        success_message.setIcon(QMessageBox.Information)
        success_message.exec_()


if __name__ == '__main__':
    # Create a QApplication instance
	app = QApplication(sys.argv)
	# Set the stylesheet
	set_stylesheet(app)
	registration_form = RegistrationForm()
	registration_form.show()
	app.exec_()
	print(sys.argv)
