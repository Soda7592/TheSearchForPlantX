import random

"""
宇宙有 12 個區域

每個區域有一類天體

兩個區域有彗星、一個有矮行星、兩個有星際雲、四個有小行星、一個有 X 行星以及兩個區域真正沒有天體

- 彗星只會出現在質數區域
- 矮行星與 X 行星不相鄰
- X 行星被觀察時會以沒有天體的狀態出現
"""
# 每片區域只有一個天體

# 天體
# 空域 : 0 (2片)
# 彗星 : 1 (2顆)
# 矮行星 : 2 (1顆)
# 星際雲 : 3 (2片)
# 小行星 : 4 (4顆)
# X 行星 : 5 (1個)

r = random.randint(0, 999)
random.seed(r)
map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
map_Index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime = [1, 2, 4, 6, 10]
months = 0


def Set_comet():
    x, x_ = (1, 1)
    while x == x_:
        x = random.choice(prime)
        x_ = random.choice(prime)
    map[x] = 1
    map[x_] = 1
    map_Index.remove(x)
    map_Index.remove(x_)


def Set_dwarf():
    x = random.choice(map_Index)
    map[x] = 2
    map_Index.remove(x)


def Set_interstellar_cloud():
    x, x_ = (1, 1)
    while True:
        x = random.randint(0, 11)
        x_ = random.randint(0, 11)
        if x != x_ and map[x] == 0 and map[x_] == 0:
            map[x] = 3
            map[x_] = 3
            map_Index.remove(x)
            map_Index.remove(x_)
            break


def Set_X_planet():
    x = random.choice(map_Index)
    while map[x - 1] == 2 or map[x - 1] == 2:
        x = random.choice(map_Index)
    map[x] = 5
    map_Index.remove(x)


def Set_asteroid():
    x = 1
    for i in range(4):
        x = random.choice(map_Index)
        map[x] = 4
        map_Index.remove(x)


def MapInit():
    Set_comet()
    Set_interstellar_cloud()
    Set_dwarf()
    Set_X_planet()
    Set_asteroid()
    print("Map init successed.")


MapInit()

# MapInit()
# print(map_Index)
