class OnlineCourse:
    def __init__(self, course, instructor):
        self.course = course
        self.instructor = instructor
        self.students = []
        

    def enroll_students(self, name):
        self.students.append(name)
        print(f"{name} has been enrolled in the course")
    def course_details(self):
        print(f'Course: {self.course}')
        print(f'Instructor: {self.instructor}')
        print(f'Enrolled students: {', '.join(self.students)}')


    def completed_course(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f'{name} has completed the course!')
        else:
            print(f'{name} is not a part of this course')

    def average_grades(self, grades):
        total = sum(grades)
        average = total / len(grades)
        print(f'The average grade is {average}')



course_input = input("Enter a course: ").lower()
name = input("Enter an instructor: ").lower()
student = input("Enter a name: ").lower()


course = OnlineCourse(course_input, name)
grades = [90,75,80,20,40]

course.average_grades(grades)
course.enroll_students(student)
course.course_details()