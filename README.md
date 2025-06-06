
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

9. Integration tests
#advanced

Implement the test_public_repos method to test GithubOrgClient.public_repos.

Make sure that the method returns the expected results based on the fixtures.

Implement test_public_repos_with_license to test the public_repos with the argument license="apache-2.0" and make sure the result matches the expected value from the fixtures.

Repo:

    GitHub repository: alx-backend-python
    Directory: 0x03-Unittests_and_integration_tests
    File: test_client.py

Understanding Authentication and Permission in Enterprise Applications

Authentication and permission systems are the cornerstone of any secure and scalable backend architecture. Whether you’re building a small SaaS platform or a robust enterprise-grade application, implementing robust user access controls ensures the integrity, confidentiality, and availability of your system’s data.

In Django, authentication and authorization (permissions) are elegantly handled through a combination of built-in tools and extendable frameworks. For mid to senior-level backend engineers, mastering these components is essential not only for technical growth but also for building secure, maintainable, and scalable systems that align with industry standards and compliance requirements (e.g., GDPR, HIPAA, SOC 2).

In small-scale apps, authentication may seem straightforward with simple login/signup flows. However, as the application scales, challenges such as multi-role systems, fine-grained permissions, external integrations (OAuth, JWT, SSO), and API security become more critical. Understanding how to implement and customize these systems will empower developers to create backend services that are both user-friendly and enterprise-ready.
Learning Objectives

By the end of this module, learners will be able to:

    Understand Core Concepts
        Define authentication and authorization, and understand how Django handles both.
        Differentiate between user roles, groups, and permission sets.

    Implement Authentication
        Build custom user models and extend Django’s default User model.
        Implement session-based and token-based (e.g., JWT) authentication.
        Integrate third-party authentication services (e.g., OAuth2, SSO).

    Design Permission Systems
        Create custom permissions for models, views, and APIs.
        Use Django’s permissions_required, @login_required, and DRF permissions.
        Implement object-level permissions for more granular control.

    Secure Enterprise APIs
        Enforce role-based access control (RBAC) for enterprise applications.
        Combine authentication with throttling and rate limiting for production use.

    Audit and Monitor Access
        Set up logging, user activity tracking, and audit trails.
        Understand best practices for secure password storage, account recovery, and session handling.

Expected Learning Outcomes

Learners will:

    Build robust authentication flows using Django and Django REST Framework.
    Develop scalable permission layers for small to enterprise-grade apps.
    Apply security principles to protect APIs and sensitive endpoints.
    Gain confidence in integrating third-party identity providers (IdPs) and implementing custom permissions.
    Understand how to structure user roles and access hierarchies in complex systems.

Suggested Tools and Libraries to Master
Tool/Library 	Purpose
Django Allauth 	Streamlined user authentication, including email verification and social auth
Django REST Framework (DRF) 	Token and session authentication for APIs
SimpleJWT / djangorestframework-simplejwt 	Lightweight JWT authentication for DRF
OAuthLib / django-oauth-toolkit 	Secure OAuth2 implementation in Django
Guardian 	Object-level permissions and per-instance access control
Auth0 	Third-party identity and access management integration
Keycloak 	Open-source identity provider for managing enterprise SSO
Okta 	Enterprise IAM provider with SSO, MFA, and directory services
PyJWT 	Lightweight JWT token generation and validation
Auditlog 	Automatic tracking of model changes and user actions for audit trails
Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. Implement Authentication
mandatory

Objective: Add user authentication using JWT (JSON Web Tokens) or Session Authentication.

Instructions:

    Install djangorestframework-simplejwt for JWT Authentication.

    Configure the authentication settings in the settings.py. More on how to: here

    Ensure all users can access their own messages and conversations

Repo:

    GitHub repository: alx-backend-python
    Directory: messaging_app
    File: messaging_app/settings.py, messaging_app/chats/auth.py, messaging_app/urls.py, messaging_app/chats/permissions.py

1. Add Permissions
mandatory

Objective: Create custom permission classes to control access.

