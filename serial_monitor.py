import serial
from time import sleep
import sys
import pyautogui


COM = '/dev/tty.usbmodem14601'
BAUD = 9600

ser = serial.Serial(COM, BAUD, timeout = .1)

print('Waiting for device');
sleep(3)
print(ser.name)

#check args
if("-m" in sys.argv or "--monitor" in sys.argv):
	monitor = True
else:
	monitor= False

while True:
	val = str(ser.readline().decode().strip('\r\n'))#Capture serial output as a decoded string
	valA = val.split("/")
	#print()
	if(len(val) > 0):
		print(val, end="\n", flush=True)
		pyautogui.write(val)
