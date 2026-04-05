from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 👉 DB create function
def init_db():
    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INTEGER,
            type TEXT,
            category TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# 👉 DB initialize
init_db()

# 👉 ADD API (UPDATED)
@app.route('/add', methods=['POST'])
def add_transaction():
    data = request.get_json()

    if not data.get("amount") or not data.get("type"):
        return jsonify({"error": "Missing fields"}), 400

    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transactions (amount, type, category) VALUES (?, ?, ?)",
        (data['amount'], data['type'], data.get('category'))
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Transaction added"}), 201

@app.route('/transactions',methods=['GET'])
def get_transactions():
	conn=sqlite3.connect('finance.db')
	cursor=conn.cursor()
	cursor.execute("SELECT*FROM transactions")
	rows=cursor.fetchall()
	conn.close()
	result=[]
	for row in rows:
		result.append({"id":row[0], "amount":row[1], "type":row[2], "category":row[3]})
	return jsonify(result)

@app.route('/update/<int:id>', methods=['PUT'])
def update_transaction(id):
    data = request.get_json()

    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE transactions SET amount=?, type=?, category=? WHERE id=?",
        (data['amount'], data['type'], data.get('category'), id)
    )

    conn.commit()
    conn.close()

    return jsonify({"message": "Transaction updated"})

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_transaction(id):

    conn = sqlite3.connect('finance.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM transactions WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "Transaction deleted"})

# 👉 RUN APP
if __name__ == '__main__':
    app.run(debug=True)