import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Define these once; use them twice!
strFrom = 'allphone@bcservice.by'
strTo = 'www.heretic@inbox.ru'
#strTo = 'delivery@nsys.by'

server = 'mail.bcservice.by'  # Сервер
port = 2525  # Порт
user_name = 'allphone@bcservice.by'  # Отправитель
user_passwd = '242425767'  # Пароль отправителя

# Create the root message and fill in the from, to, and subject headers
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'
msgRoot['From'] = strFrom
msgRoot['To'] = strTo
msgRoot.preamble = 'This is a multi-part message in MIME format.'

# Encapsulate the plain and HTML versions of the message body in an
# 'alternative' part, so message agents can decide which they want to display.
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)

msgText = MIMEText('This is the alternative plain text message.')
msgAlternative.attach(msgText)

# We reference the image in the IMG SRC attribute by the ID we give it below
# msgText = MIMEText('<br><img src="cid:header"><br>'
#                    '<b>Some <i>HTML</i> text</b>'
#                    ' and an image.'
#                    '<br><img src="cid:image2"><br>'
#                    'Nifty! and an image.'
#                    '<br><img src="cid:image3"><br>Nifty!', 'html')
# msgText = MIMEText('<p><a href="http://modelkits.by"><img src="cid:header" alt="Пример"></a></p>'
#                    '<br><h1>В продаже с 12 июня, Не пропустите!!!</h1></br>'
#                    '<p><a href="http://modelkits.by/новинки-ezp-17"><img src="cid:image1"alt="Пример"></a></p>'
#                    ' А также другие наши модели:'
#                    '<br><img src="cid:image2"><br>'
#                    '<br><img src="cid:image3"><br>', 'html')
msgText = MIMEText('<p><a href="http://modelkits.by"><img src="cid:header" alt="Пример"></a></p>'
' <TABLE BORDER>'
'        <TR>'
'               <TD><br><h1>В продаже с 12 июня, Не пропустите!!!</TD>'
'        </TR>'
'        <TR>'
'                <TD><p><a href="http://modelkits.by/новинки-ezp-17"><img src="cid:image1"alt="Пример"></a></p></TD>'
'        </TR>'
'        <TR>'
'                <TD><br><h1>Другие наши модели</TD>'
'        </TR>'
'        <TR>'
'                <TD><br><img src="cid:image2" width="300"height="190"><br></TD>'
                '<TD><br><img src="cid:image3" width="300"height="190"><br></TD>'
'        </TR>'
'</TABLE>', 'html')
msgAlternative.attach(msgText)

# This example assumes the image is in the current directory
#fp1 = open('test.jpg', 'rb')
header = open('header.jpg', 'rb')
msgHeader = MIMEImage(header.read())
header.close()
fp1 = open('test1.jpg', 'rb')
msgImage1 = MIMEImage(fp1.read())
fp1.close()
fp2 = open('test2.jpg', 'rb')
msgImage2 = MIMEImage(fp2.read())
fp2.close()
fp3 = open('test3.jpg', 'rb')
msgImage3 = MIMEImage(fp3.read())
fp3.close()
# Define the image's ID as referenced above
msgHeader.add_header('Content-ID', '<header>')
msgRoot.attach(msgHeader)
msgImage1.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage1)
msgImage2.add_header('Content-ID', '<image2>')
msgRoot.attach(msgImage2)
msgImage3.add_header('Content-ID', '<image3>')
msgRoot.attach(msgImage3)

# Send the email (this example assumes SMTP authentication is required)
import smtplib
smtp = smtplib.SMTP()
smtp.connect(server)
smtp.login(user_name, user_passwd)
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
smtp.quit()