#合并表达
#变大写
names = ['albert', 'james', 'kobe', 'kd']
newname = map(lambda x:x.upper(), names)
print(list(newname))
#过滤shenjing结尾名字
names = ['albert', 'jr_shenjing', 'kobe', 'kd']
newname = filter(lambda x:x[-8:]!='shenjing', names)
print(list(newname))
#求a.txt最长行的长度
max = 0
with open('G:\python\\a.txt', mode='r') as f:
    for line in f.readlines():
        if len(line.strip())>max:
            max = len(line.strip())
print(max)
#对于shoppinglist求总共花多少钱，打印商品信息，求单价大于10000
shop = list()
count = 0
with open('G:\python\\shopping.txt', mode='r') as f:
    for line in f.readlines():
        shop.append({'name':line.strip().split(',')[0],\
                     'price':int(line.strip().split(',')[1]),\
                     'count':int(line.strip().split(',')[2])})
        count += int(line.strip().split(',')[1]) * int(line.strip().split(',')[2])
print(count)
print(shop)
print(list(filter(lambda x: x['price']>10000, shop)))