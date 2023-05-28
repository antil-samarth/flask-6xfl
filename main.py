from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'boot'
app.config['MYSQL_DB'] = 'test_db'

mysql = MySQL(app)

@app.route('/test', methods=['GET'])
def get_test():
    cur = mysql.connection.cursor()
    cur.execute("SELECT test_word FROM test_table")
    result = cur.fetchone()[0]
    cur.close()
    return result

if __name__ == '__main__':
    app.run(debug=True)
