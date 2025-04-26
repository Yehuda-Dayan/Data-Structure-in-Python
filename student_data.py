students = {
    "Ron": {
        "age": 17,
        "subjects": ["Math", "Science", "English"],
        "grades": {85, 90, 78}
    },
    "Bob": {
        "age": 18,
        "subjects": ["History", "Math", "Art"],
        "grades": {88, 92, 80}
    }
}
def print_students():
    print("\n📚 Current student list:")
    for name, info in students.items():
        print(f"\nStudent: {name}")
        print(f"Age: {info['age']}")
        print("Subjects:")
        for subject in info['subjects']:
            print(f"  - {subject}")
        print("Grades:")
        for grade in info['grades']:
            print(f"  - {grade}")

new_name = input("\nEnter new student name: ")
new_age = int(input("Enter age: "))
new_subjects = input("Enter subjects (comma-separated): ").split(",")
new_subjects = [subject.strip() for subject in new_subjects]
new_grades = input("Enter grades (comma-separated): ").split(",")
new_grades = {int(grade.strip()) for grade in new_grades}
students[new_name] = {
    "age": new_age,
    "subjects": new_subjects,
    "grades": new_grades
}
print("\n✅ Student added.")
print_students()

name_to_update = input("\nEnter student name to update grade: ")
if name_to_update in students:
    updated_grades = input("Enter new grades (comma-separated): ").split(",")
    updated_grades = {int(grade.strip()) for grade in updated_grades}
    students[name_to_update]["grades"] = updated_grades
    print("✅ Grades updated.")
else:
    print("❌ Student not found.")
print_students()

student_name = input("\nEnter student name to remove subject: ")
subject_to_remove = input("Enter subject to remove: ")
if student_name in students:
    if subject_to_remove in students[student_name]["subjects"]:
        students[student_name]["subjects"].remove(subject_to_remove)
        print(f"Subject '{subject_to_remove}' removed from {student_name}.")
    else:
        print(f"Subject '{subject_to_remove}' not found for {student_name}.")
else:
    print(f"Student '{student_name}' not found.")
print_students()
student_name = input("Enter student name to calculate average: ").strip()

if student_name in students:
    grades_list = list(students[student_name]["grades"])
    average = sum(grades_list) / len(grades_list)
    print(f"{student_name}'s average grade: {average:.2f}")
else:
    print("Student not found.")


highest_avg = 0
top_student = None

for name, info in students.items():
    grades_list = list(info["grades"])
    avg = sum(grades_list) / len(grades_list)
    if avg > highest_avg:
        highest_avg = avg
        top_student = name

if top_student:
    print(f"\n🏅 Top student: {top_student}")
    print(f"Age: {students[top_student]['age']}")
    print(f"Subjects: {', '.join(students[top_student]['subjects'])}")


student_tuples = []

for name, info in students.items():
    tup = (name, info["age"], len(info["subjects"]))
    student_tuples.append(tup)

student_tuples.sort(key=lambda x: x[2])

print("\n📦 Students sorted by number of subjects:")
for student in student_tuples:
    print(student)