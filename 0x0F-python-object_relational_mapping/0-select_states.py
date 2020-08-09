#!/usr/bin/python3
"""Task 0"""
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

    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)

    db.close()
