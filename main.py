import pynput, time, mercenaries

def SelectBounty():
    pynput.mouse.Controller().position = (1504, 855); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def SelectParty(counter):
    pynput.mouse.Controller().position = (1415, 912); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    if (counter == 0):
        pynput.mouse.Controller().position = (845, 631); time.sleep(0.5)
        pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def SelectFight():
    m = 300
    while m <= 1200:
        pynput.mouse.Controller().position = (m, 484); time.sleep(0.1)
        pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)
        m += 70
    pynput.mouse.Controller().position = (1530, 845); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def SelectBossFight():
    pynput.mouse.Controller().position = (1530, 845); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def CollectTreasure():
    pynput.mouse.Controller().position = (723, 741); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (1035, 282); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (1282, 831); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(2)
    pynput.mouse.Controller().position = (996, 630); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def Finish():
    pynput.mouse.Controller().position = (938, 880); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def Attack():
    pynput.mouse.Controller().position = (778, 489); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    # not for every mercenary
    # pynput.mouse.Controller().position = (995, 291); time.sleep(0.5)
    # pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def EndTurn():
    pynput.mouse.Controller().position = (1567, 503); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def FinishFight():
    pynput.mouse.Controller().position = (100, 100); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(1)
    pynput.mouse.Controller().position = (100, 100); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(7)

def SelectPower():
    pynput.mouse.Controller().position = (791, 521); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (1127, 925); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)

def Await():
    t = 60*28; time.sleep(t)

def Initialize(mercenary):
    if mercenary == "Xyrella":
        return mercenaries.Xyrella()
    elif mercenary == "Millhouse":
        return mercenaries.Millhouse()
    else:
        return None
    
def Main():
    fights = 3; counter = 0
    mercenary = input("Provide a name of a mercenary you wish to start the run with: ")
    mercenary = Initialize(mercenary)
    if (mercenary == None):
        print("No config for provided mercenary!")
    else:
        print("Starting run with: " + mercenary.name)
        time.sleep(5)
        while 1:
            # every bounty #
            # print("Bounties completed in this run: " + str(counter))
            SelectBounty()
            time.sleep(3)
            SelectParty(counter)
            time.sleep(7)
            m = 0
            while m < fights:
                # every normal fight #
                if (m == 0):
                    pynput.mouse.Controller().position = (1530, 845); time.sleep(0.5)
                    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
                else:    
                    SelectFight()
                time.sleep(19)
                Await() # for farming exp instead of coins
                EndTurn()
                time.sleep(10)
                n = 0
                while n < mercenary.turns:
                    # every turn #
                    Attack()
                    time.sleep(1)
                    EndTurn()
                    time.sleep(12)
                    n += 1
                    # every turn #
                FinishFight()
                time.sleep(3)
                SelectPower()
                time.sleep(4)
                m += 1
                # every normal fight #
            SelectBossFight()
            time.sleep(19)
            Await() # for farming exp instead of coins
            EndTurn()
            time.sleep(10)
            b = 0
            while b < mercenary.boss_turns:
                # every turn #
                Attack()
                time.sleep(1)
                EndTurn()
                time.sleep(12)
                b += 1
                # every turn #
            FinishFight()
            time.sleep(10)
            CollectTreasure()
            time.sleep(3)
            Finish()
            time.sleep(3)
            counter += 1
            # every bounty #
Main()