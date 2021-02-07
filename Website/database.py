import MySQLdb
from MySQLdb.cursors import DictCursor


class Database:
    def __init__(self):
        print('Attempting to connect...')
        self.connection = MySQLdb.connect(user = "uname", passwd = "pword", db = "db", host = "localhost", cursorclass = DictCursor)
        self.cursor1 = self.connection.cursor()
        print('Connected')
    
    def getQuery(self, category): 
        return "SELECT tweeturl, tweettext, date, username FROM tweettable WHERE category = '%s'" % category

    def get_category(self, category):
        self.cursor1.execute(self.getQuery(category))
        arr = []
        for i in range(self.cursor1.rowcount):
            data = self.cursor1.fetchone()
            arr.append(data["tweettext"] + " by user: " + data["username"] + "\n. See source: " + data["tweeturl"])

        i = 6 - self.cursor1.rowcount
        while i > 0:
            arr.append("")         
            i = i - 1
        return arr
