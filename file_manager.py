from pathlib import Path
def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        if item.name != '.DS_Store':
           print(f'{i+1}: {item}')

def createfile():
    try:
        readfileandfolder()
        name = input('Enter the name of the file to create: ')
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("Enter the content of the file: ")
                fs.write(data)
            print(f'FILE {name} CREATED SUCCESSFULLY!')
        else:
            print(f'FILE {name} ALREADY EXISTS!')

    except Exception as err:
        print(f'ERROR OCCURRED: {err}')

def readfile():
    try:
        readfileandfolder()
        name = input('Enter the name of the file to read: ')
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print(f'FILE {name} READ SUCCESSFULLY!')
        else:
            print(f'FILE {name} DOES NOT EXIST!')

    except Exception as err:
        print(f'ERROR OCCURRED: {err}')

def updatefile():
    try:
        readfileandfolder()
        name = input('Enter the name of the file to update: ')
        p = Path(name)
        if p.exists() and p.is_file():
            print('PRESS 1 FOR CHANGING THE NAME OF YOUR FILE')
            print('PRESS 2 FOR OVERWRITING THE DATA OF YOUR FILE')
            print('PRESS 3 FOR APPENDING THE CONTENT OF YOUR FILE')

            res = int(input('ENTER YOUR CHOICE: '))

            if res == 1:
                name2 = input('Enter the new name of the file: ')
                p2=Path(name2)
                p.rename(p2)
                print(f'FILE {name} RENAMED TO {name2} SUCCESSFULLY!')

            elif res == 2:
                with open(p, "w") as fs:
                    data = input("Enter the new content of the file: ")
                    fs.write(data)
                print(f'FILE {name} OVERWRITTEN SUCCESSFULLY!')

            elif res == 3:
                with open(p, "a") as fs:
                    data = input("Enter the content to append to the file: ")
                    fs.write('\n'+data)
                print(f'CONTENT APPENDED TO {name} SUCCESSFULLY!')

            else:
                print('INVALID CHOICE!')

    except Exception as err:
        print(f'ERROR OCCURRED: {err}')

def deletefile():
    try:
        readfileandfolder()
        name = input('Enter the name of the file to delete: ')
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print(f'FILE {name} DELETED SUCCESSFULLY!')
        else:
            print(f'FILE {name} DOES NOT EXIST!')

    except Exception as err:
        print(f'ERROR OCCURRED: {err}')


while True:

    print('PRESS 1 for creating a file')
    print('PRESS 2 for reading a file')
    print('PRESS 3 for updating a file')
    print('PRESS 4 for deleting a file')
    print('PRESS 5 for exiting the program')

    try: 

        check=int(input('ENTER YOUR CHOICE: '))

        if check==1:
          createfile()

        elif check==2:
          readfile()

        elif check==3:
          updatefile()

        elif check==4:
          deletefile()

        elif check==5:
            print('THANK YOU FOR USING THE FILE MANAGER')
            break

        else:
          print('INVALID CHOICE!')

    except ValueError:
       print('ERROR OCCURRED: PLEASE ENTER A VALID CHOICE!')