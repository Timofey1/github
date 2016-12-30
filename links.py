from SQLHelp import *
from Functions import *

def add_url_to_links(url):
    a.query(
        'INSERT INTO links(destination) values (\'%s\')' % url
    )


def find_url_in_links(Id):
    result = a.fetch('Select * from links where id = \'%s\';' % Id)
    return result[0][1]


def createLinks():
    a.query(
        'CREATE TABLE links(id INTEGER NOT NULL PRIMARY KEY autoincrement UNIQUE, destination TEXT, isDeleted INTEGER);'
    )


a = SQLHelp()




# url = 'ya.ru'
#add_url(url)

#print(a.fetch('Select * from links;'))


