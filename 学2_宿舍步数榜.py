# -*- coding:utf-8 -*-
"""
宿舍步数榜
==========
四个室友今天的步数已经写在下面。排出名次，找出达标的人，再把步数折成公里。

运行后应看到：

    ═══ 宿舍步数榜 ═══
    第1名 小周 12400 步 ★
    第2名 老陈 10000 步
    第3名 阿宁 8600 步
    第4名 大川 5300 步
    达标 10000 步： ['小周', '老陈']
    折合公里： [6.0, 8.7, 3.7, 7.0]

函数清单（名字照写）：
1. by_steps(person)
   return 这个人的步数。排序时把它交给 key。
2. rank(board, key)
   key 是传进来的一个函数。return 按 key 从高到低排好的新列表。
3. passed_names(board, goal=10000)
   用 filter 加 lambda 留下步数达到 goal 的人，return 他们的名字列表。刚好 10000 也算。
4. km_list(board)
   用 map 加 lambda 把每个人的步数折成公里：步数 × 0.7 ÷ 1000，round(…, 1)。return 列表。

要求：
1. 名次写成 rank(dorm, by_steps)。by_steps 后面不要加括号，交进去的是函数本身。
   rank 里从高到低排，写 reverse=True。
2. 第 1 名后面加「 ★」。
3. 原来的 dorm 不要改。折合公里按原来的顺序：阿宁、小周、大川、老陈。
4. filter 和 map 得到的还不是列表，要用 list() 包起来，或者用 for 一个一个收进列表，再 return。
5. 每个人是一个字典：person["steps"] 拿步数，person["name"] 拿名字。
"""

dorm = [
    {"name": "阿宁", "steps": 8600},
    {"name": "小周", "steps": 12400},
    {"name": "大川", "steps": 5300},
    {"name": "老陈", "steps": 10000},
]

# TODO ① 定义 by_steps 和 rank
by_steps=lambda person: person["steps"]
print(by_steps(dorm[0]))
to_km =lambda p:round(p["steps"]*0.7/1000,1)
print(str(to_km(dorm[0])),"km")
print(sorted(dorm,key=by_steps))
hits=[7,8,46,12]
print(sorted(hits,key=lambda x: x))
hits=["7","8","46","12"]
print(sorted(hits,key=lambda x: int(x)))
# TODO ② 定义 passed_names：filter + lambda


# TODO ③ 定义 km_list：map + lambda


# TODO ④ 打印名次、达标名单和折合公里
