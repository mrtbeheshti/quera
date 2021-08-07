import re


def validate_email(email):
    return True if (re.match(r'^[A-Za-z0-9\_\.]+\@[A-Za-z0-9]+\.[a-zA-Z]{3}$', email))else False


def validate_phone(number):
    return True if (re.match(r'^09[0-9]{9}$', number) or
                    re.match(r'^\+989[0-9]{9}$', number) or
                    re.match(r'^00989[0-9]{9}$', number)) else False
