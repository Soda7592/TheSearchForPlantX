import GameComponent.MapSet as Map
import GameComponent.StartClue as Clue
import GameComponent.PlantXConf as XConf
import GameComponent.GameAct as Act
import random

#global chars, Force, GoldAct, TokenAct
#chars = 99
#Force = False
#GoldAct = 99
#TokenAct = 99
#Force = False
#GoldAct = 0
#TokenAct = 0

if __name__ == "__main__":
    round = 0
    Map.Force = False
    Map.GoldAct = 0
    Map.TokenAct = 0
    Map.chars = 99
    print("歡迎來到西遊記-尋找真經。")
    print("在遊戲中一共有 12 個區域，每個區域內都有一種物件。")
    print("遊戲中一共有 6 種不同的物件，其中一個是各位要尋找的真經")
    print("====================")
    print("地圖中有兩座花果山，並且花果山只會出現在質數-1的區域")
    print(
        "地圖中有一個天庭，同時真經不會相鄰於天庭"
    )
    print("地圖中有三座火焰山，")
    print("地圖中有四條流沙河")
    print(
        "地圖中有兩座荒野，但是若真經被探測到也會被視作荒野"
    )
    print("====================")
    print(
        "你的遊戲目標即 : 找到真經"
    )
    print("====================\n")
    input("按下任意鍵開始遊戲.....")
    StartClue = Clue.GiveClue(input("\n請輸入起始線索數量(0,4,8,12) > "))
    print("\n\n")
    Research = Act.Research()
    print(Map.map)
    while True:
        if round == 0 :
            print("☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼")
            print("\n目前是唐三藏的操作回合，請選擇以下行動")
            print("<==========>")
            print(
            " - 0 => 使用令牌要求某角色強制執行指令\n",
            "- 1 => 使用金箍咒讓孫悟空下次行動必定照著自己的要求進行\n",
            "- 2 => 取得一個線索，並且觀看沙悟淨當前的紀錄\n",
            "- 3 => 嘗試定位真經的位置\n",
            "- 4 => 感應到真經與其他地圖的位置關係"
            )
            act = int(input("請輸入行動代號 > "))
            if act == 0:
                Map.chars = int(input("請輸入指定的玩家角色(孫:1, 豬:2, 沙:3) > "))
                Map.TokenAct = int(input("請輸入該角色需要執行的動作 > "))
                print(Map.chars)
            elif act == 1 :
                Map.Force = True
                Map.GoldAct = int(input("請輸入要孫悟空執行的動作 > "))
            elif act == 2 :
                print(Act.GetClue())
                for i in range(len(Map.MapBy_7)) :
                    if Map.MapBy_7[i] == 6 :
                        print('\033[31m',f">> : 未知",'\033[0m')
                    else :
                        print('\033[31m',f">> : {Map.StarsMap[Map.MapBy_7[i]]}",'\033[0m')
            elif act == 3 :
                Act.PlanetNum()
                area = int(input("請給出真經所在區域 > "))
                Left = int(input("請給出真經所在區域之左邊的地圖為 > "))
                Right = int(input("請給出真經所在區域之右邊的地圖為 > "))
                result = Act.PointOutX(area, Left, Right)
                if result == True:
                    print("恭喜找出真經")
                    print(f"尋找真經使用的總年份為{Map.months/12}")
                    print(f"區域地圖為{Map.map}")
                    break
                else :
                    print("錯誤的真經位置")
            elif act == 4 :
                print("\n \033[31m")
                XConf.X()
                print('\033[0m \n')
                Map.months += 2                 
        elif round == 1 :
            print("☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼☼\n")
            print("𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 ")
            Act.randMonster()
            print("\n目前是孫悟空的操作回合，請選擇以下行動")
            if Map.Force == True :
                Map.Force = False
                print("孫悟空受到金箍咒的影響，執行了以下行為")
                if Map.GoldAct == 0 :
                    Map.GoldAct = 99
                    print("> 勘查 \n")
                    Act.PlanetNum()
                    print("請輸入起點, 終點, 以及欲探測的地點")
                    start = int(input("起點 > "))
                    end = int(input("終點 > "))
                    planet = int(input("地點 > "))
                    Act.Survey_5(start, end, planet)
                elif Map.GoldAct == 1 :
                    Map.GoldAct = 99
                    print("> 掃描 \n")
                    Act.PlanetNum()
                    print("請輸入要探測的區域")
                    area = int(input("區域 > "))
                    Act.Scan_5(area)
            else :
                print("<==========>")
                print(
                " - 0 => 進行勘查\n",
                "- 1 => 進行掃瞄\n",
                "- 2 => 打退來鬧事的妖怪\n",
                )
                act = int(input("請輸入行動代號 > "))
                if act == 0 :
                    Act.PlanetNum()
                    print("請輸入起點, 終點, 以及欲探測的地點")
                    start = int(input("起點 > "))
                    end = int(input("終點 > "))
                    planet = int(input("地點 > "))
                    Act.Survey_5(start, end, planet)
                elif act == 1 :
                    Act.PlanetNum()
                    print("請輸入要探測的區域")
                    area = int(input("區域 > "))
                    Act.Scan_5(area)
                elif act == 2 :
                    Act.AttackMonster()
            Map.Force = False
            Map.GoldAct = 99
        elif round == 2:
            print("𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 𖣘 \n")
            print("⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎")
            print("\n目前是豬八戒的操作回合，請選擇以下行動")
            #print(Map.chars)
            if Map.chars == 2 :
                print("由於師父要求你進行指定動作，所以你只能完成以下動作")
                Map.chars = 99
                if Map.TokenAct == 0 :
                    Map.TokenAct = 99
                    print("> 勘查 \n")
                    Act.PlanetNum()
                    print("請輸入起點, 終點, 以及欲探測的地點")
                    start = int(input("起點 > "))
                    end = int(input("終點 > "))
                    planet = int(input("地點 > "))
                    Act.Survey_8(start, end, planet)
                elif Map.TokenAct == 1 :
                    Map.TokenAct = 99
                    print("> 掃描 \n")
                    Act.PlanetNum()
                    print("請輸入要探測的區域")
                    area = int(input("區域 > "))
                    Act.Scan_8(area)
            else :
                print("<==========>")
                print(
                " - 0 => 進行勘查\n",
                "- 1 => 進行掃描\n",
                "- 2 => 指出地理資訊為師父補血\n"
                )
                act = int(input("請輸入行動代號 > "))
                if act == 0 :
                    Act.PlanetNum()
                    print("請輸入起點, 終點, 以及欲探測的地點")
                    start = int(input("起點 > "))
                    end = int(input("終點 > "))
                    planet = int(input("地點 > "))
                    Act.Survey_8(start, end, planet)
                elif act == 1 :
                    Act.PlanetNum()    
                    print("請輸入要探測的區域")
                    area = int(input("區域 > "))
                    Act.Scan_8(area)
                elif act == 2 :
                    Act.PlanetNum()
                    area = int(input("請選擇欲指定的區域號碼 > "))
                    planet = int(input("請給出該區域的正確地點編號 > "))
                    print(Act.SubmitPaper(area, planet))
        elif round == 3:
            print("⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎⛏︎\n")
            print("♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ")
            print("\n目前是沙悟淨的操作回合，請選擇以下行動")
            if Map.chars == 3 :
                Map.chars = 99
                print("由於師父要求你進行指定動作，所以你只能完成以下動作")
                if Map.TokenAct == 0 :
                    Map.TokenAct = 99
                    print("> 取得線索\n")
                    GetClue()
                elif Map.TokenAct == 1 :
                    Map.TokenAct = 99
                    print("> 繪製地圖 \n")
                    Act.PlanetNum()
                    area = int(input("請輸入要標記的區域 > "))
                    planet = int(input("請輸入該區域的地點編號 > "))
                    Act.DrawMap(area, planet)    
            else :
                print("<==========>")
                print(
                " - 0 => 取得一個線索\n",
                "- 1 => 將已知的一個線索繪製到地圖上\n"
                )
                act = int(input("請輸入行動代號 >"))
                if act == 0 :
                    Act.GetClue()
                elif act == 1 :
                    Act.PlanetNum()
                    area = int(input("請輸入要標記的區域 > "))
                    planet = int(input("請輸入該區域的地點編號 > "))
                    Act.DrawMap(area, planet)
            print("♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎ ♨︎\n")
        round = (round+1)%4
        if Map.IsMonster :
            Map.Health_3 -= 1
        if Map.months//12 > 10:
            print('未於時間內找到真經，遊戲結束')
            break
        else :
            print(f"當前已使用時間為 {Map.months}月/{Map.months//12}年")
        if Map.Health_3 <= 0 :
            print("唐三藏已死，遊戲結束..")
            break
        else :
            print(f'唐三藏當前剩餘血量為 : {Map.Health_3}')
       # Map.chars = 99
        #Map.TokenAct = 99
        '''
        print("<==========>")
        print(
            " - 0 => 顯示各地圖物件代號\n",
            "- 1 => 勘查 (起點, 終點, 地圖物件編號). (*3, *4)\n",
            "- 2 => 掃描 (區域編號). (*4)\n",
            "- 3 => 研究 (地圖物件編號). (*2)\n",
            "- 4 => 地圖物件確認 (區域, 地圖物件). (V:*-2, X:*+2)\n",
            "- 5 => 找到真經(?) (真經所在區域編號, 真經左側地圖物件, 真經右側地圖物件). (*5)\n",
            "- 6 => 重新查看線索\n",
            "- 7 => 遊戲幫助\n",
            "- 8 => 離開遊戲並揭曉真經位置",
        )
        print("<==========>")
        m = input("請輸入執行動作 > ")
        if m == "0":
            print("\n>==========<")
            print("地圖物件編號 : ")
            print("**荒野** : 0")
            print("**花果山** : 1")
            print("**天庭** : 2")
            print("**星際雲** : 3")
            print("**流沙河** : 4")
            print(">==========<\n")
        elif m == "1":
            start = int(input("起點 :"))
            end = int(input("終點 :"))
            planet = int(input("地圖物件編號 : "))
            print("\n\n====>", Act.Survey(start, end, planet), "\n\n")
        elif m == "2":
            area = int(input("區域編號 : "))
            # print(Map.map)
            print("\n\n====>", Act.Scan(area - 1), "\n\n")
        elif m == "3":
            planet = input("輸入一個地圖物件編號來取得一個隨機線索 : ")
            s = random.choice(Research[int(planet)])
            print("\n\n====> **", s, "**\n\n")
        elif m == "4":
            area = int(input("區域編號 : "))
            planet = int(input("地圖物件編號 : "))
            print("\n\n====>", Act.SubmitPaper(area, planet), "\n\n")
        elif m == "5":
            # print(Map.map)
            index = int(input("真經所在區域 :"))
            LeftNear = int(input("真經左側物件編號 :"))
            RightNear = int(input("真經右側物件編號 :"))
            if Act.PointOutX(index, LeftNear, RightNear):
                print("\n\n====> 恭喜，你成功找到了真經 !\n")
                print("你總共使用了 :")
                print("====> ", Map.months/12, "(年)\n\n")
            else:
                print("\n\n====> 失敗，錯誤的真經位子 ! 或是旁邊物件指出錯誤")
                print("直至目前為止，你已經使用了 :")
                print("====>", Map.months/12, "(年)\n\n")
        elif m == "6":
            for i in range(len(StartClue)):
                print(f"線索 {i}", StartClue[i], "\n")
        elif m == "7":
            print("\t**用法** : [動作編號] [參數1] [參數2] ....")
            print("\t**用法範例 ** : 1")
            print("\t起點 : 1")
            print("\t終點 : 6")
            print("\t地圖物件編號 : 2")
            print(
                "\t**用法解釋** : 調查區域1到區域6，並且給出在這些區域中有幾座天庭"
            )
        elif m == "8":
            break
        '''
#    print(Map.map)