Instructions:

    Create and extend the permissions class IsParticipantOfConversation to:
        Allow only authenticated users to access the api
        Allow only participants in a conversation to send, view, update and delete messages

    Apply the custom permissions to your viewsets to enforce access control

    Update your settings.py to set default permissions globally

Repo:

    GitHub repository: alx-backend-python
    Directory: messaging_app
    File: chats/permissions.py, chats/Views.py, messaging_app/settings.py

2. Pagination and Filtering
mandatory

Objective: implement pagination and filtering for messages

Instructions:

    Add pagination listing on the messages such that the api fetches 20 messages per page. Resource: here

    Using django-filters , Add filtering class MessageFilter to your views to retrieve conversations with specific users or messages within a time range

Repo:

    GitHub repository: alx-backend-python
    Directory: messaging_app
    File: messaging_app/settings.py, chats/views.py, chats/permissions.py, chats/filters.py, chats/pagination.py

3. Testing the API Endpoints
mandatory

Objective: Use postman to test api endpoints

Instructions:

    Test creating a conversation, sending messages and fetching conversations

    Test authentication (JWT token login) and ensure that unauthorized users cannot access private conversations.

Repo:

    GitHub repository: alx-backend-python
    Directory: messaging_app
    File: post_man-Collections


Understanding Middlewares

    Novice
    Weight: 1
    Project will start Jun 2, 2025 12:00 AM, must end by Jun 9, 2025 12:00 AM
    Checker was released at Jun 2, 2025 12:00 AM
    Manual QA review must be done (request it when you are done with the project)
    An auto review will be launched at the deadline

Overview

Middleware is a powerful feature in application design that acts as a bridge between the request and response phases of the application cycle. In this project, learners will explore the concept of middleware, learn how to write custom middleware, and implement logic such as request interception, permission enforcement, request data filtering, logging, and more. Learners will also examine real-world use cases, such as authentication and rate-limiting, and understand the best practices when integrating middleware into a Django application.

This hands-on project will guide you in building a series of middleware components for an Airbnb Clone or similar web application, allowing them to understand middleware’s role in clean architecture and modular backend development.
Learning Objectives

By the end of this project, learners should be able to:

    Understand the concept and lifecycle of middleware in Django.
    Create custom middleware to intercept and process incoming requests and outgoing responses.
    Filter and modify request/response data at the middleware level.
    Implement access control mechanisms using middleware.
    Use middleware to enforce API usage policies like rate limiting or request validation.
    Integrate third-party middleware and understand Django’s default middleware stack.
    Apply best practices for organizing middleware logic in a scalable project.

Learning Outcomes

Upon successful completion, learners will:

    Define and explain how Django middleware works within the request/response cycle.
    Write and integrate custom middleware in a Django project.
    Use middleware to enforce permissions and restrict access based on roles, IP, or headers.
    Filter and clean incoming request data before reaching the views.
    Log request and response metadata for auditing or debugging purposes.
    Separate concerns effectively using middleware rather than overloading views.
    Evaluate the trade-offs and limitations of using middleware for certain functionalities.

Implementation Tasks

Learners will:

    Scaffold a Django project with an apps/core structure for separation of concerns.
    Build custom middleware to:
        Log incoming requests and outgoing responses.
        Restrict access to authenticated users or specific user roles.
        Block requests from banned IPs or suspicious headers.
        Modify or validate incoming JSON payloads.
    Configure the MIDDLEWARE stack correctly in settings.py to include both built-in and custom middleware.
    Test middleware behavior using Postman or Django’s test client to verify interception, modification, and rejection of requests.
    Document middleware behavior using inline comments and Markdown files for clarity and maintainability.

Best Practices for Project Setup and Middleware Design

Here are some best practices to follow during implementation:
📁 Project Scaffolding Tips

    Use a modular structure like:

  /project-root
    /apps
      /core
        /middleware
        /models
        /views
      /users
      /listings
    /config
    manage.py

    Keep each custom middleware in a separate Python file under apps/core/middleware/ for clarity.
    Use environment variables and Django settings to control behavior (e.g., toggle middleware for dev/production).

