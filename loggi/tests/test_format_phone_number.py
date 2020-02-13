import pytest


# numero de digitos deve ter entre 8 e 11

#
from base.utils.phone import format_phone_number


@pytest.mark.parametrize('phone_number, expected_formatted_phone_number', [
    ('31991045943', '(31) 99104-5943'),
    ('3134777515', '(31) 3477-7515'),
    ('34777515', '3477-7515'),
    ('991045943', '99104-5943'),
    ('5531991045943', '(31) 99104-5943'),
    ('553134777515', '(31) 3477-7515')
])
def test_all_cases_with_valid_phone_numbers(phone_number, expected_formatted_phone_number):

    formatted_phone_number = format_phone_number(phone_number)

    assert formatted_phone_number == expected_formatted_phone_number


@pytest.mark.parametrize('phone_number, expected_formatted_phone_number', [
    ('12345', '12345'),
    ('', ''),
    (None, None),
    ('5534777515', '3477-7515'),
    ('1', None)
])
def test_all_cases_with_invalid_phone_numbers(phone_number, expected_formatted_phone_number):

    formatted_phone_number = format_phone_number(phone_number)

    assert formatted_phone_number == expected_formatted_phone_number