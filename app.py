from flask import Flask, jsonify
import pyodbc
import datetime

app = Flask(__name__)

conn = pyodbc.connect(
    # 'DRIVER={FreeTDS};SERVER=202.44.72.201;DATABASE=databasename;UID=username;PWD=123456789;PORT=1433')
    'DSN=DSN_NAME;UID=username;PWD=123456789;PORT=1433')

cursor = conn.cursor()
select_string = "SELECT * FROM dbo.person where name1 like 'สุรพงษ์'"
cursor.execute(select_string)
data = []
while True:
    row = cursor.fetchone()
    # for i in row:
    #     print(row)
    temp = {}

    if not row:
        break
    temp = list(row)
    data.append(temp)

# print(data)

# t = datetime.datetime(2013, 6, 18, 14, 16, 37, 860000)
# print(t)

conn.close()

@app.route('/')
def main():
    return jsonify(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)