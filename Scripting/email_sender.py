# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 12:48:50 2020

@author: saura

python: Examples - python 3.7.4 Documentation>The python standard library > Internet data handling > email = An email and MIME handling 

Can send emails to hundreds & thousands people
"""
import smtplib # allows to create smtp server which is email protocal 
from email.message import EmailMessage
from string import Template
from pathlib import Path    # or os.path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Universe'
email['to'] = 'saurabhkragarwal@gmail.com'
email['subject'] = 'You are cooooool'
email.set_content(html.substitute({'name': 'Saurabh'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo() # part of smtp protocol and the hello message is typed as ehlo
  smtp.starttls()
  smtp.login('saurabhagarwal1089@gmail.com', 'saurabh90()') #log into the server's email, and then write your password, which is 'saurabh90()' in this case 
  smtp.send_message(email)
  print('all good boss!')
