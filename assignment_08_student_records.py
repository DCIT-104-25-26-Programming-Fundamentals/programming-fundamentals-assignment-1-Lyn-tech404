def add_student(students):
    name = input("Student name: ")
    student_id = int(input("Student ID: "))

    number_of_scores = int(input("How many scores? "))
    scores = []

    for i in range(number_of_scores):
        score = int(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores
    }

    students.append(student)
    print(f'Student "{name}" added successfully.')

def display_students(students):
    if len(students) == 0:
        print("No students have been added yet.")
        return

    print("-" * 50)
    print("Name\t\tID\t\tScores\t\tAverage")
    print("-" * 50)

    for student in students:
        total = 0
        for score in student["scores"]:
            total += score

        average = total / len(student["scores"])

        print(f'{student["name"]}\t{student["id"]}\t{student["scores"]}\t{average:.2f}')

    print("-" * 50)

def calculate_average(students):
    student_id = int(input("Enter student ID: "))

    for student in students:
        if student["id"] == student_id:
            total = 0
            for score in student["scores"]:
                total += score

            average = total / len(student["scores"])
            print(f'{student["name"]}\'s average score: {average:.2f}')
            return

    print("Student ID not found.")

def main():
    students = []

    while True:
        print("\n================================")
        print("   STUDENT RECORD SYSTEM MENU")
        print("================================")
        print("1. Add student")
        print("2. Display all students")
        print("3. Calculate average score")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_average(students)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

main()