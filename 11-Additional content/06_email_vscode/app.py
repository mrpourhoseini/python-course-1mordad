import smtplib

smtp_server = smtplib.SMTP('smtp.gmail.com',587)
smtp_server.ehlo()
smtp_server.starttls()


email = 'mrpour1995@gmail.com'
password = 'rkgtapareinzhxrx'
smtp_server.login(email,password)

from_address = email
to_address = 'mpourhoseini995@gmail.com'
subject = 'Send email with VScode'
message = 'Hello VScode'
msg = "Subject: " + subject + "\n" + message
smtp_server.sendmail(from_address,to_address,msg)

smtp_server.quit()