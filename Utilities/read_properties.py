import configparser #dima
config = configparser.RawConfigParser() #hethi tkhalina na9rou el fichier config.ini eli bih el feyda
config.read(".\\Configurations\\config.ini") #whethi kif kif
#fichier hatha fih les methode static lkoll
#read propertie hethi dima ta9ra mel config  nestaamlou feha class read_config


class read_config: #fetch data (dima hakka)
    @staticmethod
    def get_url():
        url = config.get('admin login info','login_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('admin login info','username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin login info','password')
        return password

    @staticmethod
    def invalid_username():
        invalid_username = config.get('admin login info','invalid_username')
        return invalid_username



