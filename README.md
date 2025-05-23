
Project Description

This project focuses on mastering Python decorators to enhance database operations in Python applications. Through hands-on tasks, learners will create custom decorators to log queries, handle connections, manage transactions, retry failed operations, and cache query results. The tasks are designed to simulate real-world challenges, providing learners with an in-depth understanding of Python’s capabilities for dynamic and reusable code in database management.
Learning Objectives

By completing these tasks, professional developers will:

    Deepen their knowledge of Python decorators and how they can be used to create reusable, efficient, and clean code.
    Enhance database management skills by automating repetitive tasks like connection handling, logging, and caching.
    Implement robust transaction management techniques to ensure data integrity and handle errors gracefully.
    Optimize database queries by leveraging caching mechanisms to reduce redundant calls.
    Build resilience into database operations by implementing retry mechanisms for transient errors.
    Apply best practices in database interaction for scalable and maintainable Python applications.

Requirements

    Python 3.8 or higher installed.
    SQLite3 database setup with a users table for testing.
    A working knowledge of Python decorators and database operations.
    Familiarity with Git and GitHub for project submission.
    Strong problem-solving skills and attention to detail.

Key Highlights

    Task 0: Logging Database Queries
        Create a decorator to log all SQL queries executed by a function.
        Learn to intercept function calls to enhance observability.

    Task 1: Handle Database Connections with a Decorator
        Automate database connection handling with a decorator.
        Eliminate boilerplate code for opening and closing connections.

    Task 2: Transaction Management Decorator
        Implement a decorator to manage database transactions (commit/rollback).
        Ensure robust error handling and data consistency.

    Task 3: Retry Database Queries
        Build a decorator to retry database operations on failure.
        Introduce resilience against transient database issues.

    Task 4: Cache Database Queries
        Implement a decorator to cache query results.
        Optimize performance by avoiding redundant database calls.

Tasks
0. Logging database Queries
mandatory

Objective: create a decorator that logs database queries executed by any function

Instructions:

    Complete the code below by writing a decorator log_queries that logs the SQL query before executing it.

    Prototype: def log_queries()

import sqlite3
import functools

#### decorator to lof SQL queries

 """ YOUR CODE GOES HERE"""

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")

Repo:

    GitHub repository: alx-backend-python
    Directory: python-decorators-0x01
    File: 0-log_queries.py

1. Handle Database Connections with a Decorator
mandatory

Objective: create a decorator that automatically handles opening and closing database connections

Instructions:

    Complete the script below by Implementing a decorator with_db_connection that opens a database connection, passes it to the function and closes it afterword

import sqlite3 
import functools

def with_db_connection(func):
    """ your code goes here""" 

@with_db_connection 
def get_user_by_id(conn, user_id): 
cursor = conn.cursor() 
cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,)) 
return cursor.fetchone() 
#### Fetch user by ID with automatic connection handling 

user = get_user_by_id(user_id=1)
print(user)

Repo:

    GitHub repository: alx-backend-python
    Directory: python-decorators-0x01
    File: 1-with_db_connection.py

2. Transaction Management Decorator
mandatory

Objective: create a decorator that manages database transactions by automatically committing or rolling back changes

Instructions:

    Complete the script below by writing a decorator transactional(func) that ensures a function running a database operation is wrapped inside a transaction.If the function raises an error, rollback; otherwise commit the transaction.

    Copy the with_db_connection created in the previous task into the script

import sqlite3 
import functools

"""your code goes here"""

@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
cursor = conn.cursor() 
cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')

Repo:

    GitHub repository: alx-backend-python
    Directory: python-decorators-0x01
    File: 2-transactional.py

3. Using Decorators to retry database queries
mandatory

Objective: create a decorator that retries database operations if they fail due to transient errors

Instructions:

    Complete the script below by implementing a retry_on_failure(retries=3, delay=2) decorator that retries the function of a certain number of times if it raises an exception

import time
import sqlite3 
import functools

#### paste your with_db_decorator here

""" your code goes here"""

@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)

Repo:

    GitHub repository: alx-backend-python
    Directory: python-decorators-0x01
    File: 3-retry_on_failure.py

4. Using decorators to cache Database Queries
mandatory

Objective: create a decorator that caches the results of a database queries inorder to avoid redundant calls

Instructions:

    Complete the code below by implementing a decorator cache_query(func) that caches query results based on the SQL query string

import time
import sqlite3 
import functools


query_cache = {}

"""your code goes here"""

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

#### Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")

Repo:

    GitHub repository: alx-backend-python
    Directory: python-decorators-0x01
    File: 4-cache_query.py

5. Manual Review
mandatory

Repo:

    GitHub repository: alx-backend-python
    Directory: python-decorators-0x01

//END of task 

//Start of another task

Context Managers and Asynchronous programming in python
 Novice
 Weight: 1
 Project will start May 19, 2025 12:00 AM, must end by May 26, 2025 12:00 AM
 Checker was released at May 19, 2025 12:00 AM
 Manual QA review must be done (request it when you are done with the project)
 An auto review will be launched at the deadline
Tasks
0. custom class based context manager for Database connection
mandatory
Objective: create a class based context manager to handle opening and closing database connections automatically

Instructions:

Write a class custom context manager DatabaseConnection using the __enter__ and the __exit__ methods

Use the context manager with the with statement to be able to perform the query SELECT * FROM users. Print the results from the query.

Repo:

GitHub repository: alx-backend-python
Directory: python-context-async-perations-0x02
File: 0-databaseconnection.py
1. Reusable Query Context Manager
mandatory
Objective: create a reusable context manager that takes a query as input and executes it, managing both connection and the query execution

Instructions:

Implement a class based custom context manager ExecuteQuery that takes the query: ”SELECT * FROM users WHERE age > ?” and the parameter 25 and returns the result of the query

Ensure to use the__enter__() and the __exit__() methods

Repo:

GitHub repository: alx-backend-python
Directory: python-context-async-perations-0x02
File: 1-execute.py
2. Concurrent Asynchronous Database Queries
mandatory
Objective: Run multiple database queries concurrently using asyncio.gather.

Instructions:

Use the aiosqlite library to interact with SQLite asynchronously. To learn more about it, click here.

Write two asynchronous functions: async_fetch_users() and async_fetch_older_users() that fetches all users and users older than 40 respectively.

Use the asyncio.gather() to execute both queries concurrently.

Use asyncio.run(fetch_concurrently()) to run the concurrent fetch

Repo:

GitHub repository: alx-backend-python
Directory: python-context-async-perations-0x02
File: 3-concurrent.py

