import GameComponent.MapSet as Map
import GameComponent.StartClue as Clue
import GameComponent.PlantXConf as XConf
import GameComponent.GameAct as Act
import random


if __name__ == "__main__":
    print("Welcome to The Search For Plant X".center(20))
    print("There are 12 areas, every area has a type of planet.")
    print("There are 6 types of planets, and 1 of them is X planet.")
    print("====================")
    print("Two of comets and they always appear in areas which number are prime.")
    print(
        "One of dwarf and it always appears in a random area.(X planet always not near to it.)"
    )
    print("Two of interstellar cloud and they always appear in random areas.")
    print("Four of asteroids and they always appear in random areas.")
    print(
        "Three of empty planet.(When X planet was scanned, it will be shown as empty planet.)"
    )
    print("====================")
    print(
        "You goal is to find and point out the X planet and the planets which are near to it."
    )
    print("====================\n")
    input("Press any key to continue.....")
    StartClue = Clue.GiveClue()
    input("\nPress any key to enter game.....")
    print("\n")
    Research = Act.Research()
    while True:
        print("<==========>")
        print(
            " - 0 => Show the number of planets.\n",
            "- 1 => Survey (start, end, planet). (*3, *4)\n",
            "- 2 => Scan (area). (*4)\n",
            "- 3 => Research (Planet). (*2)\n",
            "- 4 => SubmitPaper (area, planet). (V:*-2, X:*+2)\n",
            "- 5 => PointOutX (AreaOfX, LeftNearPlanet, RightNearPlanet). (*5)\n",
            "- 6 => Review the start clues.\n",
            "- 7 => Help\n",
            "- 8 => ExitAndGetResult.",
        )
        print("<==========>")
        m = input("Input a Action > ")
        if m == "0":
            print("\n>==========<")
            print("Number of Planet :")
            print("**Empty** : 0")
            print("**Comet** : 1")
            print("**Dwarf** : 2")
            print("**Interstellar Cloud** : 3")
            print("**Asteroid** : 4")
            print(">==========<\n")
        elif m == "1":
            start = int(input("Start :"))
            end = int(input("End :"))
            planet = int(input("Planet : "))
            print("\n\n====>", Act.Survey(start, end, planet), "\n\n")
        elif m == "2":
            area = int(input("Area : "))
            # print(Map.map)
            print("\n\n====>", Act.Scan(area - 1), "\n\n")
        elif m == "3":
            planet = input("Input a planet to get a research result ** randomly ** : ")
            s = random.choice(Research[int(planet)])
            print("\n\n====> **", s, "**\n\n")
        elif m == "4":
            area = int(input("Area : "))
            planet = int(input("Planet : "))
            print("\n\n====>", Act.SubmitPaper(area, planet), "\n\n")
        elif m == "5":
            # print(Map.map)
            index = int(input("AreaOfX :"))
            LeftNear = int(input("LeftNearPlanet :"))
            RightNear = int(input("RightNearPlanet :"))
            if Act.PointOutX(index, LeftNear, RightNear):
                print("\n\n====> You have pointed out the X planet! Congratulations!\n")
                print("Total months you have used:")
                print("====> ", Map.months, "\n\n")
            else:
                print("\n\n====> You have pointed out the wrong planet!")
                print("Until now, you have used months:")
                print("====>", Map.months, "\n\n")
        elif m == "6":
            for i in range(len(StartClue)):
                print(f"Clue {i}", StartClue[i], "\n")
        elif m == "7":
            print("\t**Usage** : [Number of Method] [argument 1] [argument 2] ....")
            print("\t**Usage Example** : 1")
            print("\tStart : 1")
            print("\tEnd : 6")
            print("\tPlanet : 2")
            print(
                "\t**Usage Explain** : Survey from area 1 to 6, and return how many Dwarf there have or not."
            )
        elif m == "8":
            break
    print(Map.map)
