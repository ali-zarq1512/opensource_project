def input_students():
    """Inputs student information and returns a list of dictionaries."""
    students = []
    for _ in range(5):
        student = {}
        student['Student ID'] = input("Student ID: ")  # Store ID as string to match output format
        student['Name'] = input("Name: ")
        student['English'] = int(input("English: "))
        student['C-Language'] = int(input("C-Language: "))
        student['Python'] = int(input("Python: "))
        students.append(student)
    return students


def calculate_total_average(students):
    """Calculates total score and average for each student."""
    for student in students:
        total_score = student['English'] + student['C-Language'] + student['Python']
        average = total_score / 3
        student['Total Score'] = total_score
        student['Average'] = average


def calculate_grade(students):
    """Calculates the grade for each student based on their average."""
    for student in students:
        average = student['Average']
        if average >= 90:
            grade = 'A'
        elif average >= 80:
            grade = 'B+'
        elif average >= 70:
            grade = 'C'
        elif average >= 60:
            grade = 'D'
        else:
            grade = 'F'
        student['Grade'] = grade


def calculate_rank(students):
    """Calculates and assigns ranks to students based on their total scores using insertion sort."""
    n = len(students)

    # Insertion Sort (sort in descending order based on Total Score)
    for i in range(1, n):
        key = students[i]
        j = i - 1
        while j >= 0 and key['Total Score'] > students[j]['Total Score']:
            students[j + 1] = students[j]
            j -= 1
        students[j + 1] = key

    # Assign Ranks
    rank = 1
    previous_score = None
    same_rank_count = 1

    for i, student in enumerate(students):
        if student['Total Score'] != previous_score:
            student['Rank'] = rank
            previous_score = student['Total Score']
            rank += same_rank_count
            same_rank_count = 1
        else:
            student['Rank'] = rank - 1  # Same rank as previous student
            same_rank_count += 1


def print_students(students):
    """Prints the student information in a formatted table."""
    print("\t\t\t\t\t\t\t Student Grade Management Program")
    print("=" * 90)
    print("{:<15} {:<15} {:<8} {:<8} {:<8} {:<8} {:<8} {:<8} {:<5}".format(
        "Student ID", "Name", "English", "C-Lang", "Python", "Total", "Avg", "Grade", "Rank"))
    print("=" * 90)

    for student in students:
        print("{:<15} {:<15} {:<8} {:<8} {:<8} {:<8} {:<8.2f} {:<8} {:<5}".format(
            student['Student ID'], student['Name'], student['English'], student['C-Language'],
            student['Python'], student['Total Score'], student['Average'], student['Grade'],
            student['Rank']))


def main():
    """Main function to execute the program."""
    students = input_students()
    calculate_total_average(students)
    calculate_grade(students)
    calculate_rank(students) # Ranks assigned during sorting now
    print_students(students)


if __name__ == "__main__":
    main()