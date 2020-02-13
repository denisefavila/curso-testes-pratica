import pytest
from examples.identifier import Identifier


@pytest.fixture()
def identifier():
    return Identifier()


@pytest.mark.parametrize('identifier_string', [
    'a',
    'ab',
    'abcde',
    'abcdef',
    'a1',
])
def test_all_valid_cases(identifier_string, identifier):

    is_valid = identifier.validate_identifier(identifier_string)

    assert is_valid is True


@pytest.mark.parametrize('identifier_string', [
    '',
    'abcdefg',
    '1a',
    'açaí'
])
def test_all_invalid_cases(identifier_string, identifier):

    is_valid = identifier.validate_identifier(identifier_string)

    assert is_valid is False