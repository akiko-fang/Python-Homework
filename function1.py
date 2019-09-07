# 修改文件
import os
def AlterFile(Filename, BeforeAlter, AfterAlter):
    with open(Filename, mode='r') as f1, \
            open(Filename + '1', mode='w') as f2:
        for line in f1:
            if BeforeAlter in line:
                line = line.replace(BeforeAlter, AfterAlter)
            f2.write(line)
    os.remove(Filename)
    os.rename(Filename+'1',Filename)
# 判断字符串中 数字、字母、空格、其他的个数
def CountString(str):
    num = 0
    alpha = 0
    spacing = 0
    other = 0
    for i in str:
        if i.isdigit():
            num += 1
        elif i.isalpha():
            alpha += 1
        elif i.isspace():
            spacing += 1
        else:
            other += 1
    print(num, alpha, spacing, other)
# 判断对象长度是否大于5
def CountLength(arg):
    count = 0
    for item in arg:
        count += 1
        if count > 5:
            return True
    return False
# 判断列表长度是否大于2，保留前两位返回
def NewList(l1):
    count = 0
    l2 = list()
    for item in l1:
        count += 1
        if (count > 2):
            return l2
        else:
            l2.append(item)
    return l2
# 奇数索引对应元素
def FindOdd(arg):
    oddl = list()
    for i, item in enumerate(arg):
        if i % 2 == 1:
            oddl.append(item)
    return oddl
# 字典value仅保留前两个长度
def NewDict(dict):
    for key in dict.keys():
        dict[key] = NewList(dict[key])
    return dict

print(CountString('a1 B2 *'))
print(CountLength((1, 2, 3, 4, 5, 6)))
print(NewList([1, 2, 3, 4, 5]))
print(FindOdd([0, 1, 2, 3]))
print(NewDict({'1': [1, 2, 3, 4], '2': [1, 2]}))
