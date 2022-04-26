import os

dir_ = cwd = os.getcwd()


def reg(username=None, password=None):
    global he
    he = 'false'
    try:
        fold = 'Database'
        path = os.path.join(dir_, fold)
        os.mkdir(path)
        try:
            f = open(f'{dir_}\Database\{username}.txt', 'r')
            f.close()
            print('Username already exits')
        except:
            f = open(f'{dir_}\Database\{username}.txt', 'x')
            f.write(username + '\n')
            f.write(password)
            f.close()
            print('done...')
            he = 'true'
            login(username, password)

    except:
        try:
            f = open(f'{dir_}\Database\{username}.txt', 'r')
            f.close()
            print('Username already exits')
        except:
            f = open(f'{dir_}\Database\{username}.txt', 'x')
            f.write(username + '\n')
            f.write(password)
            f.close()
            print('done...')
            he = 'true'
            login(username, password)


def login(username=None, password=None):
    global hel
    hel = 'false'
    if len(username or password) > 1:
        if True:
            try:
                f = open(f'{dir_}\Database\{username}.txt', 'r')
                a = f.readline()
                b = f.readline()
                # print(a,b)
                # print(username,password)
                f.close()
                if password == b:
                    print('hi welcome', username)
                    hel = 'true'
                else:
                    print('password do not match')
            except:
                print('no User found')
        else:
            pass
    else:
        print('Enter a valid pass or username')
    return hel
