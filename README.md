````markdown
# Gradebook CLI Management System

A Python-based command-line interface (CLI) for managing students, courses, and grades with persistent JSON storage.

## Setup Instructions

### 1. Create a Virtual Environment
Open your terminal in the project root and run:
```powershell
python -m venv venv
````

### 2. Activate the Virtual Environment

**Windows:**

```powershell
.\venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 3. Initialize Data (Seed Script)

To populate the system with initial sample data for testing, run:

```powershell
python scripts/seed.py
```

## Usage & Examples

### Student and Course Management

**Add a student:**

```bash
python main.py add-student --name "Inva"
```

Expected Output:

```
Successfully added student 'Inva' with ID: 1
```

**Add a course:**

```bash
python main.py add-course --code CS101 --title "Intro to CS"
```

### 📘 Enrollment and Grading

**Enroll a student in a course:**

```bash
python main.py enroll --student-id 1 --course CS101
```

**Add a grade (0–100):**

```bash
python main.py add-grade --student-id 1 --course CS101 --grade 95
```

### Reports and Calculations

**List students (sorted by name):**

```bash
python main.py list students --sort name
```

**Calculate average for a specific course:**

```bash
python main.py avg --student-id 1 --course CS101
```

**Calculate total GPA:**

```bash
python main.py gpa --student-id 1
```

Expected Output:

```
GPA for student 1: 95.00
```

## Design Decisions & Limitations

### Design Decisions

* **JSON Persistence:**
  Data is stored in a structured JSON format within the `data/` directory. This ensures data persists between sessions without needing a database.

* **Modular Package Architecture:**
  The project uses a subpackage named `gradebook` to separate Models, Logic, and Storage.

* **Input Validation:**
  Helper functions (like `parse_grade`) validate user input before storing data.

* **Logging:**
  A centralized logging system (`logs/app.log`) tracks operations and errors.

```
```
