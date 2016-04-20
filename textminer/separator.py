import re


def words(string):
    words = re.findall(r'\w*[A-Za-z-]\w*', string)
    if len(words) < 1:
        return None
    else:
        return words


def phone_number(string):
    phone_num = re.search(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$', string)
    if phone_num:
        area_code, prefix, number, extension = phone_num.groups()
        return {'area_code': area_code, 'number': '{}-{}'.format(prefix,
                number)}
    else:
        return None

# phone number ^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$


def money(string):
    mo_problems = re.search(r'(^$)(\d,\.)')
    dolla, number = mo_problems.groups
    return {'currency': dolla, 'amount': float(number)}
