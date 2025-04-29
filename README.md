# Simple Nutrition Lookup Tool (GUI Version)

## Overview
This Python-based desktop application estimates the nutritional values of common Indian dishes including calories, protein, and fiber.  
Instead of relying on fixed datasets, it uses smart logic to approximate values and provides results in a lightweight Tkinter GUI environment.

This project is designed to promote food awareness and encourage quick access to health insights through a user-friendly interface.

## Features

- Modern GUI built using Python's Tkinter library
- Offline estimation logic for popular Indian meals (e.g., dal chawal, poha, idli sambar)
- Search-driven interface with error handling for unmatched inputs
- Fast, lightweight, and beginner-friendly application

## Technologies Used

- Python 3.x
- Tkinter (GUI framework)
- Dictionary-based logic mapping (core estimation engine)

## How It Works

- The user enters a dish name into the input field
- The application checks for a match in its internal dictionary
- If matched, it displays approximate nutritional values
- If not matched, an appropriate message is displayed

## Sample Output

- Nutrition_Estimator

![nutrition_estimator](https://github.com/user-attachments/assets/53081b71-26c3-4363-ba81-d69ce0500679)


- Nutrition_Estimator_Output

![Nutrition_Estimator_Output](https://github.com/user-attachments/assets/a4fbdb81-74e2-4ba9-91c8-b1242a80a7f9)



## How to Run

1. Ensure Python 3 is installed
2. (Linux users) Install Tkinter if not available:

   ```bash
   sudo apt install python3-tk
   python3 nutrition_estimator_gui.py

## License

This project is licensed under the MIT License.
Feel free to fork, use, and enhance with credits.

## Author
Chaitanya Khot
