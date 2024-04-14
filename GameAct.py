import MapSet

StarsMap = ["empty", "Comet", "Dwarf", "Interstellar Cloud", "Asteroid"]
# 空域 : 0
# 彗星 : 1
# 矮行星 : 2
# 星際雲 : 3
# 小行星 : 4
# X 行星 : 5


def Survey(start, end, planet):
    start = min(start, end)
    end = max(start, end)
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
    return f"There is a {StarsMap[MapSet.map[area]]} in area {area}."


# 相鄰、正對、幾格之內
# 彗星、小行星、矮行星、星際雲
# O 行星(不)與 X 行星正對
# 至少有一個 O 行星(不)與 X 行星相鄰 (V)
# O 行星與 X 行星在2~3格以內 (V)

ReasearchString = [[], [], [], [], []]


def indexs(planet):
    index = []
    for i in range(len(MapSet.map)):
        if MapSet.map[i] == planet:
            index.append(i)
    return index


def nearBy(planet):
    PlanetIndex = indexs(planet)
    Stringindex = 0
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
    Stringindex = 0
    p = "1234".replace(str(planet), "")
    for j in range(3):
        for i in PlanetIndex:
            if MapSet.map[(i + 3) % 12] == int(p[j]) or MapSet.map[(i - 3) % 12] == int(
                p[j]
            ):
                ReasearchString[planet].append(
                    f"There is at least a {StarsMap[planet]} is within three areas of a {StarsMap[int(p[j])]}"
                )


def Research():
    pass


def SubmitPaper(area, planet):
    if MapSet.map[area] == planet:
        return True
    else:
        return False


def PointOutX(index, LeftNear, RightNear):
    index_ = MapSet.map.index(5)
    LeftNear_ = MapSet.map[(index_ - 1) % 12]
    RightNear_ = MapSet.map[(index_ + 1) % 12]
    if index == index_ and LeftNear == LeftNear_ and RightNear == RightNear_:
        return True
    else:
        return False


if __name__ == "__main__":
    nearBy(1)
    nearBy3(1)
    print(ReasearchString)
    # while True:
    #     print(
    #         " - 1 => Survey (start, end, planet)\n",
    #         "- 2 => Scan (area)\n",
    #         "- 3 => Research (Couldn't work correctly now.)\n",
    #         "- 4 => SubmitPaper (area, planet)\n",
    #         "- 5 => PointOutX (AreaOfX, LeftNearPlanet, RightNearPlaner)\n",
    #         "- 6 => Help\n",
    #         "- 7 => ExitAndGetResult\n",
    #     )
    #     m = input("Input a Action > ")
    #     if m == "1":
    #         start = int(input("Start :"))
    #         end = int(input("End :"))
    #         planet = int(input("Planet : "))
    #         print(Survey(start, end, planet))
    #     elif m == "2":
    #         area = int(input("Area : "))
    #         print(Scan(area))
    #     elif m == "3":
    #         Research()
    #     elif m == "4":
    #         area = int(input("Area : "))
    #         planet = int(input("Planet : "))
    #         print(SubmitPaper(area, planet))
    #     elif m == "5":
    #         index = int(input("AreaOfX :"))
    #         LeftNear = int(input("LeftNearPlanet :"))
    #         RightNear = int(input("RightNearPlanet :"))
    #         print(PointOutX(index, LeftNear, RightNear))
    #     elif m == "6":
    #         print("Usage Example :")
    #     elif m == "7":
    #         print(MapSet.map)
    #     print("\n")
