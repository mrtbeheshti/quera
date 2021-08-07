from datetime import datetime as d


def day_calculator(date):
    givenDate = d.strptime(date, '%Y-%m-%d')
    sajjadBirthday = d.strptime('1999-01-14', '%Y-%m-%d')
    if givenDate < sajjadBirthday:
        return "Not yet born"
    else:
        livedDays = (givenDate-sajjadBirthday).days
        return livedDays
