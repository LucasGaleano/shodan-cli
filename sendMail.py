from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email_html(emailFrom, emailTo, subject, content, mailServer):
    
    MESSAGE = MIMEMultipart('alternative')
    MESSAGE['subject'] = subject
    MESSAGE['To'] = emailTo
    MESSAGE['From'] = emailFrom
    PLAIN_BODY = MIMEText(content, "plain")
    HTML_BODY = MIMEText(content, 'html')
    MESSAGE.attach(PLAIN_BODY)
    MESSAGE.attach(HTML_BODY)

    server = SMTP(host=mailServer, port=25)    
    
    server.sendmail(emailFrom, emailTo, MESSAGE.as_string())
    server.quit()

def send_email_plain(emailFrom, emailTo, subject, content, mailServer):
    
    msg = ''
    msg += f"Subject: {subject}\n"
    msg += content

    server = SMTP(host=mailServer, port=25)    
    
    server.sendmail(emailFrom, emailTo, msg)
    server.quit()