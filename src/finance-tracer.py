import sqlite3

#connect to the database
conn = sqlite3.connect('finance.db')
c = connect.cursor()

#execute commands to create tables for database

""" Tables needed include:
date TEXT, amount REAL,  Category TEXT, type TEXT, description TEXT"""

