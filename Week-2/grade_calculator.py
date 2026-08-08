# Week 2 - Python Basics
# Project: Student Grade Calculator


def calculate_grade(marks):
    """Return the grade and an encouraging message based on marks."""

    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep up the outstanding performance."
    elif 80 <= marks < 90:
        return "B", "Great job! Keep working hard and aim even higher."
    elif 70 <= marks < 80:
        return "C", "Good effort! Keep practicing to improve further."
    elif 60 <= marks < 70:
        return "D", "You passed! Keep working consistently to improve."
    else:
        return "F", "Don't give up! Review the topics and keep practicing."


def get_valid_marks():
    """Get and validate marks between 0 and 100."""

    while True:
        try:
            marks = float(input("Enter student's marks (0-100): "))

            if 0 <= marks <= 100:
                return marks

            print("Invalid marks. Please enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    print("=" * 45)
    print("       STUDENT GRADE CALCULATOR")
    print("=" * 45)

    marks = get_valid_marks()
    grade, message = calculate_grade(marks)

    print("\n" + "-" * 45)
    print(f"Marks : {marks:g}")
    print(f"Grade : {grade}")
    print(f"Message: {message}")
    print("-" * 45)


if __name__ == "__main__":
    main()