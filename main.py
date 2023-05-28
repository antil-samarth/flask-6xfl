import mysql.connector
from flask import Flask

app = Flask(__name__)

mydb = mysql.connector.connect(
  host=MYSQLHOST,
  user=MYSQLUSER,
  password=MYSQLPASSWORD,
  database=MYSQLDATABASE,
  port=MYSQLPORT
)

@app.route('/test', methods=['GET'])
def get_test():
    cur = mydb.cursor()
    cur.execute("SELECT test_word FROM test_table")
    result = cur.fetchone()[0]
    cur.close()
    return result

if __name__ == '__main__':
    app.run(debug=True)
