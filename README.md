# Finance_Tracker
💰 Expense Tracker App

An Expense Tracking Web Application built with Python Django REST Framework (DRF) and HTML templates.
The app helps users manage their finances by tracking transactions, setting financial goals, and monitoring progress.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

🚀 Features

  🔑 Authentication

      User Registration
      
      Login & Logout
  
  📊 Dashboard
  
      Overview of income, expenses, and savings
      
      Visual representation of transactions
  
  ➕ Add Transaction
  
      Record income or expense
      
      Add categories for better tracking
  
  📜 All Transactions
  
      View list of all past transactions
      
      Filter and search functionality

  🎯 Set Target
  
      Define savings/expense goals
      
      Monitor progress toward financial goals
  --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Backend: Python, Django, Django REST Framework (DRF)
  
  Frontend: HTML, CSS, JavaScript (with Django Templates)
  
  Database: SQLite (default)
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⚡ Setup Instructions

  Clone the repository

    git clone https://github.com/your-username/expense-tracker.git
    cd Expense


Create & activate virtual environment

    python -m venv venv
    source venv/bin/activate   # for Linux/Mac
    venv\Scripts\activate      # for Windows


Install dependencies

    pip install -r requirements.txt


Run migrations

    python manage.py migrate


Create a superuser (Admin Panel)

    python manage.py createsuperuser


Start development server

    python manage.py runserver
