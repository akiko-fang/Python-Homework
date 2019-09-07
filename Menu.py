#三级菜单
Car = {
    'Big': {
        'A': {1, 2},
        'B': {1, 2}
    },
    'Middle': {
        'A': {1, 2},
        'B': {1, 2}
    },
    'Small': {
        'A': {1, 2},
        'B': {1, 2}
    },
}
Tag = True
while Tag:
    print(Car.keys())
    Choice1 = input('选择菜单，exit退出')
    if(Choice1 == 'exit'):
        break
    elif Choice1 not in Car.keys():
        continue
    else:
        while Tag:
            print(Car[Choice1].keys())
            Choice2 = input('选择菜单，exit退出')
            if (Choice2 == 'exit'):
                Tag = False
                break
            elif Choice2 not in Car[Choice1].keys():
                continue
            else:
                while Tag:
                    print(Car[Choice1][Choice2])
                    Choice3 = input('exit退出')
                    if (Choice3 == 'exit'):
                        Tag = False
                        break

