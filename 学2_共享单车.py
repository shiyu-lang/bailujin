# -*- coding:utf-8 -*-
"""
共享单车
========
学校投放了一批共享单车。每辆车有自己的车号，还各自记着骑了几次、一共骑了多少分钟。
价钱是所有车一起定的：平时每 15 分钟 1 元，不满 15 分钟也按 15 分钟算。

这个价钱不该在每辆车上各存一份，不然涨价时要一辆一辆去改。
所以价钱 price 和投放数量 count 写成类属性：写在 class 里面、方法外面，所有车共用这一份。
车号、骑行次数、骑行分钟是每辆车自己的，写成 self 上的实例属性。

周末涨价到每 15 分钟 2 元：只改一次 SharedBike.price，所有车一起变。
校队训练车 T001 免费：只给这一辆写 team.price = 0，别的车不受影响。

运行后应看到：

    校园投放了 3 辆单车
    A031 骑 20 分钟，付 2 元
    A031 骑 15 分钟，付 1 元
    B112 骑 50 分钟，付 4 元
    单车 A031：骑了 2 次，共 35 分钟
    单车 B112：骑了 1 次，共 50 分钟
    单车 C007：骑了 0 次，共 0 分钟
    —— 周末每 15 分钟 2 元 ——
    B112 骑 20 分钟，付 4 元
    校队车 T001 骑 30 分钟，付 0 元
    A031 的价目：2
    T001 的价目：0
    校园投放了 4 辆单车

类清单（名字照写）：
SharedBike
    类属性 price = 1
        每 15 分钟几元。所有车共用。
    类属性 count = 0
        投放了几辆车。每造一辆加 1。
    __init__(self, no)
        存车号 self.no。骑行次数 self.rides、骑行分钟 self.minutes 从 0 开始。
        最后写 SharedBike.count = SharedBike.count + 1。
    ride(self, minutes)
        骑一次 minutes 分钟。先算段数：段数 = (minutes + 14) // 15，20 分钟是 2 段，15 分钟是 1 段。
        先加 14 再整除 15，不满一段的零头也能进成一段。
        次数加 1，分钟加上 minutes。return 段数 * self.price。
    __str__(self)
        return「单车 A031：骑了 2 次，共 35 分钟」这样一句。写了它，print(a) 就打出这一句。

要求：
1. 计数写 SharedBike.count = SharedBike.count + 1。
   写成 self.count = self.count + 1，只会给这一辆车加一个它自己的 count，类上的 count 还是 0。
2. ride 里用 self.price 取价钱：这辆车自己有 price 就用自己的，没有就用类的。T001 免费就靠这一点。
3. 三辆车 A031、B112、C007 放进列表 bikes，用 for 循环 print(bike)。
4. 涨价写 SharedBike.price = 2，不要写 a.price = 2。
5. 校队车先造 team = SharedBike("T001")，再写 team.price = 0。
6. 付多少元、打印哪一句，都按样例拼成字符串再 print，数字用 str() 变成字符串。
"""
# TODO ① 写 class SharedBike：先写两个类属性 price 和 count，再写 __init__，最后让 count 加 1
class SharedBike:
    price = 1
    count = 0
    def __init__(self,no):
        self.no = no
        self.rides = 0
        self.minutes = 0
        SharedBike.count = SharedBike.count + 1

    def ride (self,minutes):
        parts = (minutes+14)//15
        self.rides = self.rides + 1
        self.minutes = self.minutes + minutes
        return parts*self.price

    def __str__(self):
        return "单车" + self.no+":骑了" + str(self.rides) + "次，共" + str(self.minutes)+"分钟"


bike1 = SharedBike("A031")
bike2 = SharedBike("B112")
bike3 = SharedBike("C007")

print("校园内投放了"+str(SharedBike.count)+"辆共享单车")

print("A031 骑 20 分钟，付"+str(bike1.ride(20))+"元")
print("B112 骑 15 分钟，付"+str(bike2.ride(15))+"元")
print("C007 骑 50 分钟，付"+str(bike3.ride(50))+"元")

bikes=[bike1,bike2,bike3]
for bike in bikes:
    print(bike)

print("---周末每15分钟两元---")

SharedBike.price = 2
print("A031 骑 20 分钟，付"+str(bike1.ride(20))+"元")

team = SharedBike("T001")
team.price = 0
print("T001的价目"+str(team.price))
print("B112的价目"+str(bike2.price))

print("T001 骑 60 分钟，付"+str(team.ride(60))+"元")
print("B112 骑 15 分钟，付"+str(bike2.ride(15))+"元")

print("校园内投放了"+str(SharedBike.count)+"辆单车")


# TODO ② 写 ride：算段数，次数和分钟加上去，return 段数乘以 self.price
#        接着写在 class SharedBike 里面，缩进 4 格


# TODO ③ 写 __str__：return「单车 A031：骑了 2 次，共 35 分钟」
#        接着写在 class SharedBike 里面，缩进 4 格


# TODO ④ 照样例的顺序写：造三辆车，打印投放数量；骑三次；放进列表打印；
#        涨价，B112 再骑 20 分钟；造校队车并免费，骑 30 分钟；最后打印两辆车的价目和投放数量
