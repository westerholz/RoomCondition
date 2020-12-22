import configparser
import MySQLdb.cursors

insertSQL = "INSERT INTO feuchtigkeit( humidity,temperature) VALUES (%s,%s)"

config = configparser.ConfigParser()
config.read('config/config.ini')

connection = MySQLdb.connect(host = config['mysqlDB']['host'],
                    user = config['mysqlDB']['user'],
                    passwd = config['mysqlDB']['pass'],
                    db = config['mysqlDB']['db'])
cursor = connection.getCursor()

def read():
    humidity, temperature = Adafruit_DHT.read_retry(config['sensor']['type'], config['sensor']['pin'])
    return ( humidity, temperature = Adafruit_DHT )


    
    
       
