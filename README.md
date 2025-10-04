# 🎓 Student Management & Inheritance System

A clean Python console app that demonstrates **object-oriented programming** with immediate **input validation** and **neatly formatted output**. Users can add:
- **Students** (name only)
- **Graduate Students** (name + thesis)
- **PhD Students** (name + dissertation)

---

## 🚀 Features
- Inheritance: `Student` → `GradStudent`, `PhDStudent`
- Encapsulation via properties
- Simple polymorphism in display logic
- Strict input validation:
  - Menu accepts **S/G/P/Q** only
  - Names are **alphabetic only**
  - Titles (thesis/dissertation) must be **non-empty**
- Tidy, consistent console output with aligned labels

---

## 🧰 Tech Stack
- **Python 3.x**
- No external libraries

---

## 📂 Project Structure
    student-inheritance-system/
    ├── student_management.py   # Main program
    └── README.md               # This file

---

## ▶️ How to Run
    python3 student_management.py

---

## 📝 Example Session
    Welcome to the Student Management & Inheritance System

    Enter student type (S=Student, G=Graduate, P=PhD, Q=Quit): S
    Enter first name: Alen
    Enter last name: Chavez
    Enter student type (S=Student, G=Graduate, P=PhD, Q=Quit): G
    Enter first name: Dknd
    Enter last name: Wkdxns
    Enter thesis title: AI for Routing
    Enter student type (S=Student, G=Graduate, P=PhD, Q=Quit): P
    Enter first name: Mk
    Enter last name: Cejcnw
    Enter dissertation title: Advanced Systems
    Enter student type (S=Student, G=Graduate, P=PhD, Q=Quit): Q

    📚 Student Records
    ────────────────────────────────────────────────────────────
    Alen Chavez
    ────────────────────────────────────────────────────────────
    Dknd Wkdxns
    Thesis: AI for Routing
    ────────────────────────────────────────────────────────────
    Mk Cejcnw
    Dissertation: Advanced Systems
    ────────────────────────────────────────────────────────────

---

## 💡 Notes
- Inputs are re-prompted until valid.
- Output uses a fixed separator width for consistent formatting.

---

## 🧑‍💻 Author
**Alen Chavez**

---

## 📝 License
MIT License
