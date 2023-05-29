from main import app, mydb

def test_get_test():
    with app.test_client() as client:
        response = client.get('/test')
        assert response.status_code == 200
        assert response.data == b'test'

def test_update_test():
    with app.test_client() as client:
        response = client.post('/admin', data={'new_word': 'new_test'})
        assert response.status_code == 200
        assert response.data == b'Word updated successfully'

        cur = mydb.cursor()
        cur.execute("SELECT test_word FROM test_table")
        result = cur.fetchone()[0]
        cur.close()
        assert result == 'new_test'

def test_reset_test_word():
    cur = mydb.cursor()
    cur.execute("UPDATE test_table SET test_word = 'test'")
    mydb.commit()
    cur.close()