import smtplib

from data import config_4am_psybot


def send_email(text, encode='utf-8'):

    user = config_4am_psybot.EMAIL_NAME
    passwd = config_4am_psybot.EMAIL_TOKEN
    server = 'smtp.mail.ru'
    port = 587

    subject = 'Your email subject'
    to = config_4am_psybot.EMAIL_NAME
    charset = 'Content-Type: text/plain; charset=utf-8'
    mime = 'MIME-Version: 1.0'

    body = '\r\n'.join((f'From: {user}', f'To: {to}',
                        f'Subject: {subject}', mime, charset, '', text))

    try:
        smtp = smtplib.SMTP(server, port)
        smtp.ehlo
        smtp.starttls()
        smtp.ehlo
        smtp.login(user, passwd)
        smtp.sendmail(user, to, body.encode('utf-8'))
    except smtplib.SMTPException as Ex:
        print('Smth go wrong')
        raise Ex
    finally:
        smtp.quit()
