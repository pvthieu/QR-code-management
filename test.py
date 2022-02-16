import os 
import time
import tkinter
import datetime
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

window = Tk()
window.title("Quet ma QR")
window.geometry("900x500")
lbl = tkinter.Label(window, text="  *** HELLO! XIN MỜI QUÉT MÃ QR TẠI ĐÂY ***", fg="red", font=("Arial", 30))
lbl.grid(column=0, row=0)
txt = Entry(window, width=77)
txt.grid(column=0, row=1)


def handleButton():
	qr = txt.get()
	# qr.waitKey(2)
	if len(qr) > 0:	
		file = open('ktra.txt', 'r')
		danh_sach_sdt = file.read()
		for qr in danh_sach_sdt:
			qr = txt.get()
			read_ = qr[-9:]
			name_nv = qr[:-50]
			if read_ in danh_sach_sdt:
				datetime_object = datetime.datetime.now()
				time = datetime_object.strftime("%d/%m/%Y, %H:%M:%S --> ")
				if not os.path.isfile('nhanvien.txt'):
					print('Creating "nhanvien.txt"...')
					with open('nhanvien.txt', mode='a') as nv_file:
					 	nv_file.write(time + name_nv + '\n')
					 	nv_file.close()
				else:
					with open('nhanvien.txt', mode='a') as nv_file:
					 	nv_file.write(time + name_nv + '\n')
					 	nv_file.close()				
				break	 			
			else:
				print('*** Khach hang ***')
				options = Options()
				options.add_argument("user-data-dir=C:\\Users\\admin\\AppData\\Local\\Google\\Chrome\\User Data")
				options.add_argument(r'profile-directory=Profile 2')
				driver = webdriver.Chrome(executable_path=r'D:\\Cong ty\\Test\\mo_link\\chromedriver.exe', options=options)
				driver.get('https://qr.pccovid.gov.vn/ksvrbm')
				driver.implicitly_wait(10)
				driver_ = driver.find_element(By.XPATH, "//div[@class='input-qrcode--wrapper ng-star-inserted']//child::input")
				driver_.send_keys(qr)			
				time.sleep(5)
				# driver.implicitly_wait(5)
				driver.close()

handleButton()
Button = Button(window, text="KIỂM TRA", command=handleButton)
Button.grid(column=0, row=5)
window.mainloop()
