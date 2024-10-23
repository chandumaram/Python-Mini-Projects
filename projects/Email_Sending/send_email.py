import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        
        # Attach the email body
        message.attach(MIMEText(body, 'plain'))

        # Create SMTP session for sending the mail
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Use Gmail with port 587
        server.starttls()  # Enable security
        
        # Log in to the Gmail account
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        
        # Close the connection
        server.quit()

        print(f"Email successfully sent to {recipient_email}")

    except Exception as e:
        print(f"Failed to send email. Error: {str(e)}")


# Example usage
sender_email = "no-reply@StaffBond.com"
sender_password = "***************"
recipient_email = "chandumaram333@gmail.com"
subject = "Test Email"
body = "This is a test email sent from a Python script."

if  __name__ == "__main__":
    send_email(sender_email, sender_password, recipient_email, subject, body)
