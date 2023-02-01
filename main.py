
import imap_tools
from bs4 import BeautifulSoup


my_email = ""
my_pass = ""

mailbox = imap_tools.MailBox('imap.gmail.com').login(my_email, my_pass)

with open('email.txt', 'a') as file:




    for msg in mailbox.fetch('UNSEEN Subject "Sierra Tiny Houses Info Request"', charset='utf8'):
        soup = BeautifulSoup(msg.html)
        file.write("Message id: " + str(msg.uid) + '\n')
        file.write("Message Subject: " + msg.subject + '\n')
        file.write("Message Date: " + str(msg.date) + '\n')
        file.write("Message Text: " + soup.get_text() + '\n')




'''
    for msg in mailbox.fetch('UNSEEN Subject "Sierra Tiny Houses Info Request"', charset='utf8'):
        soup = BeautifulSoup(msg.html)
        for link in soup.find_all('a'):
            if link.has_attr('href'):
                file.write("Link: " + link['href'] + '\n')
        reply_to = msg.sender_email
        file.write("Message Text: " + soup.get_text() + '\n')
        #file.write("Sender email: " + reply_to + '\n')
        '''





