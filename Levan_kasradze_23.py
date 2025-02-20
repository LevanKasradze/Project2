
def calculate_average(grades):
    return sum(grades) / len(grades)
def is_passing(average):

        return average >= 70
def grade_to_letter(average):
    if 91 <= average <= 100:
        return "A"
    elif 81 <= average <= 90:
        return "B"
    elif 71 <= average <= 80:
        return "C"
    elif 61 <= average <= 70:
        return "D"
    else:
        return "F"

class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.grades = []
    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)

    def get_final_grade(self):
        if len(self.grades) == 0:
            return None
        return sum(self.grades) / len(self.grades)



class Student:
    def __init__(self, name):
        self.name = name
        self.courses = {}

    def add_course(self, course_name, credits):
        self.courses[course_name] = Course(course_name, credits)
    def remove_course(self, course_name):
        if course_name in self.courses:
            del self.courses[course_name]

    def get_gpa(self):
        total_credits = sum(course.credits for course in self.courses.values())
        total_grades = sum(course.get_final_grade() * course.credits for course in self.courses.values() if course.get_final_grade() is not None)
        return total_grades / total_credits if total_credits > 0 else 0
    def get_transcript(self):
        transcript = f"Transcript for {self.name}:\n"
        for course in self.courses.values():
            final_grade = course.get_final_grade()
            grade_letter = grade_to_letter(final_grade) if final_grade is not None else "No Grade"
            transcript += f"{course.name}: {final_grade if final_grade is not None else 'N/A'} ({grade_letter})\n"
        return transcript
student = Student("Levani")
student.add_course("Mathematics", 10)
student.add_course("History", 5)
student.courses["Mathematics"].add_grade(85)
student.courses["Mathematics"].add_grade(90)
student.courses["History"].add_grade(78)
student.courses["History"].add_grade(82)
gpa = student.get_gpa()
print(f"GPA: {gpa:.2f}")
print(student.get_transcript())
