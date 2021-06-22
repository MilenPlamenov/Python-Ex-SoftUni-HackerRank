class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class NameTooShortError(Exception):
    pass


valid = True
domain_list = ['.com', '.bg', '.org', '.net']
while True:
    email = input()
    if email == "End":
        break
    if "@" not in email:
        valid = False
        raise MustContainAtSymbolError("Email must contain @")
    else:
        name, rest = email.split("@")
        res, domain = email.split(".")
        domain = "." + domain
    if domain not in domain_list:
        valid = False
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if len(name) < 5:
        valid = False
        raise NameTooShortError("Name must be more than 4 characters")
    if valid:
        print("Email is valid")