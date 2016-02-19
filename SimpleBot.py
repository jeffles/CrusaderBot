import datetime
import pyautogui
import random
import time

# Adapt code for steam.. but also adapt it for screen size!
# Prep for github
EVENT_ACTIVE = True

#Character level buttons
HERMIT = [1110, 600]
WEREWOLF = [755, 595]

#Restart locations
WAKE_FREEPLAY = [720, 280]
DESCENT_FREEPLAY = [720, 410]
GHOSTBEARD_FREEPLAY = [720, 540]
GRIMM_FREEPLAY = [720, 670]

CHEST = [680, 375]
CHEST_CONFIRM = [680, 500]
CHARACTER_LEFT = [130, 670]
CHARACTER_TAB = [950, 535]
DIALOG_CONFIRM = [530, 420]
LEVEL_ALL = [1230, 700]

if EVENT_ACTIVE:
    GHOSTBEARD_FREEPLAY = [720, 690]


def click(x=None, y=None, keydown=None):
    if x is None:
        pyautogui.click()
        return

    if keydown:
        pyautogui.keyDown(keydown)

    pyautogui.click(x, y)

    if keydown:
        pyautogui.keyUp(keydown)


def move_to(x, y):
    pyautogui.moveTo(x, y)


def set_focus_on_characters():
    click(CHARACTER_TAB)
    click(CHARACTER_LEFT, keydown='shift')


def attack():

    # Trying to move forward a little faster and save seconds on chests
    # But may not be worth it, on the 5 row missions it ends up clicking
    # on a character, forcing us to reset to the left for leveling
    click(CHEST)
    click(CHEST_CONFIRM)

    for i in range(35):
        move_to(random.randint(770, 1180), random.randint(280, 390))
    for i in range(3):
        click(random.randint(770, 1180), random.randint(280, 390))


def level(character):
    click(character, keydown='ctrl')


def get_minutes(start_time):
    current_time = datetime.datetime.now()
    delta = current_time - start_time
    return delta.seconds//60


def level_all():
    click(LEVEL_ALL)
    time.sleep(2)
    click(DIALOG_CONFIRM)


def powers():
    click(530, 530)    # Click-o-rama
    click(570, 530)    # Magnify
    click(800, 530)    # Storm Rider
    click(610, 530)    # Fire Storm
    click(660, 530)    # Simba's Pride
    click(710, 530)    # Gold-o-rama
    click(750, 530)    # King's command
    click(840, 530)    # Alchemy


def main():
    # Before running this program, set Crusaders to full screen, and close the popup ads.
    set_focus_on_characters()

    start_time = datetime.datetime.now()

    last_minute = -1
    while True:
        current_minute = get_minutes(start_time)

        if current_minute == last_minute:
            attack()
            continue

        if current_minute % 16 == 0:
            powers()

        set_focus_on_characters()
        if current_minute % 2 == 0:
            level(HERMIT)
            level(WEREWOLF)
        else:
            level(WEREWOLF)
            level(HERMIT)

        last_minute = current_minute


if __name__ == '__main__':
    main()
