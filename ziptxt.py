import os
import shutil


def folderNamesToTxt(dir):
    if not os.path.isdir(dir):
        return print('path does not exist')
    print('create folder name list text file in: ' + dir)
    list = os.listdir(dir)
    for file in list:
        if os.path.isdir(dir + '/' + file):
            newFileName = file.replace(' ', '_')
            f = open(dir + '/ZIP_' + newFileName + '.txt', 'w')
            print('created folder name txt file')
            shutil.rmtree(dir + '/' + file)
            print('deleted source folder')



if __name__ == '__main__':
    dir = input('dir: ')
    folderNamesToTxt(dir)