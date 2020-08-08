
#ID    FUNCTION
#0     Make a new directory
#1     Copy a directory
#2     Copy a file from a directory to another directory
#3     Delete a directory
#4     Delete a file
#5     Move a directory
#6     Move a file from a directory to another directory

#import the module that has functions that allow you to copy, move, rename and delete files in your python program
import shutil   #shell utilities
import os   #allows you use operating system dependent functions



#yes
# no
# go back.

def FileOrgs():
    global f_id
    global Functions
    # Welcome the user to the application
    print("\n\t'''Welcome to the 'Saviganga Ease Your Mind' Python Script\n\tThis script automates some really boring clicky tasks on your behalf\n\tBelow is a list of the functions'''\n")

    #create a list of the functions

    list_script_functions()

    #ask the user to select an id to perform a task
    user_task = int(input('\nSelect an ID to perform a function: '))
    if user_task in f_id:
        User_task = Functions[user_task]
        print('\n', User_task, '\n')
    if 'Copy a file' in User_task:
        copy_again()
    elif 'Move a file' in User_task:
        move_file()
    elif 'Copy a directory' in User_task:
        copy_again()
    elif 'Make a new directory' in User_task:
        make_directory()



























def list_script_functions():
    global f_id
    global Functions
    f_id = []
    Functions = ['Make a new directory', 'Copy a directory',
                 'Copy a file from a directory to another directory', 'Delete a directory', 'Delete a file',
                 'Move a directory',
                 'Move a file from a directory to another directory']
    print('\t------FUNCTIONS-----')
    print('ID    FUNCTION')
    for id, function in enumerate(Functions):
        f_id.append(id)
        print(str(id) + '    ', function)











def get_destination():
    global current_wd
    print('\nSelect your destination Folder')
    global Num
    global cwd_directorylist
    find_folder()
    current_wd = os.getcwd()
    new_dir = input('Do you want to make a new directory (y/n): ')
    if new_dir == 'y':
        make_directory()
    elif new_dir == 'n':
        pass
    #print(current_wd)
    return current_wd


























def find_folder():
    global Num
    global cwd_directorylist
    #make a list to save the id of the folder from the user
    Num = []

    print('Select a number to pick a directory')

    #change the cwd starting from the root folder to ease navigation through the system (and then the selected folders as per the user preference)
    root = "C:/"
    cwd = os.path.join(root)
    cwd_directory = os.chdir(cwd)
    print(os.getcwd())

    #display the content of the cwd with id numbers to ease user selection
    cwd_directorylist = os.listdir(cwd_directory)
    delim = 0
    while delim == 0:
        print('ID', ' ', 'Folder')
        for num, val in enumerate(cwd_directorylist):
            Num.append(num)
            print(num, '. ', val)

        #ask user if the file/folder to be copied is in the cwd
        user_input = input('\nThis Folder? (y/n): ')

        #create conditions for execution

        #if user input is no, the user selects an id of the folder he wishes to navigate to and the content ofthe folder is displayed until the user reaches his desired folder
        if user_input == 'n':
            user_folderID = int(input('Select a folder ID: '))
            if user_folderID in Num:
                user_folder = cwd_directorylist[user_folderID]
                cwd = os.path.join(cwd, user_folder)
                cwd_directory = os.chdir(cwd)

                print('\n', os.getcwd())
                cwd_directorylist = os.listdir(cwd_directory)
        elif user_input == 'y':
            delim = delim + 1


























def copy_again():
    find_folder()
    global Num
    global cwd_directorylist
    # get the file(s) in the directory the user wants to copy
    #print('\n', Num, '\n')
    print(os.getcwd())
    num_files = int(input('\n How many files do you want to copy: '))
    copyfiles = []
    for i in range(1, num_files + 1):
        copyfile_id = int(input('\n Enter the ID of your file ' + str(i) + ': '))
        if copyfile_id in Num:
            copyfile_id = cwd_directorylist[copyfile_id]
            #print('\n', copyfile_id, '\n')
            copyfile_idPath = os.path.abspath(copyfile_id)
            copyfiles.append(copyfile_idPath)
#        for file in copyfiles:
#            print(file)
    print('\n', copyfiles)
    destPath = get_destination()
    print(destPath)

    # copy the file(s) to the new directory
    for x in copyfiles:
        shutil.copy(x, destPath)
    print('File(s) copied successfully')
    # print the new content of the destination folder
    DestpathList_new = os.listdir(destPath)
    print('-----NEW DESTINATION FOLDER CONTENT----- \n')
    for destfile_new in DestpathList_new:
        print(destfile_new)

























def move_file():
    find_folder()
    global Num
    global cwd_directorylist
    # get the file(s) in the directory the user wants to copy
    # print('\n', Num, '\n')
    print(os.getcwd())
    num_files = int(input('\n How many files do you want to move: '))
    movefiles = []
    for i in range(1, num_files + 1):
        movefile_id = int(input('\n Enter the ID of your file ' + str(i) + ': '))
        if movefile_id in Num:
            movefile_id = cwd_directorylist[movefile_id]
            # print('\n', copyfile_id, '\n')
            movefile_idPath = os.path.abspath(movefile_id)
            movefiles.append(movefile_idPath)
    #        for file in copyfiles:
    #            print(file)
    print('\n', movefiles)
    destPath = get_destination()
    print(destPath)
    # move the file(s) to the new directory
    for x in movefiles:
        shutil.move(x, destPath)
    print('File(s) moved successfully')
    # print the new content of the destination folder
    DestpathList_new = os.listdir(destPath)
    print('-----NEW DESTINATION FOLDER CONTENT----- \n')
    for num, destfile_new in enumerate(DestpathList_new):
        print(num, '. ', destfile_new)
























#def copy_folder():
  #  find_folder()
 #   global Num
#    global cwd_directorylist








def make_directory():
    global current_wd
    # get to the directory you want to make the folder
    #find_folder()
    print(os.getcwd())
    this_folder = input('This Folder? (y/n): ')
    if this_folder == 'y':
        create_folder()
    elif this_folder == 'n':
        find_folder()
        create_folder()
'''
    # add the cwd to the new folder name
    new_folder = input('Enter the name of your new folder: ')
    current_wd = os.path.join(os.getcwd(), new_folder)
    New_folder = os.makedirs(current_wd)
    #print(new_folderr)
    print('Successfully created')
'''


    # make the new folder




def create_folder():
    global current_wd
    # add the cwd to the new folder name
    new_folder = input('Enter the name of your new folder: ')
    current_wd = os.path.join(os.getcwd(), new_folder)
    New_folder = os.makedirs(current_wd)
    # print(new_folderr)
    print('Successfully created')
    return current_wd




















FileOrgs()
#copy_file()

#get_destination()

#find_folder()
#copy_again()
#make_directory()