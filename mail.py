# Import the following module 
from email.mime.text import MIMEText 
from email.mime.image import MIMEImage 
from email.mime.application import MIMEApplication 
from email.mime.multipart import MIMEMultipart 
import smtplib 
import os 
def start():
	#app_pass=os.getenv("app_password")

	smtp = smtplib.SMTP('smtp.gmail.com', 587) 
	smtp.ehlo() 
	smtp.starttls() 

	smtp.login('bhuktajaya@gmail.com', 'jjwc ysiu jaba laol') 

	def message(subject="Emergency alert", 
				text="", img=None, 
				attachment=None): 
		
		msg = MIMEMultipart() 
		msg['Subject'] = subject 
		msg.attach(MIMEText(text)) 
		
		if img is not None: 
			if type(img) is not list:  
				img = [img] 

			# Now iterate through our list 
			for one_img in img: 
				
				# read the image binary data 
				img_data = open(one_img, 'rb').read() 
				msg.attach(MIMEImage(img_data, 
									name=os.path.basename(one_img))) 
		return msg 

	msg = message(
		"Emergency alert",
		'''Respected user,
		A nearby user is at risk. Please help him. 
		
	This message is sent from the Semi;colon team as part of the emergency response.
		''',
		img=r"emergency-alert.jpg"
		) 

	to = ["jayabhukta@gmail.com"] 
	smtp.sendmail(from_addr="bhuktajaya@gmail.com", 
				to_addrs=to, msg=msg.as_string()) 

	smtp.quit()
	exit()
	#return True
	
#if __name__=="__main__":
	#start()
