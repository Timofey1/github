from SQLHelp import SQLHelp
import time


def createUsers():
    a.query(
        'CREATE TABLE users(uid INTEGER NOT NULL, first_name TEXT, last_name TEXT, sex INTEGER, bday INTEGER, city INTEGER, country INTEGER, home_town INTEGER, university_ids TEXT, schools_ids TEXT, followers INTEGER, relation INTEGER, groups_ids TEXT, date_creation INTEGER);'
    )


def addUser(d):
    if len(a.fetch('Select * from users where uid = %d' % d['uid'])) == 0:
        a.query('INSERT INTO users(uid) values(%d)' % d['uid'])

    uid = d['uid']
    del d['uid']

    for key in d.keys():
        a.query('UPDATE users SET \'%s\'=\'%s\' WHERE uid=\'%s\'' % (key, d[key], uid))
    a.query('UPDATE users SET date_creation=\'%s\' WHERE uid=\'%s\'' % (time.clock(), uid))
    return


a = SQLHelp()
# -----------------------------------------------------------------------------------------------------------------
dictionary = {'uid': 1, 'last_name': 'Beshkurov'}
addUser(dictionary)
# -----------------------------------------------------------------------------------------------------------------
print(a.fetch('select * from users'))
