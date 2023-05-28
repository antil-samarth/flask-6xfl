import mysql.connector
from flask import Flask
from dotenv import load_dotenv
import os

app = Flask(__name__)

mydb = mysql.connector.connect(
	host=os.getenv('MYSQLHOST'),
	port=os.getenv('MYSQLPORT'),
	database=os.getenv('MYSQLDATABASE'),
 	user=os.getenv('MYSQLUSER'),
 	password=os.getenv('MYSQLPASSWORD')
)

@app.route('/test', methods=['GET'])
def get_test():
    cur = mydb.cursor()
    cur.execute("SELECT test_word FROM test_table")
    result = cur.fetchone()[0]
    cur.close()
    return result

@app.route('/admin', methods=['POST'])
def update_test():
    new_word = request.form['new_word']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE test_table SET test_word = %s", (new_word,))
    mysql.connection.commit()
    cur.close()
    return 'Word updated successfully'

if __name__ == '__main__':
    app.run(debug=True)


