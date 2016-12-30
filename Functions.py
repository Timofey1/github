from SQLHelp import *
import time

a = SQLHelp()

def IdToShortUrl(Id):

    def reverse(s):
        new_s = ''
        for i in range(1, (len(s) + 1)):
            new_s += s[len(s) - i]
        return new_s

    mapp = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    ShortUrl = ''

    while int(Id) != 0:
        ShortUrl += mapp[Id % 62]
        Id = int(Id / 62)

    return reverse(ShortUrl)


def ShortUrlToId(ShortUrl):
    Id = 0

    for i in range(0, len(ShortUrl)):
        if 'a' <= ShortUrl[i] <= 'z':
            Id = Id * 62 + ord(ShortUrl[i]) - ord('a')
        if 'A' <= ShortUrl[i] <= 'Z':
            Id = Id * 62 + ord(ShortUrl[i]) - ord('A') + 26
        if '0' <= ShortUrl[i] <= '9':
            Id = Id * 62 + ord(ShortUrl[i]) - ord('0') + 52

    return Id

def addUser(d):
    if len(a.fetch('Select * from users where uid = %d' % d['uid'])) == 0:
        a.query('INSERT INTO users(uid) values(%d)' % d['uid'])

    uid = d['uid']
    del d['uid']
    for key in d.keys():
        a.query('UPDATE users SET \'%s\'=\'%s\' WHERE uid=\'%s\'' % (key, d[key], uid))
    a.query('UPDATE users SET date_creation=\'%s\' WHERE uid=\'%s\'' % (time.clock(), uid))
    return


def addVisit(link_id, vk_id, fromWhere):
    a.query(
        'INSERT INTO visits(vk_id, link_id, fromWhere) values (%d,%d,\'%s\')' % (vk_id, link_id, fromWhere)
    )
    return
