#created by Pan Hongbing

import re
#open “address_information.csv”
text = open('address_information.csv')
l = []
address = []
re_email = re.compile(r'^[0-9A-Za-z_]+@[0-9A-Za-z_]+(\.[0-9A-Za-z_]+)+$')

#get the comma-separated information
for line in text:    
    line = line.rstrip()
    line = re.split(r',',line)
    l.append(line)

#find which address is legal and discard the wrong ones
for i in l:           
    if re_email.match(i[1]):
        print(i[1], ": Correct Address!")
        address.append(i)
    else:
        del i




import smtplib
from email.mime.text import MIMEText
from email.header import Header

#loop for sending emails
for person in address:        
#open the file and replace user names    
    mail = open('body.txt')   
    content = mail.read()
    content = re.sub(r'User',person[0],content)
#close the file    
    mail.close()
        
        
           
        
    mail_host="smtp.zju.edu.cn" 
    mail_user="3180111440@zju.edu.cn"    
    mail_pass="godlike715"  
    
    sender = '3180111440@zju.edu.cn'
    receivers = [person[1]]

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("Pan hongbing", 'utf-8')  
    message['To'] =  Header(person[0], 'utf-8')        
 
    subject = person[2]
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)   
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("Mail sent successfully")
    except smtplib.SMTPException:
        print ("fail")
    
    
    

    






