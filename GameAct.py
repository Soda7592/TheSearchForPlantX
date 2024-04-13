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
        return f"There are count of {StarsMap[planet]}s in area {start} to {end}."
    elif count == 1:
        return f"There are count of {StarsMap[planet]} in area {start} to {end}."
    else:
        return f"There aren't any {StarsMap[planet]}s in area {start} to {end}."


def Scan(area):
    return f"There is a {StarsMap[MapSet.map[area]]} in area {area}."


def research():
    pass


def PointOutX(index, LeftNear, RightNear):
    index_ = MapSet.map.index(5)
    LeftNear_ = (index_ - 1) % 12
    RightNear_ = (index_ + 1) % 12
    if index == index_ and LeftNear == LeftNear_ and RightNear == RightNear_:
        return True
    else:
        return False
