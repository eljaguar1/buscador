import os
import json
import time
import io
import telegram

class JsonDatabase(object):
    def __init__(self,path='newdb'):
        self.path = f'{path}.jdb'
        self.items = {}

    def check_create(self):
        exist = os.path.isfile(self.path)
        if not exist:
            db = open(str(self.path), 'w')
            db.write('')
            db.close()

    def save(self):
        dbfile = open(self.path, 'w')
        i = 0
        for user in self.items:
            separator = ''
            if i < len(self.items) - 1:
                separator = '\n'
            dbfile.write(user + '=' + str(self.items[user]) + separator)
            i += 1
        dbfile.close()

    def create_user(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://eduvirtual.uho.edu.cu/',
                     'moodle_repo_id': 3,
                     'moodle_user': 'roilancr',
                     'moodle_password': 'roilan99',
                     'isadmin': 0,
                     'zips': 2048,
                     'uploadtype':'blog',
                     'proxy':'socks5://181.225.255.17:7080',
                     'tokenize':0,
                     'preview':0,
                     'brodcast':0}

    def create_admin(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': '---',
                     'moodle_repo_id': 4,
                     'moodle_user': '---',
                     'moodle_password': '---',
                     'isadmin': 1,
                     'zips': 100,
                     'uploadtype':'evidence',
                     'proxy':'',
                     'tokenize':0,
                     'preview':0,
                     'brodcast':0}

    def create_user_evea_preview(self,name):
        self.items[name] = {'dir': '',
                     'cloudtype': 'moodle',
                     'moodle_host': 'https://evea.uh.cu/',
                     'moodle_repo_id': 4,
                     'moodle_user': 'darian.borges@estudiantes.fbio.uh.cu',
                     'moodle_password': 'darian1995',
                     'isadmin': 0,
                     'zips': 250,
                     'uploadtype':'blog',
                     'proxy':'',
                     'tokenize':0,
                     'preview':1,
                     'brodcast':0}

    def remove(self,name):
        try:
            del self.items[name]
        except:pass

    def get_user(self,name):
        try:
            return self.items[name]
        except:
            return None

    def save_data_user(self,user, data):
        self.items[user] = data

    def is_admin(self,user):
        User = self.get_user(user)
        if User:
            return User['isadmin'] == 1
        return False

    def preview(self,user):
        User = self.get_user(user)
        if User:
            return User['preview'] == 1
        return False

    def load(self):
        dbfile = open(self.path, 'r')
        lines = dbfile.read().split('\n')
        dbfile.close()
        for lin in lines:
            if lin == '': continue
            tokens = lin.split('=')
            user = tokens[0]
            data = json.loads(str(tokens[1]).replace("'", '"'))
            self.items[user] = data
