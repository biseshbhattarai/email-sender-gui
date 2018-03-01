import tkinter as tk
from tkinter import *
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.label_1 = Label(text="Sender's email")
        self.label_1.grid(column=0, row=0)
        self.entry = Entry()
        
        self.entry.grid(column=0, row=2)
        self.label_2 = Label( text="Sender's password")
        self.label_2.grid(column=0, row=3)
        self.entry_2 = Entry()
        self.entry_2.grid(column=0, row=4)
        self.subject_label = Label( text="Subject")
        self.subject_label.grid(column=0, row=5)
        self.subject = Entry()
        self.subject.grid(column=0, row=6)
        self.text_label = Label( text="Body")
        self.text_label.grid(column=0, row=7)
        self.body_data = Text(height="20", width="50")
        self.body_data.grid(column=0, row=8, sticky=N+S+E+W)
        self.label_receiver = Label( text="Receiver email")
        self.label_receiver.grid(column=0, row=9)
        self.receiver_entry = Entry()
        self.receiver_entry.grid(column=0, row=10)
        self.button = Button( text="Send", command=self.send_mail)
        self.button.grid(column=0, row=12)



    def send_mail(self):
       
        email =self.entry.get()
        print(email)
        fromaddr = email
        receiver_email = self.receiver_entry.get()
        print(receiver_email)
        toaddr = receiver_email
        msg = MIMEMultipart()
        msg['from'] = fromaddr 
        msg['to'] = ''.join(toaddr)
        subject_mail = self.subject.get()
        print(subject_mail)
        msg['subject']  =  subject_mail
        body = self.body_data.get("1.0", END)
        print(body)
        msg.attach(MIMEText(body, 'plain'))
       


        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()

        server.login(fromaddr , '"hello"bisesh18')
        
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
        print("Message was succesfully sent")





        

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).grid()
    root.mainloop()