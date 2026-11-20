# -*- coding:utf-8 -*-
"""
攒机报价
========
给同一台电脑算三种方案的价钱。每个函数只管一件事，总价由 build_quote 调用别的函数算出来。

运行后应看到：

    ════ 攒机报价单 ════
    低调方案：3700 元，分 12 期每期 308.3 元
    拉满方案：4000 元，分 12 期每期 333.3 元
    加配件方案：4920 元，分 24 期每期 205.0 元
    配件小计：900 元

函数清单（名字照写）：
1. rgb_tax(style="低调")
   灯效加价。「拉满」加 300，其他不加。return 加价。
2. part_total(*prices)
   把传进来的几样配件价钱加起来，return 总数。一样都没有时是 0。
3. build_quote(cpu, gpu, *others, **opts)
   others 收进来的是处理器和显卡以外的配件价钱，opts 收进来的是灯效和运费。
   总价 = 处理器 + 显卡 + 配件小计 + 灯效加价 + 运费。
   配件小计调用 part_total。灯效加价调用 rgb_tax，灯效从 opts.get("style", "低调") 取。
   运费是 opts.get("ship", 0)，没写就是 0。return 总价。
4. monthly(total, months=12)
   每期 = 总价 / 期数，写成 round(总价 / 期数, 1)，保留一位小数。
5. quote_line(name, total, months=12)
   return「低调方案：3700 元，分 12 期每期 308.3 元」这样一句。每期调用 monthly。

要求：
1. 处理器 1200 元，显卡 2500 元。
2. 低调方案写成 build_quote(1200, 2500)。
3. 拉满方案用关键字实参 style="拉满" 传灯效。
4. 加配件方案：配件写在列表 cart = [400, 300, 200] 里，选项写在字典 extra = {"style": "拉满", "ship": 20} 里。
   调用写成 build_quote(1200, 2500, *cart, **extra)。星号把列表和字典拆开再传进去。这一行分 24 期。
5. 最后打印配件小计，同样写 part_total(*cart)。
6. 函数里不要 print，打印都写在下面的主程序里。
"""
# TODO ① 定义 rgb_tax 和 part_total
def rgb_tax(style='低调'):
    if  style =="拉满":
        return 300
    return 0
def part_total(*prices):
    total = 0
    for price in prices:
        total += price
    return total

def show_opts(**opts):
    print(opts.get("style","低调"))
    print(opts.get("ship",0))

def build_quote(cpu_price, gpu_price, *others, **opts):
    total = cpu_price+ gpu_price+part_total(*others)
    total += rgb_tax(opts.get("style","低调"))
    total += opts.get("ship",0)
    return total

def monthly(total, months=12):
    return round(total/months,1)

def quote_line(name, total, months=12):
    return name +"："+str(total)+"元，分"+str(months)+"期每期"+str(monthly(total, months))+"元"

print(rgb_tax())
print(rgb_tax("拉满"))
print(part_total(400,300,200))
show_opts(style="拉满",ship=20)
show_opts()

print("-"*10+"报价单如下"+"-"*10)

print("低调方案:",str(build_quote(1200,2500))+"元，分 12 期每期"+str(monthly(build_quote(1200,2500)))+"元")
print("拉满方案："+str(build_quote(1200,2500,style="拉满"))+"元，分 12 期每期"+str(monthly(build_quote(1200,2500,style="拉满")))+"元")

cart = [400, 300, 200]
extra = {"style":"拉满","ship":20}
print("加配件方案: " + str(build_quote(1200,2500,4300,style="拉满")) + " 元, 分 24 期每期 " + str(monthly(build_quote(1200,2500,4300,style="拉满"), 24)) + " 元")
print("配件小计: " + str(part_total(*cart)) + " 元")
# TODO ② 定义 build_quote：调用 part_total 和 rgb_tax


# TODO ③ 定义 monthly 和 quote_line


# TODO ④ 算出三种方案，打印报价单和配件小计
