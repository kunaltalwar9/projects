import configparser
import mysql.connector
from mysql.connector import Error


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database']
}


def getPassword():
    return 'sdfsdfds'


def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config) # ** clearly tells that the argument that is, is a dictionary
        if conn.is_connected():
            print("Connection successful")
            return conn
    except Error as e:
        print(e)


