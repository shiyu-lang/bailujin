# -*- coding: utf-8 -*-
"""
学1 晚自习歌单

需求
1. 歌单从空的开始，歌曲能一首一首加进去。
2. 能知道现在有几首，也能知道最新加入的是哪一首。
3. 能按关键字搜索。名字里带这个关键字的都要找到，一首都没有时结果是空的。
4. 能把某一首挪到最前面。这首歌本来就不在歌单里时，歌单保持原样。
5. 能按现有顺序报幕。每首前面有序号，最后说明一共几首。
6. 能查询某一首是否已经在歌单里。

测试提示
依次加入 Lemon、Viva La Vida、平凡之路、Lover、晴天。
加完是 5 首，最新一首是晴天。
搜 L 得到 Lemon、Viva La Vida、Lover，搜 Z 没有结果。
把平凡之路挪到最前再报幕，它排第一，总共仍是 5 首，Lemon 还在。
"""


# 在这里写。
def add_song(playlist,title):
    print("添加歌曲：",title)
    playlist.append(title)
    return playlist

def latest(playlist):
    return playlist[-1]

def has_song(playlist,title):
    if title in playlist:
        print(title,"已收录")
        return
    print(title,"未收录")

def move_to_top(playlist,title):
    if title in playlist:
        playlist.remove(title)
        playlist.insert(0,title)
    return playlist

def play_all(playlist):
    for i in range(len(playlist)):
        print(str(i+1),".",playlist[i])

def search_keyword(playlist,keyword):
    result = []
    for song in playlist:
        if keyword in song:
           result.append(song)
    return result

playlist = []

add_song(playlist,"lemon")
add_song(playlist,"Viva La Vida")
add_song(playlist,"平凡之路")
add_song(playlist,"Lover")
add_song(playlist,"晴天")

print(playlist)
print("歌曲长度",len(playlist))
print("最后一首歌：",latest(playlist))

has_song(playlist, "Viva La Vida")
has_song(playlist, "Viva")

move_to_top(playlist,"平凡之路")
print(playlist)

play_all(playlist)

print("含有L的款为：",search_keyword(playlist, "L"))

print("含有Z的歌为：",search_keyword(playlist,"Z"))