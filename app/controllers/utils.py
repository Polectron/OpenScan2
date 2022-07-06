basepath = '/home/pi/OpenScan/'
from os.path import isfile

def load_bool(name):
    filename = basepath+'settings/'+name
    if not isfile(filename):
        return
    with open(filename, 'r') as file:
        value = file.read().replace('\n','')
    if value == '1' or value == 'True' or value =='true':
        value = True
    else:
        value = False
    return value

def load_str(name):
    filename = basepath+'settings/'+name
    if not isfile(filename):
        return
    with open(filename, 'r') as file:
        value = file.read().replace('\n','')
    return value

def load_int(name):
    filename = basepath+'settings/'+name
    if not isfile(filename):
        return
    with open(filename, 'r') as file:
        value = int(file.read().replace('\n',''))
    return value

def load_float(name):
    filename = basepath+'settings/'+name
    if not isfile(filename):
        return
    with open(filename, 'r') as file:
        value = float(file.read().replace('\n',''))
    return value

def save_settings(name, value):
    filename = basepath+'settings/'+name
    with open(filename, 'w+') as file:
        file.write(str(value))
    return
