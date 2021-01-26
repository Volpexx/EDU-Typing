
import numpy as nm 
import pytesseract 
import keyboard as kb
import cv2 
from PIL import ImageGrab 


def imToString():
	
	pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
	while(True): 

		#defines positions to look for characters
		capture = ImageGrab.grab(bbox =(490, 136, 1400, 175)) 

		#waits for esc key to be pressed for next line
		kb.wait('esc')

		#checks for words in english and sets capture to grayscale for easier processing
		tesstr = pytesseract.image_to_string( 
				cv2.cvtColor(nm.array(capture), cv2.COLOR_BGR2GRAY), 
				lang ='eng') 
		kb.write(tesstr)
		print(tesstr)

# Calling the function 
imToString() 
