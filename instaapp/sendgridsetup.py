import sendgrid
from sendgrid.helpers.mail import *

def send_notification(user, comment_text):
    my_client = sendgrid.SendGridAPIClient(apikey='X')
    

    from_email = Email("insta.mriu.test.0@gmail.com")
    to_email = Email("insta.mriu.test.1@gmail.com")
    subject = "Post Notification"
    content = Content("text/plain", str(user) +"commented" +str(comment_text))
    mail = Mail(from_email, subject, to_email, content)
    response = my_client.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
