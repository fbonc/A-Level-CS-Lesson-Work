import sqlite3

connection = sqlite3.connect(r'L6 LT2\Mr. Lomax\DBs\chinook.db')

print(connection.execute("PRAGMA table_info('Artists')"))


query = '''
SELECT artists.name, albums.title 
FROM albums, artists 
WHERE albums.artistid = artists.artistid AND artists.name LIKE ?
'''

artistname = input("Artist Name: ")
params = ('%'+artistname+'%',)

results = connection.execute(query, params)

for row in results:
    print(f'{row[0]}: {row[1]}')



connection.commit()
connection.close() 