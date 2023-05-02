import pyautogui
import time

msg = input("Enter the message: ")
n = input("How many times ?: ")

count = 6
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Fire in the hole!!!")
for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')
	#time.sleep(0.5)

print("Mission Succes!")