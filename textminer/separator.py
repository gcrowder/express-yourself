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
    if len(string) == 1 or string[0] != '$' or string[1] == '$':
        return None
    mo_problems = re.search(r'((^\$\d{1,}\.\d{2})|(^\$\d{1,3},\d{3},\d{3}\.\d{2})|(^\$\d,\d{3}\.\d{2})|(^\$\d{1,3},\d{3},\d{3})|(^\$\d{1,3},\d{3})|(^\$\d{1,4}))', string)
    if len(string) == len(mo_problems.group(1)):
        dollas = mo_problems.group(1)
        return {'currency': '$', 'amount': float(dollas[1:].replace(',', ''))}
    else:
        return None

def zipcode(string):
    code = re.findall(r'^\d{5}-\d{4}', string)
    zip_code, plus_four = code.groups()
    return {'zip': zip_code, 'plus4': plus_four}
