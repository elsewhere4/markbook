markbook = {}

def addStudent():
    firstName = input("Enter first name: ")
    while not firstName.strip() or not isValidName(firstName):
        print("Invalid name. Please enter a valid name.")
        firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    while not lastName.strip() or not isValidName(lastName):
        print("Invalid name. Please enter a valid name.")
        lastName = input("Enter last name: ")
    studentID = input("Enter student ID (5 digits): ") 
    while not isValidStudentID(studentID):
        print("Invalid student ID. Please enter a 5 digit number.")
        studentID = input("Enter student ID (5 digits): ")
    while studentID in markbook:
        print("Student ID already exists.")
        studentID = input("Enter student ID (5 digits): ")
    markbook[studentID] = {
        'firstName': firstName,
        'lastName': lastName,   
        'marks': [],
        'grade': 'N/A'
    }

def isValidStudentID(studentID):
    return len(studentID) == 5 and studentID.isdigit() 

def isValidName(name):
    return len(name) <= 25 and name.isalpha()
    
def isValidFilename(filename):
    return all(not (not char.isalnum() and char != ' ') for char in filename) 

def addMarks():
    studentID = input("Enter student ID: ")
    if studentID not in markbook:
        print("Student ID not found.")
        return
    mark = input("Enter mark (0-100): ")
    if not mark.isdigit() or int(mark) < 0 or int(mark) > 100:
        print("Invalid mark. Please enter a mark between 0 and 100.")
        return
    markbook[studentID]['marks'].append(int(mark))
    print("Mark added successfully.")
    calculateGrade(studentID)

def calculateGrade(studentID):
    marks = markbook[studentID]['marks']
    averageMark = sum(marks) / len(marks) if marks else 0
    match averageMark:
        case mark if 90 <= mark <= 100:
            grade = 'A'
        case mark if 74 <= mark <= 89:
            grade = 'B'
        case mark if 60 <= mark <= 75:
            grade = 'C'
        case mark if 50 <= mark <= 59:
            grade = 'D'
        case mark if 0 <= mark <= 49:
            grade = 'F'
        case _:
            grade = 'N/A'
    markbook[studentID]['grade'] = grade

def displayMarkbook():
    print("{:<10} {:<15} {:<15} {:<20} {:<5}".format('Student ID', 'First Name', 
                                                     'Last Name', 'Marks', 'Grade'))
    print('-' * 65)
    for studentID, studentData in markbook.items():
        firstName = studentData['firstName']
        lastName = studentData['lastName']
        marks = ' , '.join(str(mark) for mark in studentData['marks'])
        grade = studentData['grade']
        print("{:<10} {:<15} {:<15} {:<20} {:<5}".format(studentID, firstName, lastName,
                                                         marks, grade))


def saveMarkbook():
    filename = input("Enter a name for the markbook: ")
    if not isValidFilename(filename):
        print("Invalid filename. Please enter a valid filename.")
        return
    try:
        with open(f"{filename}.txt", 'w') as file:
            for studentID, studentData in markbook.items():
                file.write(f"{studentID},{studentData['firstName']},{studentData['lastName']},{','.join(str(mark) for mark in studentData['marks'])},{studentData['grade']}\n")
        print("Markbook saved successfully.")
    except Exception as e:
        print(f"Error saving markbook: {e}")
def loadMarkbook():
        filename = input("Enter the filename you wish to load: ")
        if not isValidFilename(filename):
            print("Invalid filename. Please enter a valid filename.")
            return

        try:
            with open(f"{filename}.txt", 'r') as file:
                markbook.clear()
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 5:  
                        studentID, firstName, lastName, marksStr, grade = data
                        marks = [int(mark) for mark in marksStr.split(',') if mark]  
                        markbook[studentID] = {
                            'firstName': firstName,
                            'lastName': lastName,
                            'marks': marks,
                            'grade': grade
                        }
            print("Markbook loaded successfully.")
        except Exception as e:
            print(f"Error loading markbook: {e}")


def exitProgram():
    print("Exiting program.")

while True:
    print("\nMarkbook Hub:")
    print("1. Add a new student")
    print("2. Give marks to a student")
    print("3. Display the markbook")
    print("4. Save the markbook")
    print("5. Load the markbook")
    print("6. Exit :(")
    choice = input("Enter your choice (1-6): ")
    match choice:
        case '1':
            addStudent()
        case '2':
            addMarks()
        case '3':
            displayMarkbook()
        case '4':
            saveMarkbook()
        case '5':
            loadMarkbook()
        case '6':
            exitProgram()
            break
        case _:
            print("Invalid choice. Please select a valid option.")