Middleware Best Practices

    Keep middleware functions small and focused — avoid bloating a single middleware with multiple responsibilities.
    Chain logic properly — always call get_response(request) unless rejecting the request early.
    Use Django’s request.user, request.path, and request.method for clean conditional logic.
    Avoid database-heavy logic in middleware to maintain performance.
    Use logging middleware responsibly — log minimal and relevant data to avoid clutter.
    Write unit tests for middleware behavior and edge cases.
    Document each middleware clearly — what it does, why it exists, and where it sits in the stack.

Limitations and Considerations

While middleware can be powerful, it’s important to recognize its limitations:

    Middleware shouldn’t replace views or serializers for business logic.
    Middleware runs on every request, so poorly optimized code can degrade performance.
    Order in MIDDLEWARE settings matters — incorrect ordering may break expected behavior.
    Some functionalities are better suited for views, decorators, or DRF permissions.

Quiz questions
Great! You've completed the quiz successfully! Keep going! (Show quiz)
Tasks
0. project set up
mandatory

Objective: Set up the django messaging app locally

Instructions:

    Make a copy of the messaging_app directory done in the project Building Robust APIs,

    Rename the copied directory to Django-Middleware-0x03

Repo:

    GitHub repository: alx-backend-python
    Directory: Django-Middleware-0x03
    File: Django-Middleware-0x03/*

1. Logging User Requests(Basic Middleware)
mandatory

Objective: Create a middleware that logs each user’s requests to a file, including the timestamp, user and the request path.

Instructions: - create a file middleware.py and Create the middleware class RequestLoggingMiddleware with two methods, __init__and __call__.

    In the __call__ implement a logger that log’s the following information f"{datetime.now()} - User: {user} - Path: {request.path}“

    Configure the Middleware section in the settings.py with your newly created middleware

    Run the server to test it out. python manage.py runserver

Repo:

    GitHub repository: alx-backend-python
    Directory: Django-Middleware-0x03
    File: chats/middleware.py, requests.log

2. Restrict Chat Access by time
mandatory

Objective: implement a middleware that restricts access to the messaging up during certain hours of the day

Instructions:

    Create a middleware class RestrictAccessByTimeMiddleware with two methods, __init__and__call__. that check the current server time and deny access by returning an error 403 Forbidden
        if a user accesses the chat outside 9PM and 6PM.

    Update the settings.py with the middleware.

Repo:

    GitHub repository: alx-backend-python
    Directory: Django-Middleware-0x03
    File: Django-Middleware-0x03/chats/middleware.py

3. Detect and Block offensive Language
mandatory

Objective: Implement middleware that limits the number of chat messages a user can send within a certain time window, based on their IP address.

Instructions:

    Create the middleware class OffensiveLanguageMiddleware with two methods, __init__and__call__. that tracks number of chat messages sent by each ip address and implement a time based limit i.e 5 messages per minutes such that if a user exceeds the limit, it blocks further messaging and returns and error
        use the __call__method to count the number of POST requests (messages) from each IP address.
        Implement a time window (e.g., 1 minute) during which a user can only send a limited number of messages.
    Ensure the middleware is added to theMIDDLEWARE setting in the settings.py

Repo:

    GitHub repository: alx-backend-python
    Directory: Django-Middleware-0x03
    File: Django-Middleware-0x03/chats/middleware.py

4. Enforce chat user Role Permissions
mandatory

Objective: define a middleware that checks the user’s role i.e admin, before allowing access to specific actions

Instructions:

    Create the middleware class RolepermissionMiddleware with two methods, __init__ and __call__. that checks the user’s role from the request
    If the user is not admin or moderator, it should return error 403
        Ensure the middleware is added to the MIDDLEWARE setting in the settings.py

Repo:

    GitHub repository: alx-backend-python
    Directory: Django-Middleware-0x03
    File: Django-Middleware-0x03/chats/middleware.py


