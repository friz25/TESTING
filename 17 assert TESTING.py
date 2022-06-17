# Написать функцию проверки "силы" пароля, возвращает всегда строку
# - если пароль короче 8 символов то вернуть Too Weak
# - если пароль содержить только цифры, только строчные, только заглавные то вернуть Weak
# - если пароль содержит символы любых 2 наборов вернуть Good
# - если пароль содержит символы любых 3 наборов, вернуть Very Good
import string


def passord_strength(value: str) -> str:
    if len(value) < 8:
        return 'Too Weak'
    digits = string.digits  # цифры
    lowers = string.ascii_lowercase  # буквы
    uppers = lowers.upper()  # большие буквы
    count = 0
    for symbols in (digits, lowers, uppers):
        if any(e in symbols for e in value):
            count += 1
            continue
    if count == 3:
        return 'Very Good'
    return 'Weak' if count == 1 else 'Good'


if __name__ == '__main__':
    assert passord_strength('') == 'Too Weak'  # assert = проверить
    assert passord_strength('1234567') == 'Too Weak'
    assert passord_strength('qazwsxe') == 'Too Weak'
    assert passord_strength('QAZWSXE') == 'Too Weak'
    assert passord_strength('QAaa1') == 'Too Weak'
    assert passord_strength('12345678') == 'Weak'
    assert passord_strength('1234567123138') == 'Weak'
    assert passord_strength('aqsressd') == 'Weak'
    assert passord_strength('adasdadasdadada') == 'Weak'
    assert passord_strength('ASDSADSD') == 'Weak'
    assert passord_strength('ASDSAAADDASDADSD') == 'Weak'
    assert passord_strength('1234qasx') == 'Good'
    assert passord_strength('1234qasxsadas12') == 'Good'
    assert passord_strength('1234QASD') == 'Good'
    assert passord_strength('1234QASDASDAS12') == 'Good'
    assert passord_strength('QASDqasx') == 'Good'
    assert passord_strength('asadADASDADADasd') == 'Good'
    assert passord_strength('123asdGFD') == 'Very Good'
    assert passord_strength('12343553435Dd') == 'Very Good'
    assert passord_strength('asdaddasdadD2') == 'Very Good'
    assert passord_strength('DSDAQEWGHDF2s') == 'Very Good'
