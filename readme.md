# **Personal Finance Tracker API**



## **Description**



This is a backend project built using Flask and SQLite.

It allows users to add, view, update, and delete financial transactions.



#### Features



* Add new transaction
* View all transactions
* Update transaction
* Delete transaction
* Data stored in SQLite database



#### Technologies Used



* Python
* Flask
* SQLite
* Postman



#### How to Run

1. Open project folder in CMD
2. Activate virtual environment
3. Run: python app.py
4. Open Postman and test APIs



#### API Endpoints



* POST /add → Add transaction
* GET /transactions → View all transactions
* PUT /update/<id> → Update transaction
* DELETE /delete/<id> → Delete transaction



#### Sample Request

#### 

{

"amount": 2000,

"type": "income",

"category": "salary"

}



#### Sample Response



{

"message": "Transaction added"

}

