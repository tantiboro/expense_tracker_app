from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

path='ExpenseTracker/ExTrackBing/'
# path='C:/inetpub/wwwroot/image4.cf/b/'
fileAttach= 'expenses.csv'

# Load the variables from the .env file
load_dotenv(r'Y:\0Python-Working\ExpenseTracker\ExTrackBing\.env')
# load_dotenv(r'C:\inetpub\wwwroot\image4.cf\b\.env')

FROM1 = os.environ['FROM1']
TO1 = os.environ['TO1']
password1 = os.environ['password1']

# print(password1, TO1, FROM1)

###### EMAIL   ########
#####




SUBJECT = 'Expense Tracker Data  '+ fileAttach +' email sent Successfully!'
password = password1

email = EmailMessage()
email['Subject'] = SUBJECT
email['From'] = FROM1
email['To'] = TO1

with open(path+ fileAttach, 'rb') as content_file:
    content = content_file.read()
    email.add_attachment(content, maintype='application', subtype='pdf', filename= fileAttach)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()
s.login(FROM1, password)
s.send_message(email)
s.quit()
print('Email sent for file with attachment: '+ fileAttach)