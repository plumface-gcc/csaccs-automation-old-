import cv2
import pytesseract
from selenium import webdriver
import time
import re
import random

username = 'johntrollsten26@gmail.com'
password = 'marineklimenko2'

browser = webdriver.Chrome()
browser.get(('https://csaccs.com/login'))

signInUser = browser.find_element_by_id('email')
signInPass = browser.find_element_by_id('password')

time.sleep(2.45)
signInUser.send_keys(username)
time.sleep(2.1236)
signInPass.send_keys(password)

time.sleep(1.231)

signIn = browser.find_element_by_name('submit')
signIn.click()

time.sleep(1.52)


while True:

    rand = 2

    try:
        captcha = browser.find_element_by_id('captchaform')

        img = cv2.imread('cap.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        invert = 255 - opening

        data = pytesseract.image_to_string(invert, lang='eng',
                                           config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

        print(data)

    except:
        pass

    try:
        time.sleep(5)
        crime3New = browser.find_element_by_link_text('Break open a slot machine')
        crime3New.click()

    except:
        pass

    try:
        if rand == 2:
            bankTab = browser.find_element_by_link_text('Bank')
            bankTab.click()
            time.sleep(1)
            enterAmount = browser.find_element_by_name('Amount')
            depositButton = browser.find_element_by_name('Deposit')
            currentMoney = browser.find_element_by_xpath('//*[@id="navbarToggle"]/div[2]/a[1]')

            getMoney = currentMoney.text
            finalMoney = getMoney.replace('€', '')
            time.sleep(0.5)
            enterAmount.send_keys(finalMoney)
            time.sleep(0.5)
            depositButton.click()

            time.sleep(1)
            crimeButton = browser.find_element_by_link_text('Crime')
            crimeButton.click()
            time.sleep(2)
            rand = 0

    except:
        pass





"""

while True:

    try:
        captcha = browser.find_element_by_id('captchaform')

        img = cv2.imread('cap.png')
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (3, 3), 0)
        thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        invert = 255 - opening

        data = pytesseract.image_to_string(invert, lang='eng',
                                           config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')

        print(data)

    except:

        print("caught")

    time.sleep(34)
    crime3New = browser.find_element_by_link_text('Break open a slot machine')
    crime3New.click()

"""
