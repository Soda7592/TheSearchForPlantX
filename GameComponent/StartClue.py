import GameComponent.MapSet as MapSet
import random

#  import MapSet as MapSet

# print(MapSet.map)
# print(MapSet.map)
# 彗星 : 1 (2顆)
# 矮行星 : 2 (1顆)
# 星際雲 : 3 (2片)
# 小行星 : 4 (4顆)

r = random.randint(0, 999)
random.seed(r)


def GiveClue(val):
    #while val < 0 or val > 12 :
        #val = input("請輸入要取得的起始線索數量(上限為12個)... \n> ")
        #val = int(val)
    ExcludeMap = []
    StarsMap = ["花果山", "天庭", "火燄山", "流沙河"]
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
    for i in range(int(val)):
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
            f"在區域{m_[i]-1}中不存在任何一個{  StarsMap[int(ExcludeMap[m_[i] - 1][0])-1] }"
        )
        MapSet.AllClues.append(
            f"在區域{m_[i]-1}中不存在任何一個{  StarsMap[int(ExcludeMap[m_[i] - 1][0])-1] }"
        )
        ExcludeMap[m_[i] - 1] = ExcludeMap[m_[i] - 1].replace(
            ExcludeMap[m_[i] - 1][0], ""
        )
    return MapSet.AllClues
