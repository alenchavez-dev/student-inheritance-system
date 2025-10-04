# ============================================================
# Program: Student Management & Inheritance System
# Author: Alen Chavez
# Description:
#   Demonstrates OOP in Python (inheritance, encapsulation, simple
#   polymorphism) via a clean console app. Users add Students,
#   GradStudents (thesis), and PhDStudents (dissertation) with
#   immediate input validation and neatly formatted output.
# ============================================================

class Student:
    """Base Student class storing first/last names."""
    def __init__(self, fname: str = "", lname: str = ""):
        self.fname = fname
        self.lname = lname

    @property
    def fname(self) -> str:
        return self.__fname.capitalize()

    @fname.setter
    def fname(self, value: str) -> None:
        self.__fname = value

    @property
    def lname(self) -> str:
        return self.__lname.capitalize()

    @lname.setter
    def lname(self, value: str) -> None:
        self.__lname = value

    def display_name(self) -> str:
        return f"{self.fname} {self.lname}"


class GradStudent(Student):
    """Graduate student with a thesis title."""
    def __init__(self, fname: str = "", lname: str = "", thesis: str = ""):
        super().__init__(fname, lname)
        self.thesis = thesis  # raw title (no label)

    @property
    def thesis(self) -> str:
        return self.__thesis

    @thesis.setter
    def thesis(self, value: str) -> None:
        self.__thesis = value.strip()


class PhDStudent(Student):
    """PhD student with a dissertation title."""
    def __init__(self, fname: str = "", lname: str = "", dissertation: str = ""):
        super().__init__(fname, lname)
        self.dissertation = dissertation  # raw title (no label)

    @property
    def dissertation(self) -> str:
        return self.__dissertation

    @dissertation.setter
    def dissertation(self, value: str) -> None:
        self.__dissertation = value.strip()


# --------------------------- Helpers ---------------------------

def ask_name(prompt: str) -> str:
    """Alphabetic-only name (no numbers/spaces)."""
    while True:
        s = input(prompt).strip()
        if s.isalpha():
            return s
        print("❌ Invalid input. Please enter alphabetic characters only.")

def ask_non_empty(prompt: str) -> str:
    """Non-empty free text (for titles)."""
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("❌ This field cannot be empty.")

def ask_student_type(prompt: str) -> str:
    """
    Menu validator: only S, G, P, Q accepted.
    Rejects numbers or any other characters.
    """
    valid = {"S", "G", "P", "Q"}
    while True:
        s = input(prompt).strip().upper()
        if s in valid:
            return s
        print("❌ Invalid option. Please enter S, G, P, or Q.")

def add_student(student_type: str):
    """Create the correct student type with validated inputs."""
    first = ask_name("Enter first name: ")
    last  = ask_name("Enter last name: ")

    if student_type == "G":
        thesis = ask_non_empty("Enter thesis title: ")
        return GradStudent(first, last, thesis)
    if student_type == "P":
        dissertation = ask_non_empty("Enter dissertation title: ")
        return PhDStudent(first, last, dissertation)
    return Student(first, last)

def print_records(students) -> None:
    """
    Neat, consistent output:
    - Name on the first line
    - 4-space indented label line directly below (aligned for all)
    - Fixed-width separator line for visual consistency
    """
    width = 60
    sep = "─" * width
    print("\n📚 Student Records")
    print(sep)
    for s in students:
        print(s.display_name())
        if isinstance(s, GradStudent):
            print("" * 4 + f"Thesis: {s.thesis}")
        elif isinstance(s, PhDStudent):
            print("" * 4 + f"Dissertation: {s.dissertation}")
        print(sep)


# ------------------------ Main Program ------------------------

def main():
    print("Welcome to the Student Management & Inheritance System\n")
    students = []

    while True:
        entry = ask_student_type("Enter student type (S=Student, G=Graduate, P=PhD, Q=Quit): ")
        if entry == "Q":
            break
        students.append(add_student(entry))

    print_records(students)


if __name__ == "__main__":
    main()
