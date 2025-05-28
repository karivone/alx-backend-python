
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


Unittests and Integration Tests

    Novice
    Weight: 1
    Project will start May 26, 2025 12:00 AM, must end by Jun 2, 2025 12:00 AM
    Checker was released at May 26, 2025 12:00 AM
    An auto review will be launched at the deadline

Unit testing is the process of testing that a particular function returns expected results for different set of inputs. A unit test is supposed to test standard inputs and corner cases. A unit test should only test the logic defined inside the tested function. Most calls to additional functions should be mocked, especially if they make network or database calls.

The goal of a unit test is to answer the question: if everything defined outside this function works as expected, does this function work as expected?

Integration tests aim to test a code path end-to-end. In general, only low level functions that make external calls such as HTTP requests, file I/O, database I/O, etc. are mocked.

Integration tests will test interactions between every part of your code.

Execute your tests with

$ python -m unittest path/to/test_file.py

Resources

Read or watch:

    unittest — Unit testing framework
    unittest.mock — mock object library
    How to mock a readonly property with mock?
    parameterized
    Memoization

Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

    The difference between unit and integration tests.
    Common testing patterns such as mocking, parametrizations and fixtures

Requirements

    All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
    All your files should end with a new line
    The first line of all your files should be exactly #!/usr/bin/env python3
    A README.md file, at the root of the folder of the project, is mandatory
    Your code should use the pycodestyle style (version 2.5)
    All your files must be executable
    All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
    All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
    All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
    A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
    All your functions and coroutines must be type-annotated.

Required Files
utils.py (or download)
Click to show/hide file contents
client.py (or download)
Click to show/hide file contents
fixtures.py (or download)
Click to show/hide file contents
Tasks
0. Parameterize a unit test
mandatory

Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.

In this task you will write the first unit test for utils.access_nested_map.

Create a TestAccessNestedMap class that inherits from unittest.TestCase.

Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.

Decorate the method with @parameterized.expand to test the function for following inputs:

nested_map={"a": 1}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a",)
nested_map={"a": {"b": 2}}, path=("a", "b")

For each of these inputs, test with assertEqual that the function returns the expected result.

The body of the test method should not be longer than 2 lines.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_utils.py

1. Parameterize a unit test
mandatory

Implement TestAccessNestedMap.test_access_nested_map_exception. Use the assertRaises context manager to test that a KeyError is raised for the following inputs (use @parameterized.expand):

nested_map={}, path=("a",)
nested_map={"a": 1}, path=("a", "b")

Also make sure that the exception message is as expected.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_utils.py

2. Mock HTTP calls
mandatory

Familiarize yourself with the utils.get_json function.

Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.

We don’t want to make any actual external HTTP calls. Use unittest.mock.patch to patch requests.get. Make sure it returns a Mock object with a json method that returns test_payload which you parametrize alongside the test_url that you will pass to get_json with the following inputs:

test_url="http://example.com", test_payload={"payload": True}
test_url="http://holberton.io", test_payload={"payload": False}

Test that the mocked get method was called exactly once (per input) with test_url as argument.

Test that the output of get_json is equal to test_payload.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_utils.py

3. Parameterize and patch
mandatory

Read about memoization and familiarize yourself with the utils.memoize decorator.

Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.

Inside test_memoize, define following class

class TestClass:

    def a_method(self):
        return 42

    @memoize
    def a_property(self):
        return self.a_method()

Use unittest.mock.patch to mock a_method. Test that when calling a_property twice, the correct result is returned but a_method is only called once using assert_called_once.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_utils.py

4. Parameterize and patch as decorators
mandatory

Familiarize yourself with the client.GithubOrgClient class.

In a new test_client.py file, declare the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.

This method should test that GithubOrgClient.org returns the correct value.

Use @patch as a decorator to make sure get_json is called once with the expected argument but make sure it is not executed.

Use @parameterized.expand as a decorator to parametrize the test with a couple of org examples to pass to GithubOrgClient, in this order:

    google
    abc

Of course, no external HTTP calls should be made.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_client.py

5. Mocking a property
mandatory

memoize turns methods into properties. Read up on how to mock a property (see resource).

Implement the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.

Use patch as a context manager to patch GithubOrgClient.org and make it return a known payload.

Test that the result of _public_repos_url is the expected one based on the mocked payload.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_client.py

6. More patching
mandatory

Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.

Use @patch as a decorator to mock get_json and make it return a payload of your choice.

Use patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

Test that the mocked property and the mocked get_json was called once.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_client.py

7. Parameterize
mandatory

Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.

Parametrize the test with the following inputs

repo={"license": {"key": "my_license"}}, license_key="my_license"
repo={"license": {"key": "other_license"}}, license_key="my_license"

You should also parameterize the expected returned value.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_client.py

8. Integration test: fixtures
mandatory

We want to test the GithubOrgClient.public_repos method in an integration test. That means that we will only mock code that sends external requests.

Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.

Use @parameterized_class to decorate the class and parameterize it with fixtures found in fixtures.py. The file contains the following fixtures:

org_payload, repos_payload, expected_repos, apache2_repos

The setupClass should mock requests.get to return example payloads found in the fixtures.

Use patch to start a patcher named get_patcher, and use side_effect to make sure the mock of requests.get(url).json() returns the correct fixtures for the various values of url that you anticipate to receive.

Implement the tearDownClass class method to stop the patcher.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_client.py


