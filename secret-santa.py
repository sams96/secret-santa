import csv
import random
import smtplib
import time
from email.mime.text import MIMEText
from email.header import Header
import configparser

cfg = configparser.ConfigParser()
cfg.read('secret.ini')

addr = cfg['secret']['address']
pasw = cfg['secret']['passwd']
head = cfg['secret']['header']
smtp = cfg['secret']['smtp']

def choose(names):
	chosen = []
	for p in names:
		others = [x for x in names if x[2] != p[2] and x[0] != p[3] and x not in chosen]

		if not others:
			print('others is empty')
			return []

		choice = random.choice(others)
		chosen.append(choice)
		p.append(choice[0])

	return names

def sendone(i, names, wait):
	try:
		s = smtplib.SMTP(smtp, port = 587, timeout = 60)
		s.login(addr, pasw)

		msg = MIMEText('Your secret santa is ' + names[0][3], 'plain', 'utf-8')
		msg['Subject'] = Header(head, 'utf-8')
		msg['From'] = addr
		msg['To'] = names[0][1]
		s.send_message(msg)

		#print(msg.as_string())
		names.remove(names[0])
		print('sent')
		s.quit()

	except smtplib.SMTPRecipientsRefused:
		sendone(i, names, wait * 2)

	return names


def send(names):
	for i in range(len(names)):
		names = sendone(i, names, 100)

while True:
	with open('names.csv') as csvfile:
		reader = csv.reader(csvfile)
		names = [r for r in reader]
	names = choose(names)
	if names:
		break

#names = send(names)
