from .storage import load_data, save_data
from .models import Student, Course, Enrollment

def add_student(name):
    data = load_data()
    new_id = max([s['id'] for s in data['students']], default=0) + 1
    
    student = Student(new_id, name)
    data['students'].append({"id": student.id, "name": student.name})
    
    save_data(data)
    return new_id

def add_course(code, title):
    data = load_data()
    if any(c['code'] == code for c in data['courses']):
        raise ValueError(f"Course {code} already exists.")
    
    course = Course(code, title)
    data['courses'].append({"code": course.code, "title": course.title})
    save_data(data)

def enroll(student_id, course_code):
    data = load_data()
    
    if not any(s['id'] == student_id for s in data['students']):
        raise ValueError(f"Student ID {student_id} not found.")
    if not any(c['code'] == course_code for c in data['courses']):
        raise ValueError(f"Course {course_code} not found.")

    for en in data['enrollments']:
        if en['student_id'] == student_id and en['course_code'] == course_code:
            return 
            
    data['enrollments'].append({
        "student_id": student_id, 
        "course_code": course_code, 
        "grades": []
    })
    save_data(data)

def add_grade(student_id, course_code, grade):
    data = load_data()
    found = False
    for en in data['enrollments']:
        if en['student_id'] == student_id and en['course_code'] == course_code:
            temp_en = Enrollment(student_id, course_code, en['grades'] + [grade])
            en['grades'].append(grade)
            found = True
            break
    
    if not found:
        raise ValueError("Enrollment not found. Enroll the student first.")
    
    save_data(data)

def compute_average(student_id, course_code):
    data = load_data()
    for en in data['enrollments']:
        if en['student_id'] == student_id and en['course_code'] == course_code:
            if not en['grades']: return 0.0
            return sum(en['grades']) / len(en['grades'])
    raise ValueError("Enrollment not found.")

def compute_gpa(student_id):
    data = load_data()
    student_enrollments = [en for en in data['enrollments'] if en['student_id'] == student_id]
    
    if not student_enrollments:
        return 0.0
        
    averages = []
    for en in student_enrollments:
        if en['grades']:
            averages.append(sum(en['grades']) / len(en['grades']))
    
    return sum(averages) / len(averages) if averages else 0.0

def list_students():
    return load_data()['students']

def list_courses():
    return load_data()['courses']

def list_enrollments():
    return load_data()['enrollments']