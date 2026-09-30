def getLetterGrade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def main():
    name = input("Enter student name: ")

    grades = []

    grades.append(float(input("Enter grade: ")))
    grades.append(float(input("Enter grade: ")))
    grades.append(float(input("Enter grade: ")))
    grades.append(float(input("Enter grade: ")))
    grades.append(float(input("Enter grade: ")))

    average = sum(grades) / len(grades)

    letterGrade = getLetterGrade(average)

    print()
    print(name)
    print()
    print(f"Average: {average:.1f}")
    print(f"Letter Grade: {letterGrade}")


main()