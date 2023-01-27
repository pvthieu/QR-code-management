import os 
import time
import datetime

# 079086001094|BUI QUOC ANH|1986-10-11|0|163298720202401368|<1<00<<0909330233
# 212719132|PHAM VAN THIEU|1998-07-01|0|163131983101271543|<0<00<<0981671679


qr = input("***** Quet thu ma QR *****" '\n')
print('***** Quet thanh cong... Start... *****')
for qr_ in qr:
	qr_ = input("Quét mã tại đây: " '\n')
	read_ = qr_[-9:]
	name_nv = qr_[:-50]
	datetime_object = datetime.datetime.now()
	time= datetime_object.strftime(str("%d/%m/%Y, %H:%M:%S"))
	if not os.path.isfile('check_phone.txt'):
		print('Creating "check_phone.txt"...')
		with open('check_phone.txt', mode='a') as nv_file:
		 	# nv_file.write(read_ + name_nv + '\n')
		 	nv_file.write(read_ + '\n')
		 	nv_file.close()
	else:
		with open('check_phone.txt', mode='a') as nv_file:
			# nv_file.write(read_ + name_nv + '\n')
		 	nv_file.write(read_ + '\n')
		 	nv_file.close()
	print(time,'-->',name_nv)
	print('****** QUET MA THANH CONG XIN CAM ON! ******')
	print('******   XIN MOI NHAN VIEN TIEP THEO   ******' '\n')
	continue
