import GameComponent.MapSet as MapSet
import random

# 空域 : 0
# 彗星 : 1
# 矮行星 : 2
# 星際雲 : 3
# 小行星 : 4
# X 行星 : 5

ReasearchString = [[], [], [], [], []]
StarsMap = ["empty", "Comet", "Dwarf", "Interstellar Cloud", "Asteroid"]
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
        return f"There are {count} of {StarsMap[planet]}s in area {start} to {end}."
    elif count == 1:
        return f"There are {count} of {StarsMap[planet]} in area {start} to {end}."
    else:
        return f"There aren't any {StarsMap[planet]}s in area {start} to {end}."


def Scan(area):
    MapSet.months += 4
    if MapSet.map[area] == 5:
        return f"There is a {StarsMap[0]} in area {area+1}."
    return f"There is a {StarsMap[MapSet.map[area]]} in area {area+1}."


def indexs(planet):
    index = []
    for i in range(len(MapSet.map)):
        if MapSet.map[i] == planet:
            index.append(i)
    return index


def nearBy(planet):
    PlanetIndex = indexs(planet)
    p = "1234".replace(str(planet), "")
    for j in range(3):
        for i in PlanetIndex:
            if MapSet.map[(i + 1) % 12] == int(p[j]) or MapSet.map[(i - 1) % 12] == int(
                p[j]
            ):
                ReasearchString[planet].append(
                    f"At least a {StarsMap[planet]} is nearby a {StarsMap[int(p[j])]}"
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
                    f"At least a {StarsMap[planet]} is within three areas of a {StarsMap[int(p[j])]}"
                )


def Direopposite(planet):
    PlanetIndex = indexs(planet)
    p = "1234".replace(str(planet), "")
    for j in range(3):
        for i in PlanetIndex:
            if MapSet.map[(i + 6) % 12] == int(p[j]):
                ReasearchString[planet].append(
                    f"At least {StarsMap[planet]} is in the opposite direction of a {StarsMap[int(p[j])]}"
                )


def NotDireopposite(planet):
    PlanetIndex = indexs(planet)
    p = "1234".replace(str(planet), "")
    for j in range(3):
        for i in PlanetIndex:
            if MapSet.map[(i + 6) % 12] != int(p[j]):
                ReasearchString[planet].append(
                    f"All {StarsMap[planet]} isn't in the opposite direction of a {StarsMap[int(p[j])]}"
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
        MapSet.months -= 2
        return "Correct"
    else:
        MapSet.months += 2
        return "Incorrect"


def PointOutX(index, LeftNear, RightNear):
    MapSet.months += 5
    index_ = MapSet.map.index(5)
    LeftNear_ = MapSet.map[(index_ - 1) % 12]
    RightNear_ = MapSet.map[(index_ + 1) % 12]
    print(index_ + 1, " ", LeftNear_, " ", RightNear_)
    if index == index_ + 1 and LeftNear == LeftNear_ and RightNear == RightNear_:
        return True
    else:
        return False
