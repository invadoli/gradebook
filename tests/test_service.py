import unittest
import os
import json
from gradebook import service

class TestGradebookService(unittest.TestCase):

    def setUp(self):
        """Clean up the data file before each test to ensure a fresh start."""
        self.test_file = "data/gradebook.json"
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_student_happy_path(self):
        """Test adding a valid student successfully."""
        sid = service.add_student("Inva")
        students = service.list_students()
        self.assertEqual(len(students), 1)
        self.assertEqual(students[0]['name'], "Inva")
        self.assertEqual(sid, 1)

    def test_add_grade_happy_path(self):
        """Test adding a numeric grade between 0-100."""
        service.add_student("Inva")
        service.add_course("CS101", "Intro to CS")
        service.enroll(1, "CS101")
        service.add_grade(1, "CS101", 95)
        
        enrollments = service.list_enrollments()
        self.assertIn(95, enrollments[0]['grades'])

    def test_compute_average_happy_path(self):
        """Test calculating the mean of grades."""
        service.add_student("Inva")
        service.add_course("CS101", "Intro to CS")
        service.enroll(1, "CS101")
        service.add_grade(1, "CS101", 80)
        service.add_grade(1, "CS101", 90)
        
        avg = service.compute_average(1, "CS101")
        self.assertEqual(avg, 85.0)

    def test_invalid_grade_edge_case(self):
        """Test that a grade > 100 raises a ValueError."""
        service.add_student("Inva")
        service.add_course("CS101", "Intro to CS")
        service.enroll(1, "CS101")
        
        with self.assertRaises(ValueError):
            service.add_grade(1, "CS101", 150)

if __name__ == '__main__':
    unittest.main()