import MapSet
import random

# print(MapSet.map)
# 彗星 : 1 (2顆)
# 矮行星 : 2 (1顆)
# 星際雲 : 3 (2片)
# 小行星 : 4 (4顆)


def GiveClue(val):
    ExcludeMap = []
    StarsMap = ["Comet", "Dwarf", "Interstellar Cloud", "Asteroid"]
    m = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    m_ = []
    for i in range(12):
        if i in MapSet.prime:
            if MapSet.map[i] == 1:
                ExcludeMap.append("234")
            else:
                ExcludeMap.append("1234".replace(str(MapSet.map[i]), ""))
        elif MapSet.map[i] in [2, 3, 4]:
            ExcludeMap.append("234".replace(str(MapSet.map[i]), ""))
        else:
            ExcludeMap.append("234")
    for i in range(len(ExcludeMap)):
        s = ExcludeMap[i]
        ExcludeMap[i] = "".join(random.sample(s, len(s)))
    for i in range(val):
        x = random.randint(0, 11)
        while m[x] > 1:
            x = random.randint(0, 11)
        m[x] += 1
        m_.append(x + 1)
    m_.sort()
    # print(ExcludeMap)
    # print(m)
    # print(m_)
    for i in range(len(m_)):
        print(
            f"There isn't the {  StarsMap[int(ExcludeMap[m_[i] - 1][0])-1] } in the area {m_[i]}"
        )
        ExcludeMap[m_[i] - 1] = ExcludeMap[m_[i] - 1].replace(
            ExcludeMap[m_[i] - 1][0], ""
        )


GiveClue(12)
