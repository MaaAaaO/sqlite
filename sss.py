import sqlite3
db= sqlite3.connect('server.db')
c = db.cursor()
c.execute('''DROP TABLE gru1''')
c.execute('''DROP TABLE gru2''')
db.commit()
c.execute('''CREATE TABLE gru2(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT);''')
c.execute('''
    CREATE TABLE gru1 (
    id INTEGER,
    name VARCHAR(60),
    phone VARCHAR(60),
    FOREIGN(id) REFERENCES gru2(id))
    ''')
c.execute('''INSERT INTO gru2(status) VALUES ('ученик');''')
c.execute('''INSERT INTO gru2(status) VALUES ('учитель');''')
c.execute('''INSERT INTO gru2(status) VALUES ('администратор');''')
db.commit()
for i in range(3):
    f = str(input('1 INPUT:'))
    h = str(input('2 INPUT:'))
    b = str(input('3 INPUT:'))
    c.execute('''INSERT INTO gru1 (id, name, phone) VALUES('{0}','{1}', {2})'''.format(f,h,b))
    c.execute('''SELECT * FROM gru1''')
for ex in c.fetchall():
    print(*ex)
c.execute('''SELECT * FROM gru2''')
for ex in c.fetchall():
    print(*ex)