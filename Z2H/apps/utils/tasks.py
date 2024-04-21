import dramatiq
import yagmail
import os

@dramatiq.actor(priority=0, time_limit=10000)
def send_email(to_email, body, subject):
    print("Sending email to ", to_email)
    yag = yagmail.SMTP(user=os.environ["SENDER_EMAIL"], password=os.environ["SENDER_EMAIL_APP_PASSWORD"])
    yag.send(to=to_email, subject=subject, contents=body)
    print("Email sent to ", to_email)