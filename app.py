from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():
    try:
        connection = psycopg2.connect(user="",
                                      password="",
                                      host="127.0.0.1",
                                      port="5432",
                                      database="tododb")

        cursor = connection.cursor()
        postgreSQL_select_Query = "select * from account"

        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from account table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        print("Print each row and it's columns values")
        for row in mobile_records:
            print("User Id = ", row[0],)
            print("Username = ", row[1])
            print("Password  = ", row[2], "\n")



    except (Exception, psycopg2.Error) as error:
        print ("Error while connecting to PostgreSQL", error)
    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    return "Hello world"


if __name__ == '__main__':
    app.run()



