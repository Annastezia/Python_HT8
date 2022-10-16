from write_data import *
from read_data import *
from search_data import *
from into_log import *

def start():

    define = int(input('Введите число :\n1 - чтобы найти пользователя \n2 - чтобы добавить пользователя\n'))
    if define == 1:
        func = read_data()
        found = search(func)
        log_search(found)

    if define == 2:
        new_data = write_data()
        log_added(new_data)