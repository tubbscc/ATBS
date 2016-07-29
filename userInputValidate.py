#! python3

try:                                                                                            # Try block to help validate for integer value
    print('This will create the standard set of folders for a new EtQ Reliance promotion')
    print('Select which environment to create new promotions folders')
    print('1 for Dev to QA')
    print('2 for QA to PROD')

    env_choice = int(input())

    if env_choice == 1:
        env_folder = 'Dev to QA'
    elif env_choice == 2:
     env_folder = 'QA to PROD'
    elif env_choice != 1:                                                                       # Checking to see if user entered 1 or 2 which are valid options
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
