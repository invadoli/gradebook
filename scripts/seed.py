import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gradebook import service

def run_seed():
    """Populates the gradebook with initial sample data."""
    print("Starting data seed...")

    try:
        # Add Students
        s1 = service.add_student("Urata Smakiqi")
        s2 = service.add_student("Berat Ujkani")

        # Add Courses
        service.add_course("CS102", "Introduction to Programming")
        service.add_course("MATH201", "Calculus I")

        # Enrollments
        service.enroll(s1, "CS102")
        service.enroll(s1, "MATH201")
        service.enroll(s2, "CS102")

        # Add Grades
        service.add_grade(s1, "CS102", 92)
        service.add_grade(s1, "CS102", 88)
        service.add_grade(s1, "MATH201", 75)
        service.add_grade(s2, "CS102", 85)

        print("Seed successful! data/gradebook.json has been populated.")

    except Exception as e:
        print(f"Seed failed: {e}")

if __name__ == "__main__":
    run_seed()