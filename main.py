import mysql.connector
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.pooling import PooledMySQLConnection


def get_database_connection() -> PooledMySQLConnection | MySQLConnectionAbstract:
    connection = mysql.connector.connect(user='ericl160',
                                         password='222924870',
                                         host='10.8.37.226',
                                         database='ericl160_db')
    return connection


def execute_statement(connection: PooledMySQLConnection | MySQLConnectionAbstract, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    results = []

    for r in cursor:
        results.append(r)

    cursor.close()
    connection.close()
    return results


def get_student_schedule(student_id):
    query = f"CALL Student_Info({student_id})"
    return execute_statement(get_database_connection(), query)


student_id = input("Enter a student_id number: ")
output = get_student_schedule(student_id)

print()
for row in output:
    period, course, room, teacher = row[:4]
    print(f"Period: {period}\nCourse: {course}\nRoom: {room}\nTeacher: {teacher}\n")
