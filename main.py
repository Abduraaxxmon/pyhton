import sqlite3 as sql

# connection = sql.connect("./data.db")
# # # connection.execute(':memory:')
# # connection.execute('use salom')
# cursor = connection.cursor()

# queary="select datetime('now','localtime')"
# cursor.execute(queary)

# result = cursor.fetchall()
# print(result)
# connection.close()
def writeQueary( queary):

    with sql.connect('./data.db') as f:
        cursor= f.cursor()
        cursor.execute(queary)
        print(cursor.fetchall())
        f.commit()

        
queary="select * from _users"
sq="""
create * from _users;z
insert into _users values(2,'salom2')    
"""
# writeQueary(sq)

def update(id,name):
    queary="""
    update _users 
    set name = ?
    where id = ? and
    """
    with sql.connect('./data.db') as f:
        cursor= f.cursor()
        cursor.executemany(queary,name,id)
        print(cursor.fetchall())
        f.commit()

update(2,'Salom3')
