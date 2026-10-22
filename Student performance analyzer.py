import json

def get_score(subject):
    while True:
        try:
            score = int(input("enter " + subject + " score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100")
        except ValueError:
            print("Please enter a number")

# Load existing students first
try:
    with open("student.json", "r") as file:
        students = json.load(file)
except:
    students = []

while True:
    print("\n1. Add new student")
    print("2. view all students")
    print("3. search for a student")
    print("4. view class statistics")
    print("5. Exit")
    choice = input("select an option: ")
    
    if choice == "5":
        print("Goodbye bro")
        break

    elif choice == "1":
        name = input("enter student name:")
        student_id = input("enter student ID:")
        math = get_score("math")
        physics = get_score("physics")
        python = get_score("python")
        scores = [math, physics, python]
        avg = round(sum(scores) / len(scores), 2)

        if avg >= 70:
            grade = "A"
            status = "excellent"
        elif avg >= 60:
            grade = "B"
            status = "very good"
        elif avg >= 50:
            grade = "C"
            status = "good"
        elif avg >= 40:
            grade = "D"
            status = "pass"
        else:
            grade = "F"
            status = "fail"

        student = {"name": name, "id": student_id, "scores": scores, "average": avg, "grade": grade, "status": status}
        students.append(student)

        try:
            with open("student.txt", "a") as file:
                file.write(f"{name}, {student_id}, {math}, {physics}, {python}, {avg}\n")
        except:
            print("something went wrong")

        try:
            with open("student.json", "w") as file:
                json.dump(students, file)
        except:
            print("something went wrong")

        print("Average:", avg)
        print("Grade:", grade)
        print("Status:", status)

    elif choice == "2":
        for student in students:
            print("name:", student["name"])
            print("id:", student["id"])
            print("scores:", student["scores"])
            print("average:", student["average"])
            print("grade:", student["grade"])
            print("status:", student["status"])
            print("---")

    elif choice == "3":
        search_id = input("Enter student id :")
        found = False
        for student in students:
            if student["id"] == search_id:
                print(student)
                found = True
                break
        if not found:
            print("student hasnt been stored")

    elif choice == "4":
        if len(students) == 0:
            print("No students yet")
        else:
            total_avg = sum(s["average"] for s in students) / len(students)
            print(f"Total students: {len(students)}")
            print(f"Class average: {round(total_avg, 2)}")