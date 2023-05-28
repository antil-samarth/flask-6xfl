import mysql.connector
from flask import Flask
from dotenv import load_dotenv

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

if __name__ == '__main__':
    app.run(debug=True)
