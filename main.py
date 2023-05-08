import pynput, time
fights = 3; turns = 3; m = 0; n = 0; b = 0
def SelectBounty():
    pynput.mouse.Controller().position = (1504, 855); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
def SelectParty():
    pynput.mouse.Controller().position = (1415, 912); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
def SelectFight():
    pynput.mouse.Controller().position = (467, 505); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (612, 506); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (751, 508); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (977, 505); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (1029, 505); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (1530, 845); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
def SelectBossFight():
    pynput.mouse.Controller().position = (768, 219); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
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
    pynput.mouse.Controller().position = (965, 722); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (778, 489); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (995, 291); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
def ButtonClick():
    pynput.mouse.Controller().position = (1567, 503); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
def FinishFight():
    pynput.mouse.Controller().position = (100, 100); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(7)
def SelectPower():
    pynput.mouse.Controller().position = (791, 521); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
    pynput.mouse.Controller().position = (1127, 925); time.sleep(0.5)
    pynput.mouse.Controller().click(pynput.mouse.Button.left, 1); time.sleep(0.5)
def Main():
    time.sleep(5)
    while 1:
        # every bounty #
        SelectBounty()
        time.sleep(3)
        SelectParty()
        time.sleep(7)
        m = 0
        while m < fights:
            # every normal fight #
            SelectFight()
            time.sleep(20)
            ButtonClick()
            time.sleep(10)
            n = 0
            while n < turns:
                # every turn #
                Attack()
                time.sleep(1)
                ButtonClick()
                time.sleep(11)
                n += 1
                # every turn #
            FinishFight()
            time.sleep(5)
            SelectPower()
            time.sleep(3)
            m += 1
            # every normal fight #
        SelectBossFight()
        time.sleep(20)
        ButtonClick()
        time.sleep(10)
        b = 0
        while b < turns:
            # every turn #
            Attack()
            ButtonClick()
            time.sleep(11)
            b += 1
            # every turn #
        FinishFight()
        time.sleep(15)
        CollectTreasure()
        time.sleep(3)
        Finish()
        time.sleep(3)
        # every bounty #
Main()