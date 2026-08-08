# Student Performance Analyzer

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input(f"\nEnter name of student {i + 1}: ")

    math = float(input("Enter Math marks: "))
    python = float(input("Enter Python marks: "))
    sql = float(input("Enter SQL marks: "))

    total = math + python + sql
    percentage = total / 3

    # Grade calculation
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    # Pass/Fail
    if math >= 40 and python >= 40 and sql >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    students[name] = {
        "Math": math,
        "Python": python,
        "SQL": sql,
        "Total": total,
        "Percentage": percentage,
        "Grade": grade,
        "Result": result
    }


# Display results
print("\n========== STUDENT RESULTS ==========")

for name, data in students.items():
    print(f"\nStudent: {name}")
    print(f"Math: {data['Math']}")
    print(f"Python: {data['Python']}")
    print(f"SQL: {data['SQL']}")
    print(f"Total: {data['Total']}")
    print(f"Percentage: {data['Percentage']:.2f}%")
    print(f"Grade: {data['Grade']}")
    print(f"Result: {data['Result']}")


# Find topper
highest_percentage = 0
topper = ""

for name, data in students.items():
    if data["Percentage"] > highest_percentage:
        highest_percentage = data["Percentage"]
        topper = name

print("\n========== TOPPER ==========")
print("Topper:", topper)
print("Percentage:", highest_percentage)


# Class average
average = sum(
    student["Percentage"] for student in students.values()
) / len(students)

print("\nClass Average:", round(average, 2), "%")
