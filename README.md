# student-result-management-system-of-pass-fail
Python GUI app for managing student results using Excel
# 📊 Student Result Management System (Python GUI)

A Python-based desktop application that analyzes student academic results from an Excel file and displays class-wise performance using a clean and interactive graphical user interface.

This project is suitable for college mini-projects, RTRP submissions, and resume portfolios.

---

## 🚀 Features

- 📁 Load student data from Excel (.xlsx file)
- 📚 Automatically detects subjects without hardcoding
- 🏫 Displays available classes dynamically
- ✅ Separates pass and fail students
- 📊 Calculates GPA (average of subject marks)
- ❌ Shows failed subjects and failure count
- 📈 Sorts students by GPA (highest to lowest)
- 📉 Displays pass and fail percentages
- 🖥️ User-friendly Tkinter GUI

---

## 🛠️ Technologies Used

- Python  
- Tkinter (GUI)  
- Pandas  
- OpenPyXL  

---

## 📂 Project Structure

student-result-management-system/
│
├── student_result_gui.py
├── README.md
├── requirements.txt
└── sample_data.xlsx

yaml
Copy code

---

## 📑 Excel File Format

The Excel file must follow this format:

| RollNo | Name | Class | Subject1 | Subject2 | Subject3 | ... |
|-------|------|-------|----------|----------|----------|-----|

### Rules:
- First column → Roll Number  
- Second column → Student Name  
- Third column → Class (e.g., CSE-A, CSE-B)  
- Remaining columns → Subject marks  
- Pass mark = **35**  
- Marks must be numeric  

---

## ▶️ How to Run the Application

### 1️⃣ Install Python
Ensure Python 3.9 or above is installed.

Download from: https://www.python.org/downloads/

---

### 2️⃣ Run the Program

```bash
python student_result_gui.py
Required libraries (pandas and openpyxl) will be installed automatically if missing.

🧠 How the Application Works
Click Load Excel

Select the Excel file

Choose a class from the sidebar

View:

Pass students

Fail students

GPA rankings

Pass/Fail statistics

🎯 Use Cases
College and school result analysis

Academic performance tracking

Python GUI mini project

RTRP project submission

Resume portfolio project

🔮 Future Enhancements
Export results to PDF or Excel

Student search functionality

Graphical performance analysis (charts)

Admin login system

Attendance integration

👤 Author
Shaik Irfan Hussain
B.Tech CSE Student
GitHub: https://github.com/247r1a05c2-b

