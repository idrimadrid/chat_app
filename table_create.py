import psycopg2


def main():
    conn = psycopg2.connect("host='localhost' dbname='chat_db' user='postgres' password='admin'")
    cursor = conn.cursor()

    TABLES = {}
    TABLES['clients'] = (
        "CREATE TABLE clients("
        "Id SERIAL PRIMARY KEY NOT NULL,"
        "UserName VARCHAR(20) UNIQUE NOT NULL,"
        "Password VARCHAR (20) NOT NULL,"
        "CreateDate DATE)")

    TABLES['messages'] = (
        "CREATE TABLE messages("
        "Id SERIAL PRIMARY KEY NOT NULL,"
        "UserName VARCHAR(20),"
        "Messages VARCHAR(200),"
        "CreateDate DATE)")


    for name, ddl in TABLES.items():
            print("Creating table {}: ".format(name), end='')
            cursor.execute(ddl)

    conn.commit()
if __name__ == '__main__':
    main()