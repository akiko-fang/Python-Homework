#一旦某函数执行，则将函数执行时间写入到日志文件中，日志文件路径可以指定。
import time
def log(fileroad):
    def outer(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            ex_time = end_time - start_time
            with open(fileroad, mode='a') as f:
                f.write(str(ex_time)+'\n')
            print(ex_time)
            return res
        return wrapper
    return outer
#为多个函数加上认证的功能,登录成功一次，无需重复登录,超时重复登陆
LoginFlag = False
TimeFlag = False
logtime = 0
def auth(fileroad):
    def outer(func):
        def wrapper(*args, **kwargs):
            global LoginFlag,TimeFlag,logtime
            Waitingtime = time.time() - logtime
            if LoginFlag and Waitingtime < 3:
                res = func(*args, **kwargs)
                return res
            else:
                with open(fileroad, mode='r') as f:
                    dict = eval(f.read())
                username = input('UserName>>').strip()
                password = input('Password>>').strip()
                if username == dict['name'] and password == dict['password']:
                    LoginFlag = True
                    logtime = time.time()
                else:
                    print('login fail')
                res = func(*args, **kwargs)
                return res
        return wrapper
    return outer
#eval的用法：执行字符串
with open('G:\python\\user.txt', mode='r') as f:
    dict = eval(f.read())
print(dict)
