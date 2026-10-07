"""Run a sample course through the grade calculator."""

from grades import letter_grade, weighted_average

COURSE = [
    {"name": "Homework", "scores": [95, 88, 92, 100], "weight": 0.25},
    {"name": "Quizzes", "scores": [78, 85, 90], "weight": 0.15},
    {"name": "Midterm", "scores": [84], "weight": 0.25},
    {"name": "Final", "scores": [89], "weight": 0.35},
]

# Worked out by hand:
#   Homework 93.75 * 0.25 = 23.44
#   Quizzes  84.33 * 0.15 = 12.65
#   Midterm  84.00 * 0.25 = 21.00
#   Final    89.00 * 0.35 = 31.15
#                   total = 88.24
EXPECTED = 88.24


def main():
    grade = weighted_average(COURSE)
    print(f"Calculated: {grade:.2f} ({letter_grade(grade)})")
    print(f"Expected:   {EXPECTED:.2f} ({letter_grade(EXPECTED)})")


if __name__ == "__main__":
    main()
