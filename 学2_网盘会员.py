# -*- coding:utf-8 -*-
"""
网盘会员
========
同一个网盘有三种用户。
    普通用户：容量 100 GB，下载每秒 100 KB。
    超级会员：容量 5120 GB，下载每秒 20480 KB，还记着会员剩几个月。
    学生会员：也是超级会员，容量 2048 GB，下载每秒 10240 KB，卡片后面多一句「（学生认证）」。

三种用户都要：记名字和已用空间、算下载要几分钟、存文件、打出自己的卡片。
算下载、存文件的方法三种用户一模一样，只是速度和容量的数不同；只有卡片的写法各不相同。
三个类各写一遍，同样的方法就要抄三份。所以用继承：
    CloudDisk 写全部方法：minutes、save、card。
    VipDisk(CloudDisk) 继承它。构造里先写 super().__init__(...)，让父类存好名字和已用空间，
        再加上剩余月数，改掉容量和速度。card 写成会员自己的样子，这叫重写。
    StudentVip(VipDisk) 再继承 VipDisk。card 里先用 super().card() 拿到会员卡片，再接上「（学生认证）」。
三种用户放进一个列表，同样写 d.card()，各调用各的 card，这就是多态。
d.minutes(4096) 和 d.save(8) 用的是同一个继承来的方法，结果不同，是因为各自的速度和容量不同。
minutes 里 size 是 MB，乘 1024 变成 KB，除以每秒的 KB 数 speed，再除以 60 变成分钟。

运行后应看到：

    小林 普通用户 已用 96/100 GB
    阿杰 超级会员 还剩 3 个月 已用 1200/5120 GB
    小美 超级会员 还剩 10 个月 已用 30/2048 GB（学生认证）
    —— 下载 4096 MB 的课程视频 ——
    小林 要 699.1 分钟
    阿杰 要 3.4 分钟
    小美 要 6.8 分钟
    —— 再存 8 GB 的照片 ——
    小林 空间不够，还差 4 GB
    阿杰 存好了，已用 1208 GB
    小美 存好了，已用 38 GB
    —— 谁是会员 ——
    小林 不是会员
    阿杰 是会员
    小美 是会员
    小美的类型就是 VipDisk 吗：False

类清单（名字照写）：
CloudDisk
    __init__(self, user, used)
        存用户名 self.user、已用 GB self.used。容量 self.space = 100，速度 self.speed = 100。
    minutes(self, size)
        下载 size MB 要几分钟：return round(size * 1024 / self.speed / 60, 1)。
    save(self, size)
        再存 size GB。已用加上 size 超过容量：return「小林 空间不够，还差 4 GB」，已用不变。
        没超过：已用加上 size，return「阿杰 存好了，已用 1208 GB」。
    card(self)
        return「小林 普通用户 已用 96/100 GB」。
VipDisk(CloudDisk)
    __init__(self, user, used, months)
        第一句 super().__init__(user, used)。再存 self.months，容量改成 5120，速度改成 20480。
    card(self)
        return「阿杰 超级会员 还剩 3 个月 已用 1200/5120 GB」。
StudentVip(VipDisk)
    __init__(self, user, used, months)
        第一句 super().__init__(user, used, months)。再把容量改成 2048，速度改成 10240。
    card(self)
        return super().card() + "（学生认证）"。

要求：
1. disks = [CloudDisk("小林", 96), VipDisk("阿杰", 1200, 3), StudentVip("小美", 30, 10)]。
2. 四段打印都用 for d in disks。第一段打印 d.card()；第二段算 4096 MB 要几分钟；第三段每人再存 8 GB。
3. 第四段用 isinstance(d, VipDisk) 判断是不是会员。小美是 StudentVip，也算 VipDisk。
4. 最后打印 type(disks[2]) is VipDisk。type 只认对象自己是哪一个类，所以是 False。
5. VipDisk 和 StudentVip 里不要再写 minutes 和 save，它们从 CloudDisk 继承下来就能用。
"""
# TODO ① 写 CloudDisk：__init__、minutes、save、card
class CloudDisk:
    def __init__(self, user, used):
        self.user = user
        self.used = used
        self.space = 100
        self.speed = 100

    def minutes(self, size):
        return round(size*1024/self.speed/60, 1)

    def save(self, size):
        if self.used+size > self.space:
            return self.user+"空间不够，还差"+str(self.used+size-self.space)+"GB"
        self.used+=size
        return self.user+"存好了，已用"+str(self.used)+"GB"

    def card(self):
        return self.user+"普通用户，已用"+str(self.used)+"/"+str(self.space)+"GB"

class VipDisk(CloudDisk):
    def __init__(self, user, used, months):
        super().__init__(user, used)
        self.months = months
        self.space = 5120
        self.speed = 20480

    def card(self):
        return self.user+"超级会员，已用"+str(self.months)+"个月，已用"+str(self.used)+"/"+str(self.space)+"GB"


class StudentVip(VipDisk):
    def __init__(self, user, used, months):
        super().__init__(user, used,months)
        self.space = 2048
        self.speed = 10240

    def card(self):
        return super().card()+"(学生认证)"


cloud_disk = CloudDisk("小林", 96)
vip_disk = VipDisk("阿杰", 1200, 3)
student_disk = StudentVip("小美", 30, 10)

disks = [cloud_disk, vip_disk, student_disk]

print("--- 谁是会员 ---")
for d in disks:
    print(d.card())

print("--- 下载 4096 MB 的课程视频 ---")
for d in disks:
    print(f"{d.user} 要 {d.minutes(4096)} 分钟")

print("--- 再存 8 GB 的照片 ---")
for d in disks:
    print(d.save(8))

print("--- 谁是会员 ---")
for d in disks:
    if isinstance(d, VipDisk):
        print(f"{d.user} 是会员")
    else:
        print(f"{d.user} 不是会员")

print(f"\n小美的类型是 VipDisk 吗: {type(student_disk) is VipDisk}")

vip_disk = VipDisk("阿杰",1200,3)
cloud_disk = CloudDisk("小林",96)
student_disk = StudentVip("小美",30,10)
disk = [vip_disk,cloud_disk,student_disk]
for disk in disk:
    print(disk.card())

for disk in disk:
    if isinstance(disk, VipDisk):
        print(disk.user+"是会员")
    else:
        print(disk.user+"不是会员")

print("小美的类型是VipDisk吗："+str(type(vip_disk)is VipDisk))
print(vip_disk.card())
print(cloud_disk.card())
print(student_disk.card())

print(vip_disk.minutes(4096))
print(vip_disk.save(1000))
# TODO ② 写 VipDisk(CloudDisk)：构造第一句 super().__init__(user, used)，再重写 card


# TODO ③ 写 StudentVip(VipDisk)：构造用 super()，card 里用 super().card()


# TODO ④ 三种用户放进列表，四段 for 循环按样例打印，最后打印 type 的对比
