import smtplib

gmail_user = ''
gmail_password = ''

# send an email from above gmail user account, 
def sendEmail(message):
    sent_from = gmail_user
    to = ['lfchesebrough@gmail.com', 'lx829382@dal.ca']
    subject = 'VACCINE SHIFT AVAILABLE'
    body = message

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')

