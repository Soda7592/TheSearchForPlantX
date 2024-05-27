import GameComponent.MapSet as MapSet
import random

# 0. X 行星不與 XX 行星正對 (包含小行星/彗星/星際雲)
# 1. X 行星在 XX 行星 2~3 格以內 (包含彗星/星際雲)
# 2. X 行星不與 XX 行星相鄰 (星際雲/彗星)
ConfString = []
StarsMap = ["花果山", "天庭", "火燄山", "流沙河"]
#r = random.randint(0, 999)
random.seed(10)
# 天體
# 空域 : 0 (2片)
# 彗星 : 1 (2顆)
# 矮行星 : 2 (1顆)
# 星際雲 : 3 (2片)
# 小行星 : 4 (4顆)
# X 行星 : 5 (1個)


def Set_Xconf():
    # conf = random.randint(0, 2)
    index = MapSet.map.index(5)
    # print("index : ", index)

    # 0. X 行星不與 XX 行星正對 (包含小行星/彗星/星際雲)
    for i in [1, 3, 4]:
        establish = True
        for j in range(len(MapSet.map)):
            if MapSet.map[j] == i:
                if MapSet.map[(j + 6) % 12] == index:
                    establish = False
                    break
            else:
                continue
        if establish:
            ConfString.append(
                f"真經不正對{StarsMap[i-1]}"
                #f"The X planet is not in the opposite direction of the {StarsMap[i-1]}"            
)

    # 1. X 行星在 XX 行星 2~3 格以內 (包含小行星/彗星/星際雲)
    for i in [1, 3]:
        establish_2 = False
        establish_3 = False
        for j in range(len(MapSet.map)):
            if MapSet.map[j] == i:
                if abs(j - index) <= 2:
                    establish_2 = True
                    break
                elif abs(j - index) <= 3:
                    establish_3 = True
                    break
        if establish_2:
            ConfString.append(f"真經在{StarsMap[i-1]}2格以內")
        elif establish_3:
            ConfString.append(f"真經在{StarsMap[i-1]}3格以內")

    # 2. X 行星不與 XX 行星相鄰 (星際雲/彗星)
    for i in [1, 3]:
        establish = True
        for j in range(len(MapSet.map)):
            if MapSet.map[j] == i:
                if abs(j - index) == 1:
                    establish = False
                    break
        if establish:
            ConfString.append(f"真經不與{StarsMap[i-1]}相鄰")


Set_Xconf()

def X() :
    randConf = random.choice(ConfString)
    print(randConf)
    #print(ConfString)
# elif conf == 1 :
#     targetPlanet = random.choice([1,3,4])

# elif conf ==2:
#     targetPlanet = random.choice([1,3])
# if conf == 0 :
