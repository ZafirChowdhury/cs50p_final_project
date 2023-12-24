This is my final project for CS50P and the first project that I ever did.
# CGPA calculator and grade sheet maker

#### Video Demo:  https://youtu.be/N4Mn2M27VFo

#### Description:

This program does 2 things -
1. Calculate the CGPA of a user using the provided inputs.
2. Make a grade transcript(pdf file) if the user wants.

Reasons for making this project -

1. Calculate my CGPA before my university officially publishes my grade.
Faculty members most of the time give us our grades/marks before the university.
 I used to calculate my CGPA manually, it's not hard but tedious. So I wanted to automate this process. The first part of the program takes in my old CGPA, credit completed and the courses I took and there info then calculates my GPA, new CGPA and total credit completed and prints them.

2. Make a grade transcript.
There is a 2 week delay from my university grade submission and giving an official marks sheet. I have Asian parents who want to see the grades I got as soon as possible. So the program makes a pdf of all the courses I took, their grade and my overall grade. So I can send them to my parents.

Step by step how my program works - 
- Firstly it takes the users total credit completed and CGPA witch both can be “0” or “”  if its there 1st semester.
- Then it takes in the number of courses the user did. 
- This takes in this info for each of the courses (course id, credit and grade).

    Course id can be left empty to save time where it will be replaced by placeholder course id (Course 1, Course 2 … Course n).

    Grades can be given in 3 ways , Grade - “A”, Grade Point - “4” or Marks - “95”.
    Where the program will convert them to calculate/print out as pdf. It is converted according to my university's grading system.

- Then the program asks the user if they want a pdf or not. 

- If the user says no, Program prints out users -
    GPA: 
    Credit passed:

    CGPA:
    Total Credit passed:

- If the user says yes, Program then will ask for the users name and student id then make a pdf using FPDF with users' grades. If name and id is left empty it  will make a pdf with my name and id.
