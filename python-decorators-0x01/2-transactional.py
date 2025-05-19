import sqlite3 
import functools

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

def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #check if connection is already in a transaction
        is_managing_transaction = not conn.in_transaction
        try:
            result = func(conn, *args, **kwargs)
            if is_managing_transaction:
                conn.commit()
            return result
        except Exception as e:
            if is_managing_transaction:
                conn.rollback()
            raise e
    return wrapper


@with_db_connection 
@transactional 
def update_user_email(conn, user_id, new_email): 
cursor = conn.cursor() 
cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 
#### Update user's email with automatic transaction handling 

update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
