# Users记录用户信息（姓名，密码，余额），UserName记录用户名，BlackList记录黑名单用户，ShopList是可买商品信息
File = list()
Users = list()
UserName = list()
Blacklist = list()
ShopList = [['Macbook',9999],['iphone',6666],['bike',300]]

#读取文件用户信息到 Users 和 UserName
with open('G:\\python\\user.txt',mode='r',encoding='ANSI') as fuser:
    for line in fuser.readlines():
        File.append(line)
        line=line.strip('\n')
        UserName.append(line.split('|')[0])
        Users.append({'name':line.split('|')[0],'password':line.split('|')[1],'amount':int(line.split('|')[2])})

while(True):
    print('请输入功能编号：')
    choice = int(input('1:注册\n2:登陆\n3:退出\n'))

    # 注册，会检查用户名重复情况，注册成功会加入文件和两个list
    if (choice == 1):
        Name = input('请输入用户名：\n')
        while Name in UserName:
            Name = input("用户名重复，请重新输入：\n")
        Password = input('请输入密码：\n')
        Password2 = input('请再次输入密码：\n')
        if (Password != Password2):
            print('两次密码不一致')
            continue
        Amount = input('请输入工资：\n')
        with open('G:\\python\\user.txt',mode='a',encoding='ANSI') as fuser:
            fuser.writelines(Name+'|'+Password+'|'+Amount+'\n')
        Str = str(Name)+'|'+str(Password)+'|'+str(Amount)+'\n'
        File.append(Str)
        UserName.append(Name)
        Users.append({'name':Name,'password':Password,'amount':Amount})

    # 登陆：首先check用户名存在，其次check用户名在黑名单的
    elif (choice == 2):
        #不存在，退出
        Name = input('请输入用户名：\n')
        if Name not in UserName:
            print("用户名不存在\n")
            continue
        #黑名单，改名
        elif Name in Blacklist:
            print('密码错误三次请修改用户名\n')
            NewName = input('新用户名\n')
            #更改文件和两个list
            UserName[UserName.index(Name)] = NewName
            for item in Users:
                if(item['name'] == Name):
                    item['name'] = NewName
                    Password = item['password']
                    Amount = item['amount']
            for line in File:
                if line.split('|')[0] == Name:
                    File.remove(line)
                    Str = str(NewName) + '|' + str(Password) + '|' + str(Amount) + '\n'
                    File.append(Str)
            with open('G:\\python\\user.txt', mode='w', encoding='ANSI') as fuser:
                fuser.writelines(File)
        #用户名没问题，检查密码
        else:
            for useritem in Users:
                if (useritem['name'] == Name):
                    Password = input('请输入密码：\n')
                    passerror = 0
                    #密码check，三次不对加入黑名单
                    while (useritem['password'] != Password):
                        if (passerror == 2):
                            print('密码错误三次')
                            Blacklist.append(Name)
                            break
                        passerror += 1
                        Password = input('密码错误重新输入：\n')
                    #成功登陆开始购物
                    BuyTag = False
                    BuyList = [] #Buytag用来记录是否买东西，Buylist记录买了什么
                    while(useritem['password'] == Password):
                        #打印商品列表
                        for i,item in enumerate(ShopList):
                            print(i+1,item[0],int(item[1]))
                        buy = int(input('请输入购买编号，按0退出\n'))
                        if(buy==0): #退出购买，输出已买东西列表
                            if(BuyTag):
                                for item in BuyList:
                                    print(item+'\n')
                            break
                        if(buy!=0): #购买，检查余额并扣款
                            if(int(useritem['amount']<ShopList[buy-1][1])):
                                print('余额不足\n')
                                break
                            else:
                                print('购买成功\n')
                                BuyTag = True
                                BuyList.append(ShopList[buy-1][0])
                                #修改余额
                                useritem['amount'] -= ShopList[buy-1][1]
                                for line in File:
                                    if line.split('|')[0] == useritem['name']:
                                        File.remove(line)
                                        Str = str(useritem['name']) + '|' + str(useritem['password']) + '|' + str(useritem['amount']) + '\n'
                                        File.append(Str)
                                with open('G:\\python\\user.txt', mode='w', encoding='ANSI') as fuser:
                                    fuser.writelines(File)
                        continue
    else:
        break

