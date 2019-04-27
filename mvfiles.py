import csv
import glob
import os
import shutil

MVRULE = './mvrule.csv'

# output: [{'filematch':'./*_dir1_*.txt', 'dst':'./dir1/'}]
def read_csv(mvrule):
    dictlist = []
    print ('import file... : ' + mvrule)
    print ()
    if os.path.exists(mvrule):
        with open(mvrule, encoding="utf-8") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                dict = {}
                if len(row) < 2:
                    print ('Ignored row[' + str(i+1) + '] : ' + str(row))
                    continue
                if (row[0][0] == '#'):
                    print ('Ignored row[' + str(i+1) + '] : ' + str(row))
                    continue
                else:
                    dict['filematch'] = row[0]
                    dict['dst'] = row[1]
                    dictlist.append(dict)
        return dictlist
    else:
        print('Error: \'./mvrule.csv\' doesn\'t exist.')
        return None


def create_directories(dictlist):
    print()
    print('Creating directories...')
    for dict in dictlist:
        if os.path.exists(dict['dst']):
            print(dict['dst'] + ' already exists.')
        else:
            os.makedirs(dict['dst'])
            print ('Create: ' + dict['dst'])


def move_files(dictlist):
    print()
    print('Moving files...')
    print()
    print('*---------- Result ----------*')
    for dict in dictlist:
        if dict['dst'][-1] != '/':
            dict['dst'] += '/'
        if not os.path.isdir(dict['dst']):
            print('Error: directory doesn\'t exist. (' + dict['dst'] + ')')
            continue
        filepaths = glob.glob(dict['filematch'])
        if len(filepaths) == 0:
            print('There is no match for \''+ dict['filematch'] +'\'')
        else:
            for filepath in filepaths:
                fp_split = filepath.split(os.sep)
                if len(fp_split) != 0:
                    filename = fp_split[-1]
                else:
                    filename = filepath
                if os.path.isfile(filepath):
                    checkpath = dict['dst'] + filename
                    if os.path.exists(checkpath):
                        print()
                        print('Error : the file already exists.')
                        print('  ' + checkpath)
                    else:
                        try:
                            os.rename(filepath,filepath)
                            # use only for checking if the file is opened by another process
                        except PermissionError:
                            print()
                            print('Error: permission error (' + filepath +')')
                        else:
                            shutil.move(filepath, dict['dst'])
                            print()
                            print('move file from : ' + filepath)
                            print('move file to   :<dir> ' + dict['dst'])
                else:
                    print('Error: file doesn\'t exist. (' + filepath + ')')


if __name__ == '__main__':
    dictlist = read_csv(MVRULE)
    if dictlist != None:
        create_directories(dictlist)
        move_files(dictlist)
    print()
    print ('Press [Enter] key to exit.')
    input()
