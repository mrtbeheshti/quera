def check_registration_rules(**kwargs):
    valids = []
    for username, password in kwargs.items():
        if (
            len(password) >= 6
            and len(username) >= 4
            and username != "quera"
            and username != "codecup"
            and not password.isdigit()
        ):
            valids.append(username)
    return valids


print(check_registration_rules(username="password", sadegh="He3@lsa"))
print(
    check_registration_rules(
        quera="qwerty80", mmdreza="monday80", ali="aliali@", mammad="salam"
    )
)
