# Student Progression Outcome System

## Overview
This Python program determines the progression outcome of students based on their credit scores in different categories. It supports both students and staff members and provides various functionalities such as saving results, generating a histogram, and writing outputs to a file.

## Features
- Accepts user input for credits in "Pass", "Defer", and "Fail" categories.
- Validates inputs to ensure they are within the allowed credit range.
- Determines progression outcomes:
  - Progress
  - Progress (Module Trailer)
  - Module Retriever
  - Exclude
- Allows staff members to enter multiple records.
- Displays results in a histogram using a graphical interface.
- Saves results to a text file and allows retrieval of saved records.

## Requirements
- Python 3.x
- `graphics.py` (for rendering histograms)

## Installation
1. Ensure you have Python 3 installed.
2. Install `graphics.py` if not already installed. You can download it from: [Graphics.py](https://mcsp.wartburg.edu/zelle/python/)
3. Place `progression_outcome.py` in your working directory.

## Usage
### Running the program
Execute the script using:
```sh
python progression_outcome.py
```

### User Types
- **Student**: Can enter credits once and receive an outcome.
- **Staff**: Can enter multiple records, view a histogram, and save results.

### Output
1. The program prints the outcome based on input credits.
2. If the user is a staff member:
   - Results are stored and displayed in bulk.
   - A histogram is generated for visualization.
   - The outcomes are saved to `CWText.txt`.
   - The saved records can be displayed upon request.

## Example Run
```
Are you a Student or Staff Member (student/staff) : staff

Please enter your credits at pass: 100
Please enter your credits at defer: 20
Please enter your credits at fail: 0
Progress (Module Trailer)

Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: q
```
A histogram window appears, and results are displayed and saved.

## File Structure
- `progression_outcome.py` - Main program file.
- `CWText.txt` - Stores saved progression results.

## Author
- **Name :** Thinuka Lehan
- **Student ID:** w2052786
- **Date:** 10/12/2023

## License
This project is for educational purposes only and is not intended for commercial use.

