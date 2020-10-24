import psycopg2


def main():
    conn = psycopg2.connect("host='ec2-52-72-34-184.compute-1.amazonaws.com' port='5432' dbname='dcqsqk92pdhf6o' user='ugpndzjemldrwf' password='5f52b1ba3113ab3af88a8124423e664a3559fbe43b5b071acd88f430e12b8b0f'")
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