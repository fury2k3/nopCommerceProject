import logging

#logger hethi taatina info kemla 3ali sayer fi dossier LOGS

class Log_maker:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename=".\\Logs\\nopcommerce.log", filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%d-%m-%y %H:%M:%S',force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger