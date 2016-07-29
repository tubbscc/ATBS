#! python3

import os

# Set path before using for new pc or user
#base_path = 'C:\\Users\\Casey\\Desktop\\ATBS'
base_path = 'C:\\Users\\yi2845\\Documents\\P_Drive\\Project Work\\ETQ\\testdir'
folder1 = 'Backup'
folder2 = 'Logs'
folder3 = 'Master Data Info'
folder4 = 'Package Files'
folder5 = 'Promotion File'
folder6 = 'Testing'
folder7 = 'Source'
folder8 = 'Target'

# check for base path on this pc
if not os.path.exists(base_path):
    print('base_path does not exist on this pc.')
    print('Make sure you have edited the base_path variable in this file before proceeding.')
    print('press enter to exit')
    raw_input()
    quit()

# Try block to help validate for integer value
try:
    print('This will create the standard set of folders for a new EtQ Reliance promotion')
    print('Select which environment to create new promotions folders')
    print('1 for Dev to QA')
    print('2 for QA to PROD')

    env_choice = int(input())

    # Checking to see if user entered 1 or 2 which are valid options
    if env_choice == 1:                                                                                                                                                                
        env_folder = 'Dev to QA'
    elif env_choice == 2:
     env_folder = 'QA to PROD'
    elif env_choice != 1:
        print('Invalid choice')
        quit()
    elif env_choice !=2:
        print('Invalid choice')
        quit()
except ValueError:                                                                              # Any value other than integer fails this test
    print('You entered something other than a number')
    print('Press any key to exit...')
    input()
    quit()

print('Date of promotion  example format  7-24-2016')
prom_date = input()

# function to create new folder
def create_folder(new_folder):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

#newpath = base_path + '\\' + prom_date + '\\' + env_folder
#create_folder(newpath)

newpath = base_path + '\\' + prom_date + ' ' + env_folder
create_folder(newpath)

# sub-folders to create
newpath_subs1 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder1
newpath_subs2 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder2
newpath_subs3 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder3
newpath_subs4 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder4
newpath_subs5 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder5
newpath_subs6 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder6
newpath_subs7 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder2 + '\\' + folder7
newpath_subs8 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder2 + '\\' + folder8

# try block to create sub-folders
try:
    os.makedirs(newpath_subs1)
    os.makedirs(newpath_subs2)
    os.makedirs(newpath_subs3)
    os.makedirs(newpath_subs4)
    os.makedirs(newpath_subs5)
    os.makedirs(newpath_subs6)
    os.makedirs(newpath_subs7)
    os.makedirs(newpath_subs8)
except OSError:
    pass

#print('base_path = ' + base_path)
#print('new_path = ' + newpath)
#print('new_path_subs = ' + newpath_subs)
#print('env_choice = ' + str(env_choice))
#print(prom_date)

input("Finished...Press enter to continue")
