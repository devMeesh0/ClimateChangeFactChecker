import MySQLdb
from MySQLdb.cursors import DictCursor

class database:
    def __init__(self):
        print('Attempting to connect...')
        self.connection = MySQLdb.connect(user = "baccaffb66e822", passwd = "99cfc83e", db = "heroku_8d712e26b0e3972", host = "us-cdbr-east-03.cleardb.com", cursorclass = DictCursor)
        self.cursor1 = self.connection.cursor()
        print('Connected')
    
    def getQuery(self, category): 
        return "SELECT tweeturl, tweettext, date, username FROM tweettable WHERE category = '%s'" % category

    def get_category(self, category):
        self.cursor1.execute(self.getQuery(category))
        for i in range(self.cursor1.rowcount):
            data = self.cursor1.fetchone()
            return data["tweeturl"], data["tweettext"], data["date"], data["username"]