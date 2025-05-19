import time
import sqlite3 
import functools

#### paste your with_db_decorator here
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Open the connection
        conn = sqlite3.connect('users.db')
        try:
            # Call the decorated function, passing the connection as the first argument
            return func(conn, *args, **kwargs)
        finally:
            # Always close the connection afterward
            conn.close()
    return wrapper

def retry_on_failure(retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wraps(*args, **kwargs):
            attempt = 0
            while attempt < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt +1} failed with error: {e}")
                    attempt += 1
                    time.sleep(delay)
                raise Exception(f"Function failed after {retries} retries.")
            return Wrapper
        return decorator


@with_db_connection
@retry_on_failure(retries=3, delay=1)

def fetch_users_with_retry(conn):
cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
return cursor.fetchall()

#### attempt to fetch users with automatic retry on failure

users = fetch_users_with_retry()
print(users)

