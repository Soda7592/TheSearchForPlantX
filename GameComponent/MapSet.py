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
Health_3 = 5
MapBy_7 = [6,6,6,6,6,6,6,6,6,6,6,6]
IsMonster = False
chars = 99
Force = False
TokenAct = 0
fuckingwords = ["孕婦打架算圍毆嗎", "導演喊卡之後男優多動一下算強姦嗎", "孕婦打麻將算是聚賭嗎", "松鼠被車輾過是松餅還是鼠餅", "｢沒有事情是絕對的」這句話是絕對的嗎", "導盲犬可以入內是給盲人還是導盲犬看的", "茶算一種蔬菜湯嗎", "買站票的人可以坐火車嗎", "分一半和分兩半是一樣的嗎", "一個半小時是三十分鐘還是九十分鐘", "咖啡是一種豆漿嗎", "射程500公尺的子彈可以在501公尺處接住嗎", "毒藥過期了是更毒了還是沒毒了", "禿頭的人洗頭可以改用洗面乳嗎", "半人馬懷孕的時候小孩在人的肚子裡還是馬的肚子裡", "學法律的人為甚麼叫律師不是法師", "打死自己算強壯還是虛弱呢"]
AllClues = []
StarsMap = ["荒野", "花果山", "天庭", "火燄山", "流沙河"]
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
    print("遊戲地圖設定完畢")
    #print("Map init successed.")


MapInit()

# MapInit()
# print(map_Index)
