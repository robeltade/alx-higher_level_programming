#!/usr/bin/python3
"""
List all states with name starting with N.
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':

    db_key = []

    for args in argv[1:]:
        db_key.append(args)

    db = MySQLdb.connect(
      host='localhost',
      port=3306,
      user=f"{db_key[0]}",
      passwd=f"{db_key[1]}",
      db=f"{db_key[2]}"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE states.name LIKE BINARY 'N%' ORDER BY states.id ASC")
    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
