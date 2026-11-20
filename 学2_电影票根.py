# -*- coding: utf-8 -*-
"""
学2 电影票根

需求
1. 一张票在生成时记下片名、座位和价格，这三项之后不能再改。
2. 一沓票能逐张显示，每张都能看到片名、座位和价格。
3. 能算出一沓票的总价。
4. 能从一沓票里找出最便宜的一张。
5. 能按预算筛出价格不超过预算的那些票。

测试提示
四张票是：星际穿越 7排6座 39.9，流浪地球3 IMAX厅1排2座 59.9，
情书 4排8座 29.9，海上钢琴师 5排10座 45.0。
总价是 174.7 元，最便宜的是情书。40 元以内是星际穿越和情书。
"""


# 在这里写。
class Ticket:
    def __init__(self,film,seat,price):
        self.record = (film,seat,price)

    def show(self):
        film,seat,price = self.record
        print(film,seat,price)

    def price(self):
        return self.record[2]


    def label(self):
        return self.record[0] + "."+self.record[1]

def total(tickets):
    total = 0
    for ticket in tickets:
        total += ticket.price()
    return total

def find_cheapest(tickets):
    min_ticket = tickets[0]
    for ticket in tickets:
        if ticket.price() < min_ticket.price():
            min_ticket = ticket
    return min_ticket
def filter_by_seat(tickets,budgest):
    seats = []

tickets =[
  Ticket( "星际穿越","7排6座",39.9),
  Ticket( "流浪地球3","IMAX厅1排2座",59.9),
  Ticket( "情书","4排8座",29.9),
  Ticket( "海上钢琴师","5排10座",45.0),
]
for t in tickets:
    t.show()

print("合计",total(tickets))