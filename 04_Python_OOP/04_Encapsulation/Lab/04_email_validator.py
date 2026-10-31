class EmailValidator:
    def __init__(self, min_length:int, mails:list, domains:list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name:str):
        if not len(name) >= self.min_length:
            return False

        return True

    def __is_mail_valid(self, mail:str):
        if not mail in self.mails:
            return False

        return True

    def __is_domain_valid(self, domain:str):
        if not domain in self.domains:
            return False

        return True

    def validate(self, email:str):
        name = email.split("@")[0]
        mail = email.split("@")[1].split(".")[0]
        domain = email.split("@")[1].split(".")[1]

        if self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain):
            return True
        else:
            return False
