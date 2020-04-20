import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('john.sodermark@gmail.com','Programvara1')
conn.sendmail('john.sodermark@gmail.com','Kait.Sodermark@gmail.com',"Subject:Hej!..\n\nHej,\nMy computer sent this automatically, even though you don't think it's cool..\n\n-JP")
conn.quit()
