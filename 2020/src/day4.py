import os, re

os.chdir('../github/advent/2020')

def test_fields(passport):
    """
    checks if there are all eight fields, with the cid field being optional
    """
    if passport.count(':') == 8:
        return 'valid'
    elif passport.count(':') == 7 and passport.find('cid:') == -1:
        return 'valid'
    else:
        return 'invalid'


def test_byr(passport):
    """
    checks if the birth year is between 1920 and 2002
    """
    match = re.search('(byr:)([0-9]{4})(\s|$)', passport)
    if match == None:
        return 'invalid'
    if int(match.group(2)) >= 1920 and int(match.group(2)) <= 2002:
        return 'valid'
    else:
        return 'invalid'


def test_iyr(passport):
    """
    checks if the issue year is between 2010 and 2020
    """
    match = re.search('(iyr:)([0-9]{4})(\s|$)', passport)
    if match == None:
        return 'invalid'
    if int(match.group(2)) >= 2010 and int(match.group(2)) <= 2020:
        return 'valid'
    else:
        return 'invalid'


def test_eyr(passport):
    """
    checks if the expiration year is between 2020 and 2030
    """
    match = re.search('(eyr:)([0-9]{4})(\s|$)', passport)
    if match == None:
        return 'invalid'
    if int(match.group(2)) >= 2020 and int(match.group(2)) <= 2030:
        return 'valid'
    else:
        return 'invalid'


def test_hgt(passport):
    """
    checks if the height is either 150-193 cm or 59-76 in
    """
    match = re.search('(hgt:)([0-9]{2,3})(cm|in)(\s|$)', passport)
    if match == None:
        return 'invalid'
    if match.group(3) == 'cm':
        if int(match.group(2)) >= 150 and int(match.group(2)) <= 193:
            return 'valid'
        else:
            return 'invalid'
    if match.group(3) == 'in':
        if int(match.group(2)) >= 59 and int(match.group(2)) <= 76:
            return 'valid'
        else:
            return 'invalid'
    else:
        return 'invalid'


def test_hcl(passport):
    """
    checks if the hair color is a hex value
    """
    match = re.search('(hcl:)(#[0-9a-f]{6})(\s|$)', passport)
    if match == None:
        return 'invalid'
    else:
        return 'valid'


def test_ecl(passport):
    """
    checks if the eye color is in a set list
    """
    match = re.search('(ecl:)([a-z]{3})(\s|$)', passport)
    if match == None:
        return 'invalid'
    if str(match.group(2)) in ['amb','blu','brn','gry','grn','hzl','oth']:
        return 'valid'
    else:
        return 'invalid'


def test_pid(passport):
    """
    checks if the pid is 9 digits long
    """
    match = re.search('(pid:)([0-9]{9})(\s|$)', passport)
    if match == None:
        return 'invalid'
    else:
        return 'valid'


def advent5a(passport):
    """
    for the answer to the first part, it only checks if all the fields are present
    """
    validity = 0
    if test_fields(passport) == 'valid': validity += 1
    if validity == 1:
        return 1
    else:
        return 0


def advent5b(passport):
    """
    for the answer to the second part, it checks all eight tests
    """
    validity = 0
    if test_fields(passport) == 'valid': validity += 1
    if test_byr(passport) == 'valid': validity += 1
    if test_iyr(passport) == 'valid': validity += 1
    if test_eyr(passport) == 'valid': validity += 1
    if test_hgt(passport) == 'valid': validity += 1
    if test_hcl(passport) == 'valid': validity += 1
    if test_ecl(passport) == 'valid': validity += 1
    if test_pid(passport) == 'valid': validity += 1
    if validity == 8:
        return 1
    else:
        return 0



with open('./data/day4.txt') as f:
    passports = f.read().split('\n\n')
    total_valid, total_valid2 = 0,0
    for line in passports:
        passport = line.replace('\n',' ')
        total_valid += advent5a(passport)
        total_valid2 += advent5b(passport)
    print(total_valid, total_valid2)



# fin
