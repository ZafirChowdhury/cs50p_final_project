import project

def test_grade_convert():
    assert project.grade_convert("A-") == 3.7
    assert project.grade_convert(3.7) == "A-"
    assert project.grade_convert("a-".upper()) == 3.7


def test_number_to_grade():
    assert project.number_to_grade(int(69)) == ("C+", 2.3)
    assert project.number_to_grade(int(420)) == (None, None)
    assert project.number_to_grade(int(89)) == ("A-", 3.7)


def test_cal_gpa():
    assert project.cal_gpa([4, 3, 3], [4.0, 4.0, 3.0]) == 3.7


def test_cal_cgpa():
    assert project.cal_cgpa(3.73, 42, 3.7, 10) == 3.72


def test_make_grade_book():
    course_id = ["ENG101", "ENG102", "ENG105"]
    credit_per_course = [3, 3, 3]
    grade = ["A-", "A", "A-"]
    result = [
        ["Course ID", "Credit", "Grade"],
        ["ENG101", 3, "A-"],
        ["ENG102", 3, "A"],
        ["ENG105", 3, "A-"]
    ]
    
    assert project.make_grade_book(course_id, credit_per_course, grade) == result
