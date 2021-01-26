
import numpy as nm 
import pytesseract 
import keyboard as kb
import cv2 
from PIL import ImageGrab 


def imToString():




	pytesseract.pytesseract.tesseract_cmd ='C:/Program Files/Tesseract-OCR/tesseract.exe'
	while(True): 

	
		cap = ImageGrab.grab(bbox =(490, 136, 1400, 175)) 

		
		kb.wait('esc')
		tesstr = pytesseract.image_to_string( 
				cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
				lang ='eng') 
		kb.write(tesstr)
		print(tesstr)



# Calling the function 
imToString() 


