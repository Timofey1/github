from SQLHelp import SQLHelp


def createVisits():
    a.query(
        'CREATE TABLE visits(id INTEGER NOT NULL PRIMARY KEY autoincrement UNIQUE, vk_id INTEGER, link_id INTEGER, fromWhere TEXT, date INTEGER);'
    )


def addVisit(link_id, vk_id, fromWhere):
    a.query(
        'INSERT INTO visits(vk_id, link_id, fromWhere) values (%d,%d,\'%s\')' % (vk_id, link_id, fromWhere)
    )
    return

a = SQLHelp()
