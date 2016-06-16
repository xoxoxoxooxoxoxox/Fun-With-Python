'''
Author: Chin-Chwen Tien
Version: 1.0
Create Date: Tue June 14, 2016
Objective: Don't just sit in front of the PC all day!!
'''

import time
import webbrowser

totalBreak = 3
breakCount = 0

print("This program started on " + time.ctime())
while breakCount < totalBreak:
	print("Current Time: " + time.ctime())
	time.sleep(30 * 60)
	print("Take a break!")
	webbrowser.open("https://www.youtube.com/watch?v=DDO_aCkivxU")
	breakCount += 1
