# from turtle import position
import pyautogui as pt
# import subprocess
# from pynput.mouse import Controller, Button
import time
import pyperclip as pc

# mouse = Controller()
class WhatsApp:

    def __init__(self, speed=.5, click_speed=.3):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('dot.png', confidence=.5)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot):', e)

wa_bot = WhatsApp(speed=.5, click_speed=.4)
time.sleep(3)
wa_bot.nav_green_dot()