#!/usr/bin/python3
"""script that takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Initialize connection"""
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states\
        WHERE BINARY name = %s;", (argv[4], ))
    for row in cur.fetchall():
        print(row)

    db.close()
