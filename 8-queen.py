#八皇后
def conflict(placed,pos):
    if pos in placed: #同列
        return True
    for i in range(len(placed)):
        if abs(pos - placed[i]) == abs(len(placed)-i): #同对角线，即摆放差值=行差
            return True
    return False
def queen(num=8,placed=[]):
    for i in range(num):
        if not conflict(placed,i):
            if len(placed) == num-1:
                yield [i,]
            else:
                for j in queen(num,placed+[i,]):
                    yield [i,] + j
res = list(queen())
print(len(res))
print(res)