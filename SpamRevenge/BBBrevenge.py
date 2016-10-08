import smtplib
import time
import gmail

def main():

	while True:
		g1 = gmail.login(""); // User login ("username","password")
		BBBunread = g.inbox().mail(unread=True, sender="sender");	 //Change "sender" to email you want to spam
		if BBBunread:
			for unread in BBBunread:
				sendSpam();
				unread.delete();
		time.sleep(5);
		g1.logout();

def sendSpam():
	to = ''; //This is the recipient of your spam
	gmail_user = ''; //Email you want to send from 
	gmail_pwd = ''; // Password you want to send from 
	smtpserver = smtplib.SMTP("smtp.gmail.com",587);
	smtpserver.ehlo();
	smtpserver.starttls();
	smtpserver.ehlo();
	smtpserver.login(gmail_user,gmail_pwd);
	header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n';
	print header
	msg = header + '\n this is test msg from mkyong.com \n\n'
	for i in range(500): //Change number of times the email is sent
		smtpserver.sendmail(gmail_user, to, msg)
	print 'done!'
	smtpserver.close()

if __name__ == "__main__":
	main();
