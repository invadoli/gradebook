import argparse
from gradebook import service

def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI Management System")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # add-student --name "..."
    parser_student = subparsers.add_parser("add-student")
    parser_student.add_argument("--name", required=True)

    # add-course --code CS101 --title "..."
    parser_course = subparsers.add_parser("add-course")
    parser_course.add_argument("--code", required=True)
    parser_course.add_argument("--title", required=True)

    # enroll --student-id 1 --course CS101
    parser_enroll = subparsers.add_parser("enroll")
    parser_enroll.add_argument("--student-id", type=int, required=True)
    parser_enroll.add_argument("--course", required=True)

    # add-grade --student-id 1 --course CS101 --grade 95
    parser_grade = subparsers.add_parser("add-grade")
    parser_grade.add_argument("--student-id", type=int, required=True)
    parser_grade.add_argument("--course", required=True)
    parser_grade.add_argument("--grade", type=int, required=True)

    # list [students|courses|enrollments] [--sort name|code]
    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("category", choices=['students', 'courses', 'enrollments'])
    parser_list.add_argument("--sort", choices=['name', 'code'], default=None)

    # avg --student-id 1 --course CS101
    parser_avg = subparsers.add_parser("avg")
    parser_avg.add_argument("--student-id", type=int, required=True)
    parser_avg.add_argument("--course", required=True)

    # gpa --student-id 1
    parser_gpa = subparsers.add_parser("gpa")
    parser_gpa.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    try:
        if args.command == "add-student":
            sid = service.add_student(args.name)
            print(f"Successfully added student '{args.name}' with ID: {sid}")
        
        elif args.command == "add-course":
            service.add_course(args.code, args.title)
            print(f"Successfully added course: {args.code} - {args.title}")

        elif args.command == "enroll":
            service.enroll(args.student_id, args.course)
            print(f"Enrolled student {args.student_id} in course {args.course}")

        elif args.command == "add-grade":
            service.add_grade(args.student_id, args.course, args.grade)
            print(f"Added grade {args.grade} for student {args.student_id} in {args.course}")

        elif args.command == "list":
            items = []
            if args.category == "students":
                items = service.list_students()
                if args.sort == "name": items.sort(key=lambda x: x['name'])
                for s in items: print(f"ID: {s['id']} | Name: {s['name']}")
            
            elif args.category == "courses":
                items = service.list_courses()
                if args.sort == "code": items.sort(key=lambda x: x['code'])
                for c in items: print(f"Code: {c['code']} | Title: {c['title']}")
            
            elif args.category == "enrollments":
                for e in service.list_enrollments():
                    print(f"Student: {e['student_id']} | Course: {e['course_code']} | Grades: {e['grades']}")

        elif args.command == "avg":
            avg = service.compute_average(args.student_id, args.course)
            print(f"Average for student {args.student_id} in {args.course}: {avg:.2f}")

        elif args.command == "gpa":
            gpa = service.compute_gpa(args.student_id)
            print(f"GPA for student {args.student_id}: {gpa:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()