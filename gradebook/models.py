class Student:
    def __init__(self, student_id, name):
        if not name or not name.strip():
            raise ValueError("Student name cannot be empty.")
        self.id = student_id
        self.name = name

    def __str__(self):
        return f"Student(id={self.id}, name={self.name})"
    
class Course:
    def __init__(self, code, title):
        if not title or not title.strip():
            raise ValueError("Course title cannot be empty.")
        self.code = code
        self.title = title

    def __str__(self):
        return f"Course(code={self.code}, title={self.title})"
    
class Enrollment:
    def __init__(self, student_id, course_code, grades=None):
        if grades is None:
            grades = []
        for g in grades:
            if not (0 <= g <= 100):
                raise ValueError(f"Invalid grade {g}. Must be between 0 and 100.")
        
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades

    def __str__(self):
        return f"Enrollment [Student: {self.student_id}, Course: {self.course_code}, Grades: {self.grades}]"