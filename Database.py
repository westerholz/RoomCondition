import configparser
import MySQLdb

class Database(object):
    def __init__(self, configpath):
        config = configparser.ConfigParser()
        self.config    = config.read(configpath)
        self.insertSQL = "INSERT INTO feuchtigkeit( humidity,temperature) VALUES (%s,%s)"
        self.connection = MySQLdb.connect(
                    host   = self.config['mysqlDB']['host'],
                    user   = self.config['mysqlDB']['user'],
                    passwd = self.config['mysqlDB']['pass'],
                    db     = self.config['mysqlDB']['db'])
        self.cursor = self.connection.getCursor()                  

    def writeToDB(self, humidity, temperature):
        value = humidity, temperature
        self.cursor.execute(self.insertSQL, value)
        self.connection.commit()