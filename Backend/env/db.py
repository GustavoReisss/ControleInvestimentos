from pony.orm import Database


db = Database()
db.bind(provider='mysql', host='localhost', port=3306, user='admin', password='admin', db='investimentos')