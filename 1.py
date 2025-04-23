from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

# Basic PyQt app setup
app = QApplication()

# Main window
window = QWidget()
window.setWindowTitle('Button Layouts - Ex 1')
window.resize(600,400)
# --- Layout and Widgets ---
# The main vertical layout
main_layout = QVBoxLayout()

# Create the three buttons
button1 = QPushButton('Button 1')
button2 = QPushButton('Button 2')
button3 = QPushButton('Button 3')

# Add the buttons directly to the vertical layout
main_layout.addWidget(button1)
main_layout.addWidget(button2)
main_layout.addWidget(button3)
# --- End Layout and Widgets ---

# Apply the layout to the window
window.setLayout(main_layout)

# Show the window and run the app
window.show()
app.exec_()

