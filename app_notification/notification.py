
import smtplib
from email.message import EmailMessage
def enviar_mail(data):

    destinatario = ''#db.session.query(Usuario).get(data['id_usuario'])
    print(destinatario.email, data)
    remitente = "flask.nube@outlook.com"
    destinatario = destinatario.email
    mensaje = f"¡El Archivo {data['nombre_archivo']} fue tranformado!"
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = f"Archvio {data['nombre_archivo']} tranformado"
    email.set_content(mensaje)
    smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    smtp.starttls()
    smtp.login(remitente, "flask.123")
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()