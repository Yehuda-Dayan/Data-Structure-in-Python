students = {
    "Alice": {"grade": 90, "age": 17},
    "Bob": {"grade": 85, "age": 18},
    "Charlie": {"grade": 72, "age": 16}
}


def print_students():
    print("\n📚 Current student list:")
    for name, info in students.items():
        print(f"{name}: Grade = {info['grade']}, Age = {info['age']}")

print_students()


new_name = input("\nEnter new student name: ")
new_grade = float(input("Enter grade (0-100): "))
new_age = int(input("Enter age: "))
students[new_name] = {"grade": new_grade, "age": new_age}
print("\n✅ Student added.")
print_students()


name_to_update = input("\nEnter student name to update grade: ")
if name_to_update in students:
    updated_grade = float(input("Enter new grade: "))
    students[name_to_update]["grade"] = updated_grade
    print("✅ Grade updated.")
else:
    print("❌ Student not found.")
print_students()


name_to_remove = input("\nEnter student name to remove: ")
if name_to_remove in students:
    del students[name_to_remove]
    print(f"✅ {name_to_remove} was removed.")
else:
    print("❌ Student not found.")
print_students()


if students:
    total = sum(s["grade"] for s in students.values())
    average = total / len(students)
    print(f"\n🎓 Average grade: {average:.2f}")
else:
    print("\nNo students to calculate average.")


if students:
    top_student = max(students, key=lambda name: students[name]["grade"])
    top_grade = students[top_student]["grade"]
    print(f"🏅 Top student: {top_student} with grade {top_grade}")