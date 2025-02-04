class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"Hi, my name is: " + self.getName()
    
    def getName(self):
        return self.name

    def getAddress(self):
        return self.address
    
    def setAddress(self, newAddress):
        self.address = newAddress


class Student(Person):
    def __init__(self, name, address, numCourses, courses = [], grades = []):
        Person.__init__(self, name, address)
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades

    def __str__(self):
        return "Hi, my name is " + self.getName() + ", I am a student here at DSU."

    def addCourseGrade(self, courseName, grade):
        newClass = True
        for i in range(len(self.courses)):
            if self.courses[i] == courseName:
                self.grades[i] = grade
                newClass = False
                break
        if newClass:
            self.courses.append(courseName)
            self.grades.append(grade)
            self.numCourses += 1

    def printGrades(self):
        print("Your grades: ")
        for i in range(len(self.courses)):
            print(self.courses[i], end='\t')
            print(self.grades[i])
        print()

    def getAverageGrades(self):
        averageGrade = 0
        for i in range(len(self.grades)):
            averageGrade += self.grades[i]
        return round(averageGrade / self.numCourses, 2)


class Teacher(Person):
    def __init__(self, name, address, numCourses, courses = []):
        Person.__init__(self, name, address)
        self.numCourses = numCourses
        self.courses = courses

    def __str__(self):
        return "Hi, my name is Dr." + self.getName() + ", I am a professor here at DSU."
    
    def addCourse(self, courseName):
        if courseName not in self.courses:
            self.numCourses += 1
            self.courses.append(courseName)
            return True
        return False
        

    def removeCourse(self, courseName):
        amountOfCourses = self.numCourses
        courses = []
        for course in self.courses:
            if course != courseName:
                courses.append(course)
        self.courses = courses
        self.numCourses = len(courses)

        return amountOfCourses != self.numCourses 
        

class Course:
    def __init__(self, courseName, professor, students = []):
        self.courseName = courseName
        self.students = students
        self.professor = professor

    def changeProfessor(self, professor):
        self.professor = professor

    def addStudent(self, student):
            self.students.append(student)
    
    def __str__(self):
        return ("There are currently " + str(len(self.students)) 
        + " students taking " + self.courseName)


class Program:
    def __init__(self, programName, director, courses = []):
        self.programName = programName
        self.courses = courses
        self.director = director

    def addCourse(self, courseName):
        self.courses.append(courseName)

    def changeDirector(self, newDirector):
        self.director = newDirector

    def __str__(self):
        result = ("The " + self.programName 
            + " program consist of the following courses: ")
        
        for i in range(len(self.courses)):
            result += self.courses[i] + ", "
        result = result[:-2]
        return result



student1 = Student("Louis", "333 berkeley road", 4, ["Introduction to c++", "Computer networking"], [100, 97])
print()
print(student1)
student1.addCourseGrade("History", 75)
student1.addCourseGrade("Computer networking", 98)
print(student1.getName() + " average grade is: " + str(student1.getAverageGrades()))
print()

professor1 = Teacher("Smolinski", "554 kerby way", 3, ["English", "Stochastic", "Introduction to c++"])
professor1.addCourse("Computational Thinking II")
professor1.removeCourse("English")
print(professor1)
print()


studentValery = Student("Valery", "539 blue street wy", 4, ["Introduction to c++"], [95])
studentTom = Student("Tom", "220 Peachtree run, Dover, DE", 4, ["Introduction to c++"], [80])
studentKlay = Student("Klay", "935 queensland st, Queens", 4, ["Introduction to c++", "Algebra 1"], [92, 80])
course1 = Course(courseName='introduction_to_cpp', professor="Dr. Smolinski", students=[studentValery, studentTom, studentKlay])
print(course1)
print()

ComputerScienceProgram = Program("Computer Science", "Dr. Rasamny", ["computer networking", "computational thinking", "cs capstone"])
ComputerScienceProgram.addCourse("c++")
print(ComputerScienceProgram)
print()