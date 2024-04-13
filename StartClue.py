import MapSet

# print(MapSet.map)
# 彗星 : 1 (2顆)
# 矮行星 : 2 (1顆)
# 星際雲 : 3 (2片)
# 小行星 : 4 (4顆)


def GiveClue(val):
    ExcludeMap = []
    for i in range(12):
        if MapSet.map[i] == 1:
            ExcludeMap.append("234")
        elif MapSet.map[i] == 2:
            ExcludeMap.append("134")
        elif MapSet.map[i] == 3:
            ExcludeMap.append("124")
        elif MapSet.map[i] == 4:
            ExcludeMap.append("123")
        else:
            ExcludeMap.append("1234")
