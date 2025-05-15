import mysql.connector

connection = mysql.connector.connect(user='ericl160',
                                     password='REDACTED',
                                     host='10.8.37.226',
                                     database='ericl160_db')

cursor = connection.cursor()

student_id = input("Enter a student_id number: ")
query = f"CALL Student_Info({student_id})"

cursor.execute(query)

for row in cursor:
    period, course, room, teacher = row[:4]
    print(f"Period: {period}\nCourse: {course}\nRoom: {room}\nTeacher: {teacher}\n")

cursor.close()
connection.close()
