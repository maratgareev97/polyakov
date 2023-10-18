import connect


def cret():
    connection = connect.con()
    cursor = connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS table2 (id int NOT NULL AUTO_INCREMENT, name text, phone text, description text, PRIMARY KEY (id));")
    connection.commit()
    cursor.close()
    connection.close()


def ins():
    connection = connect.con()

    cursor = connection.cursor()
    cursor.execute("insert into table2 (name, phone, description) VALUES (1,2,3)")
    connection.commit()
    cursor.close()
    connection.close()


def allSelect():
    connection = connect.con()

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM table2")
    result = cursor.fetchall()  # в виде строки
    cursor.close()
    connection.close()
    # for i in result:
    #     print(i)
    return result


def deleteById(id):
    connection = connect.con()
    cursor = connection.cursor()
    cursor.execute("""DELETE FROM table2 WHERE id=%s""", (id))
    connection.commit()

    cursor.close()
    connection.close()

# cret()
# ins()
# allSelect()
