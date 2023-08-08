from fpdf import FPDF
import datetime


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln()

    def chapter_body(self, header, data):
        # Set font and background color for table header
        self.set_font('Arial', 'B', 10)
        self.set_fill_color(200, 200, 200)
        self.ln()

        # Table header
        for item in header:
            self.cell(40, 10, str(item), 1, 0, 'C', True)
        self.ln()
        
        # Set font and background color for table rows
        self.set_font('Arial', '', 10)
        self.set_fill_color(255, 255, 255)
        
        # Table data
        for row in data:
            for item in row:
                self.cell(40, 10, str(item), 1, 0, 'C', True)
            self.ln()
    
    def add_table(self, header, data, table_name):
        self.chapter_title(table_name)
        self.chapter_body(header, data)


def main():    
    credit_completed = input("Done credits: ")
    if credit_completed == "" or credit_completed[-1] == "0":
        credit_completed = 0
    else:
        while True:
            try:
                credit_completed = int(credit_completed)
                break
            except ValueError:
                pass

    if credit_completed == 0:
        cgpa = 0
    else:
        cgpa = taking_flaot("CGPA: ")
    

    number_of_course_taken = taking_int("Number of Course taken: ")

    
    course_id = []
    credit_per_course = []
    grade = []
    grade_point = []

    c_id_count = 1
    for _ in range(number_of_course_taken):
        
        c_id = input("Course ID: ").strip().upper()
        if c_id:
            course_id.append(c_id)
        else:
            course_id.append(f"Course {c_id_count}")
            c_id_count = c_id_count + 1

        credit = taking_int("Credit: ")
        credit_per_course.append(credit)

        while True:
            grade_temp, grade_point_temp = take_grade()
            if grade_temp is None or grade_point_temp is None:
                pass
            else:
                break
        grade.append(grade_temp)
        grade_point.append(grade_point_temp)

    if "W" in grade:
        for i in range(len(grade)):
            if grade[i] == "W":
                credit_per_course[i] = 0
    
    gpa = cal_gpa(credit_per_course, grade_point)
    cgpa = cal_cgpa(cgpa, credit_completed, gpa, sum(credit_per_course))
    done_credit = sum(credit_per_course) + credit_completed

    if "F" in grade:
        gpa = 0



    pdf_flag = input("Do you  want a pdf? (yes/no) ").strip().upper()
    
    if pdf_flag == "NO":
        print()
        print("Results - ")
        print("GPA: ",gpa)
        print("Credit passed: ", sum(credit_per_course))
        print()

        print("Cumulative Results - ")
        print("CGPA: ",cgpa)
        print("Total credit passed: ",done_credit)
        print()
    
    else:
        name = input("Name: ").strip()
        if not name:
            name = "Zafir Chowdhury"
        
        id = input("ID: ").strip()
        if not id:
            id = "2111652"
        
        semester = input("Semester: ").strip()

        grade_book = make_grade_book(course_id, credit_per_course, grade)

        date = datetime.date.today()

        make_pdf(date, name, id, semester, grade_book, gpa, sum(credit_per_course), cgpa, done_credit)


def make_grade_book(course_id, credit_per_course, grade):
    grade_book = [["Course ID", "Credit", "Grade"]]

    for i in range(len(course_id)):
        grade_book.append([course_id[i], credit_per_course[i], grade[i]])

    return grade_book


def make_pdf(date, name, id, semester, grade_book, gpa, crdit_done, cgpa, total_credit_done, table_name=""):
    pdf = PDF()
    pdf.add_page()

    pdf.cell(10, 10, f"Date: {date}.", ln=1)
    pdf.cell(10, 10, f"Name: {name}.", ln=1)
    pdf.cell(10, 10, f"ID: {id}", ln=1)
    pdf.cell(10, 10, f"{semester}", ln=1)

    pdf.add_table(grade_book[0], grade_book[1:], table_name)

    pdf.cell(10, 10, f"GPA: {gpa}", ln=1)
    pdf.cell(10, 10, f"Credit passed: {crdit_done}", ln=1)
    pdf.cell(10, 10, f"CGPA: {cgpa}", ln=1)
    pdf.cell(10, 10, f"Total credit done: {total_credit_done}")

    pdf.output(f"{id}.pdf")

    print("PDF made successfully")


def take_grade():
    while True:
        try:
            temp = input("Grade: ")
            if temp.upper() == "W":
                return "W", 0.0
            
            elif "." in temp and temp in ["4.0", "3.7", "3.3", "3.0", "2.7", "2.3", "2.0", "1.7", "1.3", "1.0", "0.0", "0"]:
                grade_point = float(temp)
                grade = grade_convert(grade_point)
                return grade, grade_point
            
            elif temp.upper() in ["A", "A-", "B+", "B", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F", "W"]:
                grade = temp
                grade_point = grade_convert(grade.upper())
                return grade, grade_point

            elif temp.isalnum():
                return number_to_grade(int(temp))
        
        except ValueError:
            pass


def grade_convert(grade):
    grade_dic = {
        "A" : 4.0,
        "A-" : 3.7,
        "B+" : 3.3,
        "B" : 3.0,
        "B-" : 2.7,
        "C+" : 2.3,
        "C" : 2.0,
        "C-" : 1.7,
        "D" : 1.0,
        "D+" : 1.3,
        "D" : 1.0,
        "F" : 0.0, 
        4.0: 'A', 
        3.7: 'A-', 
        3.3: 'B+', 
        3.0: 'B', 
        2.7: 'B-', 
        2.3: 'C+', 
        2.0: 'C', 
        1.7: 'C-', 
        1.0: 'D', 
        1.3: 'D+', 
        0.0: 'F'     
    }

    return grade_dic.get(grade, None)


def number_to_grade(n):
    if 90 <= n <= 100:
        return "A", 4.0

    elif 85 <= n <= 89:
        return "A-", 3.7

    elif 80 <= n <= 84:
        return "B+", 3.3
    
    elif 75 <= n <= 79:
        return "B", 3.0
    
    elif 70 <= n <= 74:
        return "B-", 2.7
    
    elif 65 <= n <= 69:
        return "C+", 2.3
    
    elif 60 <= n <= 64:
        return "C", 2.0
    
    elif 55 <= n <= 59:
        return "C-", 1.7
    
    elif 50 <= n <= 54:
        return "D+", 1.3
    
    elif 45 <= n <= 49:
        return "D", 1.0
    
    elif 00 <= n <= 44:
        return "F", 0.0
    
    else:
        return None, None
    

def taking_int(s):
    while True:
        try:
            i = int(input(s))
            return i
        except ValueError:
            pass


def taking_flaot(s):
    while True:
        try:
            f = float(input(s))
            return f
        except ValueError:
            pass


def cal_gpa(credit, grade_point):
    total_credit = sum(credit) 
    total_gpa = 0
    
    for i in range(len(credit)):
        total_gpa = total_gpa + (credit[i] * grade_point[i])

    return round(total_gpa/total_credit, 2)
    

def cal_cgpa(cgpa, done_credit, gpa, credit):
    total_done_credit = done_credit + credit

    return round(((cgpa*done_credit) + (gpa*credit)) / total_done_credit, 2)


if __name__ == "__main__":
    main()    
