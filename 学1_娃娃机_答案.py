# -*- coding:utf-8 -*-
"""娃娃机。"""


class ClawMachine:
    """一台娃娃机。名字、娃娃数、单价、余币、已抓次数都记在这一台自己身上。"""

    def __init__(self, name, dolls, price):
        self.name = name
        self.dolls = dolls
        self.price = price
        self.coins = 0
        self.tries = 0

    def insert(self, n):
        """投 n 个币，return 投完以后的余币。"""
        self.coins = self.coins + n
        return self.coins

    def status(self):
        """return 这一台现在的样子。"""
        return (self.name + "：娃娃 " + str(self.dolls) + " 只，余币 "
                + str(self.coins) + " 个，抓了 " + str(self.tries) + " 次")

    def grab(self):
        """抓一次。币不够就不抓；每抓满 3 次必中一只。return 这一次的结果。"""
        if self.coins < self.price:
            return "币不够，还差 " + str(self.price - self.coins) + " 个"
        self.coins = self.coins - self.price
        self.tries = self.tries + 1
        if self.tries % 3 == 0:
            self.dolls = self.dolls - 1
            return "抓中了！还剩 " + str(self.dolls) + " 只"
        return "差一点，没抓到"


rabbit = ClawMachine("兔兔机", 5, 2)
bear = ClawMachine("小熊机", 8, 3)

print("兔兔机投币后余币：" + str(rabbit.insert(7)))
for i in range(4):
    print("第" + str(i + 1) + "次：" + rabbit.grab())

print("小熊机投币后余币：" + str(bear.insert(9)))
for i in range(3):
    print("第" + str(i + 1) + "次：" + bear.grab())

print(rabbit.status())
print(bear.status())
