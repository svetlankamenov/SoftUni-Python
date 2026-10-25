class Email:
    def __init__(self, sender, receiver, content, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

email_list = []

while True:
    info = input()
    if info == "Stop":
        break

    info = info.split(" ")
    email_list.append(Email(info[0], info[1], info[2]))

info = input().split(", ")
info = list(map(int, info))

for i in info:
    email_list[i].send()

for email in email_list:
    print(email.get_info())