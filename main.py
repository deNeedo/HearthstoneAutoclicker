import pynput, time; 
#, time, numpy, cv2, pyautogui; 
import mercenaries; 

# def CompareImages(image1, image2):
#   amount = 0; 
#   for m in range(1080):
#      for n in range(1920):
#         value = 0; 
#         for b in range(3):
#            value += abs(int(image1[m][n][b]) - int(image2[m][n][b])); 
#         amount += (765 - value) / 765; 
#   return "Identity coefficient: " + str(amount / (1080 * 1920));
#
# cv2.imread
# time.sleep(1); image1 = cv2.cvtColor(numpy.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR);  
# time.sleep(2); image2 = cv2.cvtColor(numpy.array(pyautogui.screenshot()), cv2.COLOR_RGB2BGR); 
# # test = abs(image1 - image2)
# # print(sum(sum(sum(test))))
# print("Screenshots taken!"); print(CompareImages(image1, image2)); 

def PlayButton():
    pynput.mouse.Controller().position = (1470, 900); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)

def SelectParty(counter):
    PlayButton()
    if (counter == 0):
        time.sleep(0.1); pynput.mouse.Controller().position = (845, 631); time.sleep(0.1)
        pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)

def SelectFight():
    m = 300
    while m <= 1200:
        pynput.mouse.Controller().position = (m, 484); time.sleep(0.1)
        pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)
        m += 70

def CollectTreasure():
    pynput.mouse.Controller().position = (723, 741); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)
    pynput.mouse.Controller().position = (1035, 282); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)
    pynput.mouse.Controller().position = (1282, 831); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(2)
    pynput.mouse.Controller().position = (996, 630); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)

def Finish():
    pynput.mouse.Controller().position = (938, 880); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)

def Attack(targeting):
    pynput.mouse.Controller().position = (778, 489); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)
    if (targeting):
        pynput.mouse.Controller().position = (995, 291); time.sleep(0.1)
        pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)

def EndTurn():
    pynput.mouse.Controller().position = (1567, 503); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(11)

def FinishFight():
    pynput.mouse.Controller().position = (100, 100); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(1)
    pynput.mouse.Controller().position = (100, 100); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(7)

def SelectPower():
    pynput.mouse.Controller().position = (791, 521); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.1)
    pynput.mouse.Controller().position = (1127, 925); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(3)

def Await(minutes):
    t = 60*minutes; time.sleep(t)

def Retire():
    pynput.mouse.Controller().position = (796, 1000); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(1)
    pynput.mouse.Controller().position = (1094, 796); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(1)
    pynput.mouse.Controller().position = (844, 617); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(4)
    pynput.mouse.Controller().position = (844, 617); time.sleep(0.1)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(2)

def Initialize(mercenary):
    if mercenary == "Xyrella":
        return mercenaries.Xyrella()
    elif mercenary == "Millhouse":
        return mercenaries.Millhouse()
    elif mercenary == "Vanessa":
        return mercenaries.Vanessa()
    else:
        return None
    
def Main():
    fights = 3; counter = 0
    mercenary = input("Provide a name of a mercenary you wish to start the run with: "); 
    mercenary = Initialize(mercenary); 
    if (mercenary == None):
        print("No config for provided mercenary!"); 
    else:
        print("Starting run with: " + mercenary.name); 
        time.sleep(3)
        while 1:
            # every bounty #
            PlayButton()
            time.sleep(3)
            SelectParty(counter)
            time.sleep(7)
            m = 0
            while m < fights:
                # every normal fight #
                if (m == 0):
                    PlayButton()
                else:    
                    SelectFight()
                    PlayButton()
                time.sleep(17)
                Await(28) # for farming exp instead of coins
                EndTurn()
                n = 0
                while n < mercenary.turns:
                    # every turn #
                    Attack(mercenary.targeting)
                    time.sleep(1)
                    EndTurn()
                    n += 1
                    # every turn #
                FinishFight()
                SelectPower()
                m += 1
                # every normal fight #
            Retire()
            # PlayButton()
            # time.sleep(17)
            # Await(28) # for farming exp instead of coins
            # EndTurn()
            # b = 0
            # while b < mercenary.boss_turns:
            #     # every turn #
            #     Attack(mercenary.targeting)
            #     time.sleep(1)
            #     EndTurn()
            #     b += 1
            #     # every turn #
            # FinishFight()
            # time.sleep(7)
            # CollectTreasure()
            # time.sleep(3)
            # Finish()
            # time.sleep(3)
            # counter += 1
            # every bounty #
Main()
