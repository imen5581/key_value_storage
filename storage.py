import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

db = {}

# Преобразуем хранилище в json
def to_json(dict_name):
    return json.dumps(dict_name, ensure_ascii=False)

def write_to_file(dict_name):
    with open(storage_path, 'w', encoding='utf-8') as f:
        f.write(to_json(dict_name))
        
def read_to_file():
    with open(storage_path, 'r', encoding='utf-8') as f:
       data = json.load(f)
    return data   
    

#Задаем аргументы командной строки
parser = argparse. ArgumentParser(description = 'My parser')
parser.add_argument('--key',
                    default = None,
                    help = 'key of data (default: None)'
                    )
parser.add_argument('--val',
                    default = None,
                    help = 'value of data (default: None)'
                    )
args = parser.parse_args()



# Логика хранилища
if args.key != None and args.val != None:

    if os.path.isfile(storage_path) == True:
    
        db = read_to_file()
        if args.key in db:
            db[args.key].append(args.val)
            write_to_file(db)
        
        elif args.key not in db:
            db.update({args.key: [args.val]})
            write_to_file(db)
            
    else:
        
        db.update({args.key : [args.val]})
        write_to_file(db)
        
if args.key != None and args.val == None:
    

    try:
        
               
        db = read_to_file()
            
        if args.key in db:
            
            num = 0

            len_list = len(db[args.key])
            while len_list > 0:
                print(db[f'{args.key}'][num], end = '')
                if len_list != 1:
                    print(',', end = ' ')
                len_list -= 1
                num += 1
                
        elif args.key  not in db:
            print ('None')
    
    except FileNotFoundError:
        print('None')
    


