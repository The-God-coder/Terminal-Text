
import smtplib
def sendEmail(phoneNumber, message, SenderEmail, SenderPassword):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(SenderEmail, SenderPassword)
    s.sendmail(SenderEmail, f"{phoneNumber}@vtext.com", message)
    s.quit()

if __name__ == "__main__":
    sendEmail(input("Phone Num:   "), input("Message:   "), input("Email:   "), input("Password:   "))