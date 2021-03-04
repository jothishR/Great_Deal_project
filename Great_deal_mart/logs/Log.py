import os
import logging
curr_path = os.getcwd()
print(curr_path+'\\Info_log.log' )

def Info_log():
    logging.basicConfig(filename=curr_path + '\\Info_log.log', format='%(asctime)s %(message)s', filemode='w')
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)


"""def Error_log():
    logging.basicConfig(filename=path + '\\apps\logs\db.log', format='%(asctime)s %(message)s', filemode='w')
    print(path + '\logs\db.log')
    self.log = logging.getLogger()
    self.log.setLevel(logging.DEBUG)"""

