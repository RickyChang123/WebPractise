import  sqlite3

conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()


cursor.execute("""CREATE TABLE users (
    id INT PRIMARY KEY,
    userName TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT UNIQUE
)""")


# cursor.execute("""Delete from users""")

# result = cursor.execute(
#     "select * from users")
# print(result.fetchall())


conn.commit()
conn.close()



