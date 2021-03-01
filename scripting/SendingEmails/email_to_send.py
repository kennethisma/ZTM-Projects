import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template
import os


correo = os.environ.get('DB_USER')  # Enviroment variable
contraseña = os.environ.get('DB_PASSWORD')  # Enviroment variable

html = Template(Path("index.html").read_text())
email = EmailMessage()

email['from'] = "Python"
email['to'] = "Aquivatucorreo@inout.com"
email['subject'] = 'Esto fue enviado desde python'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(correo, contraseña)
    smtp.send_message(email)
    print('Sent it boss')
