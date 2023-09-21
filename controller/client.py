import sys

sys.path.insert(1, 'service')

import connectpostgres as con

# Function Insert to table person
def insert(fullname, email, age):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "INSERT INTO person (fullname, email, age) VALUES (%s, %s, %s)"
    cursor.execute(sql, (fullname, email, age))
    conn.commit()
    cursor.close()

# Function Select all data from table person
def select_all():
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "SELECT * FROM person"
    cursor.execute(sql)
    result = cursor.fetchall()
    rows = [['ID', 'Fullname', 'Email', 'Age', 'Date']]
    for data in result:
        rows.append(data)
    cursor.close()
    return rows

# Function Select data by id from table person
def select_by_id(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "SELECT * FROM person WHERE id = %s"
    cursor.execute(sql, (id,))
    result = cursor.fetchall()
    rows = [['ID', 'Fullname', 'Email', 'Age', 'Date']]
    for data in result:
        rows.append(data)
    cursor.close()
    return rows

# Function Update data by id from table person
def update(id, fullname, email, age):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "UPDATE person SET fullname = %s, email = %s, age = %s WHERE id = %s"
    cursor.execute(sql, (fullname, email, age, id))
    conn.commit()
    cursor.close()

# Function Delete data by id from table person
def delete(id):
    conn = con.connectdb()
    cursor = conn.cursor()
    sql = "DELETE FROM person WHERE id = %s"
    cursor.execute(sql, (id,))
    conn.commit()
    cursor.close()