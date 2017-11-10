#  !/usr/bin/python

import os
import sys
import time
from shutil import copyfile

if len(sys.argv) > 1:
    walk_dir = sys.argv[1]
else:
    walk_dir = r'C:\Users\luchito\Downloads\CSCI3110-work'
#walk_dir = r'C:\Users\luchito\Downloads\repository'
# detination
newdest = r'C:\Users\luchito\Desktop\temp'

# temporary file -- test file is a script
testFileSource = r'C:\Users\luchito\Downloads\grade.pl'
#testFileSource = r'C:\Users\luchito\Downloads\OLA4\OLA4\inventory.txt'

t0 = time.time()

for root, dir, file in os.walk(walk_dir):
    #print(root)

    #if ('OLA4' or 'ola4' or 'lab4' or 'OLA 4' or 'roject4' or 'roject 4'or 'OpenLab4' or 'ola4ads' ) in root:
    if  ('5') in root:

        for filename in file:

            #if '.cpp' in filename:
            if '.pl' in filename:
                mRoot = root.split(os.sep)

                src = os.path.join(root, filename)
                directory = '%s\\%s' % (newdest, mRoot[6])
                dest = '%s\\%s\\%s' % (newdest, mRoot[6], filename)

                # If the directory is not there it creates a new one directory
                if not os.path.exists(directory):
                    os.makedirs(directory)
                # copy the file to the new directory
                copyfile(src, dest)

                # it copies the file that is for testing in every folder
                testDest = '%s\\%s\\%s' % (newdest, mRoot[6], 'grade.pl')
                # This function copies an external file as an input for a program
                copyfile(testFileSource, testDest)

                #if ('ola4.cpp') in filename:
                if ('.pl') in filename:

                    # this rename the file
                    newname = '%s\\%s\\%s' % (newdest, mRoot[6], 'StudentSolution.pl')
                    # this catches the files that has more than one file
                    try:
                        #this change the file name
                        os.rename(dest, newname)
                    except FileExistsError:

                        print('** file exist: '+ dest)

            #if '.h' in filename:
            if '.docx' in filename:
                mRoot = root.split(os.sep)

                src = os.path.join(root, filename)
                directory = '%s\\%s' % (newdest, mRoot[6])
                dest = '%s\\%s\\%s' % (newdest, mRoot[6], filename)
                if not os.path.exists(directory):
                    os.makedirs(directory)

                copyfile(src, dest)

    '''if  ('OLA4') in root:

        for filename in file:

            if '.cpp' in filename:
            #if '.rkt' in filename:
                mRoot = root.split(os.sep)

                src = os.path.join(root, filename)
                directory = '%s\\%s' % (newdest, mRoot[6])
                dest = '%s\\%s\\%s' % (newdest, mRoot[6], filename)

                # If the directory is not there it creates a new one directory
                if not os.path.exists(directory):
                    os.makedirs(directory)
                # copy the file to the new directory
                copyfile(src, dest)

                # it copies the file that is for testing in every folder
                testDest = '%s\\%s\\%s' % (newdest, mRoot[6], 'inventory.txt')

                # This function copies an external file as an input for a program
                copyfile(testFileSource, testDest)

                if ('ola4.cpp') in filename:
                    # this rename the file
                    newname = '%s\\%s\\%s' % (newdest, mRoot[6], 'main.cpp')
                    # this catches the files that has more than one file
                    try:
                        #this change the file name
                        os.rename(dest, newname)
                    except FileExistsError:

                        print('** file exist: '+ dest)

            if '.h' in filename:
            # if '.docx' in filename:
                mRoot = root.split(os.sep)

                src = os.path.join(root, filename)
                directory = '%s\\%s' % (newdest, mRoot[6])
                dest = '%s\\%s\\%s' % (newdest, mRoot[6], filename)
                if not os.path.exists(directory):
                    os.makedirs(directory)

                copyfile(src, dest)'''





t1 = time.time()
total = t1 - t0
print('%.4f' % total)
