# -*- coding:utf-8 -*-
"""
电量管家
========
旁边的 digi_tools.py 里已经写好三个数码小工具。用三种 import 把它们拿进来，
再写一个会记次数的查电量函数。

运行后应看到：

    充电宝能充几次： 1
    2GB 更新包要下几分钟： 3.4
    第 1 次查电量：剩 80%，电量健康
    第 2 次查电量：剩 35%，有点焦虑
    第 3 次查电量：剩 15%，找充电宝！
    一共查了 3 次

digi_tools.py 里有：
    charge_times(powerbank, phone)   充电宝能给手机充几次
    download_minutes(size_mb, speed) 下载要几分钟
    battery_badge(left)              按剩余电量给一个状态

要求：
1. 三种 import 都要写：
       import digi_tools
       from digi_tools import download_minutes
       import digi_tools as dt
2. 充电次数写成 digi_tools.charge_times(10000, 4000)，前面带模块名。
3. 下载时间写成 download_minutes(2048, 10)。from 拿进来的名字，直接写函数名。
4. 写 check_battery(left)。文件里已经有 checks = 0。
   函数里先写 global checks，再把 checks 加 1。电量状态调用 dt.battery_badge(left)。
   每查一次打印一行：第 1 次查电量：剩 80%，电量健康
5. 依次查 80、35、15，最后打印一共查了几次。
6. 和 digi_tools.py 放在同一个文件夹里运行。不要改 digi_tools.py。
"""

checks =0

# TODO ① 写三种 import
import digi_tools
from digi_tools import download_minutes
import digi_tools as dt
# TODO ② 打印充电次数和下载时间
print(digi_tools.charge_times(10000, 4000))
print(digi_tools.battery_badge(60))
print(download_minutes(2048,10))

def check_battery(left):
    global checks
    checks +=1
    badge=dt.battery_badge(left)
    text="第"+str(checks)+"次查电量："
    print(text+"剩"+str(left)+"%,"+badge)

check_battery(80)
check_battery(35)
check_battery(15)
print("一共查了"+str(checks)+"次")


# TODO ③ 写 check_battery(left)：global 计数，调用 dt.battery_badge


# TODO ④ 查三次电量，打印一共查了几次
