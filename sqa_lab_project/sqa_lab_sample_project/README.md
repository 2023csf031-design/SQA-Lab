# SQA Lab Sample Project: Student Grade Manager

A small, complete Python project prepared for the **Software Construction and Development (SCD) Lab Manual**. It gives you real code to upload to GitHub in Lab 2 and, when your instructor provides access, to analyze with SonarQube for code quality.

## Table of Contents

1. Purpose of This Project
2. Features
3. Project Structure
4. Requirements
5. Getting Started
6. Running the Demo
7. Running the Tests
8. How the Code Works
9. Grading Scale
10. Usage Example
11. Uploading to GitHub (Lab 2)
12. Optional: Using Git on the Command Line
13. Running a SonarQube Scan
14. Verification Checklist
15. Troubleshooting
16. Ideas for Extending the Project

## 1. Purpose of This Project

The lab manual teaches basic Software Quality Assurance with GitHub and SonarQube, but it does not include any code. This project fills that gap. It is deliberately small so you can read every line, yet it contains the ingredients a quality tool looks at: functions, classes, input validation, error handling, documentation strings, and unit tests.

## 2. Features

* Add a student with a mark, or update the mark of an existing student
* Remove a student
* Validate input: names cannot be empty and marks must be between 0 and 100
* Calculate the class average
* Find the highest and lowest scoring students
* Convert any mark into a letter grade
* List students who passed or failed (the pass mark is 50)
* Print a report sorted by student name

## 3. Project Structure

    sqa_lab_sample_project/
        grade_manager.py            Main logic (GradeManager class and letter_grade function)
        main.py                     Demo program that prints a sample report
        test_grade_manager.py       14 unit tests
        Sonar configuration file    Settings for the SonarQube scan (see section 13)
        .gitignore                  Files Git should skip
        README.md                   This document

## 4. Requirements

* Python 3.8 or newer
* No extra packages. Everything used comes with Python.

Check your version by typing `python` in a terminal. The first line shows the version, and `exit()` leaves the prompt. On some systems the command is `python3`.

## 5. Getting Started

1. Download and unzip the project folder.
2. Open a terminal inside the folder.
3. Run the demo and the tests using the commands below.

## 6. Running the Demo

    python main.py

Expected output:

    Student Report
    Ayesha: 91.0 (A)
    Bilal: 67.5 (C)
    Hina: 48.0 (F)
    Usman: 76.0 (B)
    Class average: 70.62
    Top student: Ayesha
    Passed: Ayesha, Bilal, Usman
    Failed: Hina

## 7. Running the Tests

    python test_grade_manager.py

A successful run ends with a line that says the tests ran and the result is OK. The suite covers:

* Every letter grade boundary
* Adding, updating, and removing students
* Name trimming and rejection of empty names
* Rejection of marks below 0 or above 100
* Average, highest, and lowest calculations
* Behavior of an empty manager (average is 0.0, highest and lowest are None)
* Pass and fail lists
* Report formatting

## 8. How the Code Works

### The GradeManager class

* `add_student(name, mark)`: trims the name, checks it is not empty, checks the mark is between 0 and 100, then stores the mark as a decimal number.
* `remove_student(name)`: deletes a student and raises a KeyError if the name is unknown.
* `get_mark(name)`: returns one student's mark.
* `average()`: returns the class average, or 0.0 when there are no students.
* `highest()` and `lowest()`: return a tuple of name and mark, or None when there are no students.
* `grade_for(name)`: returns the letter grade for one student.
* `passed_students()` and `failed_students()`: return sorted name lists based on the pass mark.
* `report()`: returns one formatted line per student, sorted by name.

### The letter_grade function

Takes a mark and returns A, B, C, D, or F using the scale in section 9.

### Design notes

* Marks are kept in a private dictionary, so outside code uses the public methods instead of changing data directly.
* Invalid input raises a clear ValueError instead of failing silently.
* Every function has a short documentation string, which quality tools and teammates both appreciate.
* The pass mark is a named constant, so it can be changed in one place.

## 9. Grading Scale

* **A:** 85 and above
* **B:** 70 up to 84.9
* **C:** 60 up to 69.9
* **D:** 50 up to 59.9
* **F:** below 50

A student passes with a mark of 50 or more.

## 10. Usage Example

    from grade_manager import GradeManager

    manager = GradeManager()
    manager.add_student("Ayesha", 91)
    manager.add_student("Hina", 48)

    print(manager.average())          # 69.5
    print(manager.grade_for("Hina"))  # F
    print(manager.highest())          # ('Ayesha', 91.0)

## 11. Uploading to GitHub (Lab 2)

1. Open your SQA Lab repository on GitHub.
2. Click **Add file**, then **Upload files**.
3. Drag in `grade_manager.py`, `main.py`, `test_grade_manager.py`, the Sonar configuration file, and `.gitignore`. Keep this README if you want it to replace the one in your repository.
4. Write a commit message such as "Add sample project files".
5. Click **Commit changes**.
6. Return to the repository page and confirm that every file is listed.

## 12. Optional: Using Git on the Command Line

    git clone YOUR_REPOSITORY_URL
    cd YOUR_REPOSITORY_FOLDER
    git status
    git add .
    git commit
    git push origin main

Copy the project files into the cloned folder before running `git add .`. The `git commit` command opens an editor where you type the commit message.

## 13. Running a SonarQube Scan

Your instructor provides the SonarQube server address and a login token.

1. Confirm that the Sonar configuration file is in the project root. It already defines the project key and name, marks the two source files, marks the test file, and sets the Python version and file encoding.
2. Install the SonarScanner command line tool if it is not already available.
3. Run the scanner from the project folder, supplying the server address and token your instructor gave you.
4. Open the project in the SonarQube dashboard.

Things to look at on the dashboard:

* **Bugs:** code that is likely to fail
* **Vulnerabilities:** security weaknesses
* **Code smells:** maintainability problems
* **Duplications:** repeated blocks of code
* **Coverage:** how much code the tests exercise (needs a coverage report)
* **Quality Gate:** the overall pass or fail result

Because this project is small and clean, expect few or no issues. Try adding a deliberately messy function to see what SonarQube reports, then fix it and scan again.

## 14. Verification Checklist

* [ ] The demo prints the expected report
* [ ] All 14 tests pass
* [ ] All project files are uploaded to the SQA Lab repository
* [ ] The commit message is clear
* [ ] Every file is visible on the repository page
* [ ] The SonarQube scan completed and I reviewed the dashboard

## 15. Troubleshooting

**The python command is not found.**
Try `python3` instead, or install Python from python.org.

**The tests cannot import grade_manager.**
Run the command from inside the project folder so Python can see all the files.

**The upload page rejects a file.**
Upload the files directly, not a zipped folder, because GitHub stores a zip as one binary file.

**The Sonar configuration file is missing from GitHub.**
Files that start with a dot or are easy to overlook can be skipped when dragging. Check the file list and upload it again if needed.

**The scan fails to connect.**
Check the server address and token with your instructor.

## 16. Ideas for Extending the Project

* Save and load students from a file
* Add subjects so each student has several marks
* Add a command line menu for entering marks
* Add a coverage report so SonarQube can show test coverage
* Add a GitHub Actions workflow that runs the tests on every push

## Author and Course

Prepared for the Software Construction and Development lab sessions.
