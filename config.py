import os
import configparser
import json
from util import (
    parse_json
)
class Config(object):
    def __init__(self, config_file='config.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: config.ini")
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        return self._config.get(section, name)

    def getRaw(self, section, name):
        return self._configRaw.get(section, name)

    def getAddressObject(self,nickName):
        resp_json = None
        path = os.path.join(os.getcwd(),"/cookies/{}.address.json".format(nickName))
        if not os.path.exists(path):
            return resp_json
        try:
            f = open(path, 'r')  
            text = f.read()
            f.close()
            resp_json = parse_json(text)
        except Exception:
            return resp_json
        return resp_json
    
    def setAddressObject(self,nickName,text):
        path = os.path.join(os.getcwd(),"/cookies/{}.address.json".format(nickName))
        if os.path.exists(path):
            os.remove(path)
        f = open(path,"w+")
        f.write(text)
        f.close()

global_config = Config()
