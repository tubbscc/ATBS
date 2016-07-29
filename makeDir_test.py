#! python3

if __name__ == "__main__":
    import os

    print('This will create the standard set of folders for a new EtQ Reliance promotion')
    print('Select which environment to create new promotions folders')
    print('1 for Dev to QA')
    print('2 for QA to PROD')
    env_choice = int(input())

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

    print('Date of promotion  example format  7-24-2016')
    prom_date = input()

    base_path = 'C:\\Users\\Casey\\Desktop\\ATBS'
    folder1 = 'Backup'
    folder2 = 'Logs'
    folder3 = 'Master Data Info'
    folder4 = 'Package Files'
    folder5 = 'Promotion File'
    folder6 = 'Testing'



    def create_folder(new_folder):
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    #newpath = base_path + '\\' + prom_date + '\\' + env_folder
    #create_folder(newpath)

    newpath = base_path + '\\' + str(prom_date) + ' ' + env_folder
    create_folder(newpath)


    newpath_subs1 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder1
    newpath_subs2 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder2
    newpath_subs3 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder3
    newpath_subs4 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder4
    newpath_subs5 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder5
    newpath_subs6 = base_path + '\\' + prom_date + ' ' + env_folder + '\\' + folder6

    os.makedirs(newpath_subs1)
    os.makedirs(newpath_subs2)
    os.makedirs(newpath_subs3)
    os.makedirs(newpath_subs4)
    os.makedirs(newpath_subs5)
    os.makedirs(newpath_subs6)



    #create_folder(newpath)

    print('base_path = ' + base_path)
    print('new_path = ' + newpath)
    #print('new_path_subs = ' + newpath_subs)
    print('env_choice = ' + str(env_choice))
    print(prom_date)

    input("Press enter to continue")
    main()
