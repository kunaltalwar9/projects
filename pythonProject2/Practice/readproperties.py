import configparser

config = configparser.RawConfigParser()
config.read("#path of config.ini file")


class Readconfig:
    @staticmethod
    def getapplicationurl(self):
        url = config.get('common info', 'base url')
        return url

    @staticmethod
    def getemail(self):
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword(self):
        password = config.get('common info', 'password')
        return password