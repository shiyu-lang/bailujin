# -*- coding:utf-8 -*-
"""
快递柜
======
驿站门口有一排快递柜。快递员放进一件快递，柜子生成一个取件码，用短信发给收件人。
取件码要藏在柜子里，谁都不能直接看，也不能直接改；只能在柜子上输入取件码，输对了才开门。
连续输错 3 次，柜子锁定，再输对也打不开，要找驿站工作人员。
输错了几次、柜子是不是空的，可以给外面看，但不能让外面改。

这就是封装：数据藏在对象里面，外面只能走对象给的「正门」，也就是方法。
    藏起来：属性名前面加两个下划线，写成 self.__code。在类外面读 a07.__code 会报 AttributeError；
            在类外面写 a07.__code = 0 不报错，可那只是给对象新加了一个属性，柜子里的取件码不变。
    只能看：方法上面加一行 @property，外面写 a07.wrong 就能读到，不用加括号；
            写 a07.wrong = 0 会报 AttributeError，改不了。

取件码从 2048 开始，每放一件加 1。「下一张取件码」是所有柜子共用的，写成类属性 next_code。

运行后应看到：

    短信：A03 取件码 2048
    短信：A07 取件码 2049
    取件码不对，还能试 2 次
    A03 开门，请取走 蓝牙耳机
    A03 空着吗：True
    取件码不对，还能试 2 次
    取件码不对，还能试 1 次
    取件码不对，A07 已锁定
    A07 已锁定，请找驿站工作人员
    A07 输错次数：3
    取件码藏在柜子里，外面看不到
    输错次数只能看，不能改

类清单（名字照写）：
Locker
    类属性 next_code = 2048
    __init__(self, no)
        存柜号 self.no。快递 self.__parcel 是 ""，取件码 self.__code 是 0，输错次数 self.__wrong 是 0。
        后面这三个，名字前面都是两个下划线。
    put(self, parcel)
        把 parcel 存进 self.__parcel。取件码用 Locker.next_code，存进 self.__code，再让 Locker.next_code 加 1。
        return 这一件的取件码，主程序拿它「发短信」。
    pick(self, code)
        已经输错 3 次：return「A07 已锁定，请找驿站工作人员」。A07 换成这一格的 self.no。
        code 和 self.__code 不一样：输错次数加 1。加完正好是 3，return「取件码不对，A07 已锁定」；
            不到 3，return「取件码不对，还能试 2 次」这样一句，2 是 3 减去输错次数。
        输对了：先记下快递名，再把快递、取件码、输错次数都清回一开始的样子，
            return「A03 开门，请取走 蓝牙耳机」。
    wrong（上面写 @property）
        return self.__wrong。
    empty（上面写 @property）
        柜子里没有快递就是空的：return self.__parcel == ""。

要求：
1. 两格柜子：a03 = Locker("A03")，a07 = Locker("A07")。A03 放蓝牙耳机，A07 放机械键盘。
   put 交回的取件码存进 code1、code2，打印两条短信。
2. A03 先输 1234，再输 2048；再打印 A03 是不是空的。读 a03.empty 不加括号。
3. A07 依次输 1111、2222、3333、2049。第 4 次虽然输对了，柜子已经锁了。再打印 A07 输错次数。
4. 用 try 和 except AttributeError 试两件事：print(a07.__code) 和 a07.wrong = 0。
   报错时分别打印「取件码藏在柜子里，外面看不到」「输错次数只能看，不能改」。
   try 下面的语句出错时，程序不停下，转去执行 except 下面的语句。一段写四行：
       try:
           print(a07.__code)
       except AttributeError:
           print("取件码藏在柜子里，外面看不到")
"""
# TODO ① 写 class Locker：类属性 next_code，__init__ 里三个属性名前面加两个下划线
class Locker:
    next_code = 2048
    def __init__(self, no):
        self.no = no
        self.__parcel = ""
        self.__code = 0
        self.__wrong = 0

    def put(self, parcel):
        self.__parcel = parcel
        self.__code =Locker.next_code
        Locker.next_code += 1
        return self.__code



    def pick(self, code):
        if self.__wrong >= 3:
            return self.no + " 已锁定，请找驿站工作人员"
        if code != self.__code:
            self.__wrong += 1
            if self.__wrong == 3:
                return "取件码不对，" + self.no + " 已锁定"
            else:
                remain = 3 - self.__wrong
                return "取件码不对，还能试 " + str(remain) + " 次"
        parcel = self.__parcel
        self.__code = 0
        self.__parcel = ""
        self.__wrong = 0
        return self.no + " 开门，请取走 " + parcel


    @property
    def wrong(self):
        return self.__wrong


    @property
    def empty(self):
        return self.__parcel ==""

a03 = Locker("A03")
a07 = Locker("A07")
code1 = a03.put("蓝牙耳机")
code2 = a07.put("机械键盘")
print("短信：A03 取件码 " + str(code1))
print("短信：A07 取件码 " + str(code2))

print(a03.pick(1234))
print(a03.pick(2048))
print("A03 空着吗：" + str(a03.empty))

print(a07.pick(1111))
print(a07.pick(2222))
print(a07.pick(3333))
print(a07.pick(2049))
print("A07 输错次数：" + str(a07.wrong))

try:
    print(a07.__code)
except AttributeError:
    print("取件码藏在柜子里，外面看不到")
try:
    a07.wrong = 0
except AttributeError:
    print("输错次数只能看，不能改")
# TODO ② 写 put：存快递、发取件码，next_code 加 1
#        接着写在 class Locker 里面，缩进 4 格


# TODO ③ 写 pick：先看锁没锁，再比对取件码，输对了清回去
#        接着写在 class Locker 里面，缩进 4 格


# TODO ④ 写两个只读属性 wrong 和 empty：每个上面一行 @property
#        接着写在 class Locker 里面，缩进 4 格


# TODO ⑤ 按要求放快递、取快递，最后用 try 试一试外面能不能看、能不能改
