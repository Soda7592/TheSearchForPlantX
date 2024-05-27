import GameComponent.MapSet as MapSet
import random
import GameComponent.StartClue as clue

# 空域 : 0
# 彗星 : 1
# 矮行星 : 2
# 星際雲 : 3
# 小行星 : 4
# X 行星 : 5

ReasearchString = [[], [], [], [], []]
StarsMap = ["荒野", "花果山", "天庭", "火燄山", "流沙河"]
r = random.randint(0, 999)
random.seed(r)


def Survey(start, end, planet):
    start = min(start, end)
    end = max(start, end)
    if end - start >= 3:
        MapSet.months += 3
    else:
        MapSet.months += 4
    count = 0
    for i in range(start, end):
        if MapSet.map[i] == planet:
            count += 1
    if count > 1:
        return f"區域 {start} 到 {end} 中存在 {count} 座{StarsMap[planet]}"
    elif count == 1:
        return f"區域 {start} 到 {end} 中存在 {count} 座{StarsMap[planet]}"
    else:
        return f"區域 {start} 到 {end} 不存在{StarsMap[planet]}"


def Scan(area):
    MapSet.months += 4
    if MapSet.map[area] == 5:
        return f"> 存在{StarsMap[0]}"
    return f"> 存在{StarsMap[MapSet.map[area]]}"


def indexs(planet):
    index = []
    for i in range(len(MapSet.map)):
        if MapSet.map[i] == planet:
            index.append(i)
    return index

def PlanetNum():
    print("***********")
    for i in range(len(StarsMap)) :
        print(f"{StarsMap[i]}編號為{i}")
    print("***********\n")

def nearBy(planet):
    PlanetIndex = indexs(planet)
    p = "1234".replace(str(planet), "")
    for j in range(3):
        for i in PlanetIndex:
            if MapSet.map[(i + 1) % 12] == int(p[j]) or MapSet.map[(i - 1) % 12] == int(
                p[j]
            ):
                ReasearchString[planet].append(
                    f"至少有一個{StarsMap[planet]} is nearby a {StarsMap[int(p[j])]}"
                )


def nearBy3(planet):
    PlanetIndex = indexs(planet)
    p = "1234".replace(str(planet), "")
    for j in range(3):
        for i in PlanetIndex:
            if MapSet.map[(i + 3) % 12] == int(p[j]) or MapSet.map[(i - 3) % 12] == int(
                p[j]
            ):
                ReasearchString[planet].append(
                    f"至少有一個{StarsMap[planet]}相鄰{StarsMap[int(p[j])]}的距離在三個區域內"
                )


def Direopposite(planet):
    PlanetIndex = indexs(planet)
    p = "1234".replace(str(planet), "")
    for j in range(3):
        for i in PlanetIndex:
            if MapSet.map[(i + 6) % 12] == int(p[j]):
                ReasearchString[planet].append(
                    f"至少有一個{StarsMap[planet]}是正對著{StarsMap[int(p[j])]}"
                )


def NotDireopposite(planet):
    PlanetIndex = indexs(planet)
    p = "1234".replace(str(planet), "")
    for j in range(3):
        for i in PlanetIndex:
            if MapSet.map[(i + 6) % 12] != int(p[j]):
                ReasearchString[planet].append(
                    f"所有的{StarsMap[planet]}皆不在{StarsMap[int(p[j])]}的對面"
                )
            else:
                break


def Research():
    MapSet.months += 2
    for i in range(1, 5):
        nearBy(i)
        nearBy3(i)
        Direopposite(i)
        NotDireopposite(i)
    return ReasearchString


def SubmitPaper(area, planet):
    if MapSet.map[area] == planet:
        if MapSet.Health_3 < 3 :
            MapSet.Health_3 += 1
        return "\n正確，唐三藏回復了一點血量\n"
    else:
        MapSet.months += 2
        return "\n不正確\n"

def randMonster() :
    monster = random.randint(0, 1000)
    if monster <= 650 and MapSet.IsMonster == False:
        MapSet.IsMonster = True
        print("\n出現妖怪! 請保護唐三藏\n")       

def AttackMonster() :
    if MapSet.IsMonster == True:
        MapSet.IsMonster = False
        print("\n成功擊退妖怪\n")
    elif MapSet.IsMonster == False:
        print("\n沒有妖怪啊，你在幹嘛= = ?\n")
    MapSet.months += 2    

def Survey_5(start, end, planet) :
    s = random.randint(0, 1000)
    if s <= 600 :
        print('\n\033[31m',Survey(start, end, planet),'\033[0m')
        area = random.randint(0,11)
        if MapSet.map[area] == 5 :                                                 print(f"探查超成功!我還知道了區域{area}是{StarsMap[MapSet.map[0]]}\n")
        else :
            print(f"探查超成功!我還知道了區域{area}是{StarsMap[MapSet.map[area]]}\n")
    else :
        MapSet.months += 4
        print("\n失敗，這次的搜索一點幫助都沒有\n")

def Scan_5(area) :
    s = random.randint(0, 1000)
    if s<= 600 :
        print('\n\033[31m',Scan(area), '\033[0m')
        area = random.randint(0, 11)
        if MapSet.map[area] == 5 :
            print(f"探查超成功!我還知道了區域{area}是{StarsMap[MapSet.map[0]]}\n")
        else :
            print(f"探查超成功!我還知道了區域{area}是{StarsMap[MapSet.map[area]]}\n")
    else :
        MapSet.months += 4
        print("\n失敗，這次的搜索一點幫助都沒有\n")

def Survey_8(start, end, planet) :
    s = random.randint(0, 1000)
    if s <= 600 :
        print('\n\033[31m', Survey(start, end, planet), '\033[0m')
        print(f"探查成功!\n")
    else :
        MapSet.months += 4
        print("\n失敗，這次的搜索一點幫助都沒有\n")
        print("豬八戒 : ", random.choice(MapSet.fuckingwords))

def Scan_8(area) :
    s = random.randint(0, 1000)
    if s <= 600 :
        print('\n\033[31m',Scan(area),'\033[0m')
        print("探查成功\n")
    else :
        MapSet.months += 4
        print("\n失敗，這次的搜索一點幫助都沒有\n")
        print("豬八戒 : ", random.choice(MapSet.fuckingwords))

def DrawMap(area, planet) :
    area -= 1
    MapSet.months += 1
    MapSet.MapBy_7[area] = planet
    
def GetClue():
    clue.GiveClue(1)
    #MapSet.months += 2
    #print("GetClue !")
    print("\n")
    return MapSet.AllClues

def PointOutX(index, LeftNear, RightNear):
    MapSet.months += 5
    index_ = MapSet.map.index(5)
    LeftNear_ = MapSet.map[(index_ - 1) % 12]
    RightNear_ = MapSet.map[(index_ + 1) % 12]
    #print(index_ + 1, " ", LeftNear_, " ", RightNear_)
    if index == index_ and LeftNear == LeftNear_ and RightNear == RightNear_:
        return True
    else:
        return False
