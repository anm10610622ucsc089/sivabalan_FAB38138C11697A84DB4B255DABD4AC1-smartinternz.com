class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the student list in descending order of CGPA
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

# Example usage:
if __name__ == "__main__":
    students = [
        Student("bala", "001", 3.8),
        Student("suresh", "002", 3.5),
        Student("vimal", "003", 3.9),
        Student("kavi", "004", 3.7)
    ]

    sorted_students = sort_students(students)
    
    # Print sorted students
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")