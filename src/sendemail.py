import smtplib
from speech import say

def send(input):
	if "send an email to " not in input:
	        say("Sorry, you must specify someone in your contacts, for example by saying send an email to mom saying hello.")
        else:
		#detects if the user said "send an email to jared saying hello" or "send an email to jared that says hello"
	        hasmsg = True #bool that determines if user remembered to include email message.
		if "saying" in input:
	        	saystring = "saying"
	        elif "that says" in input:
	        	saystring = "that says"
	        else:
	                say("Sorry, you must specify a message by for example saying send an email to mom saying hello.")
			hasmsg = False
	         	
		if hasmsg:
                	msg = input[input.index(saystring)+len(saystring):]
                	temp = input[len("send an email to "):]
                	contact = temp[0:temp.index(saystring)-1].lower()
                	print contact
                	try:
	        	        contactfile = open("/home/pi/piband/src/" + contact.lower(), "r")
	        	        contactemail = contactfile.read()
	        	        say("Ok. This is the message I will send to " + contact + ":" + msg)
	        	        print msg
	        	        fromaddr = open("/home/pi/piband/src/fromaddr", "r").read()
	        	        emailpass = open("/home/pi/piband/src/emailpass", "r").read()
	        	        print fromaddr
	        	        print emailpass
	        	        msg = "From: " + fromaddr + "\n" + msg
	        	
			        server = smtplib.SMTP("smtp.gmail.com", 587)
	        	        server.ehlo()
	        	        server.starttls()
	        	        server.login(fromaddr, emailpass)
	        	
			        #Comment out or change the following line to remove or change the email signature.
	        	        msg = msg + "\nsent from my PiBand"
                	        server.sendmail(fromaddr, contactemail, msg)
                	        say("Email sent!")
                	except Exception as e:
                	        print e
                	        say("Sorry, " + contact + " is not in your contacts. Instructions on how to put someone in your contacts are in the readme file.")

