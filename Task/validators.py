import re
from django.core.exceptions import ValidationError


# This validator checked the text: contains words and numbers and _ but starts with words.
def check_text(value):
    regex_check = re.match('^[^\d_][a-zA-Z_\d]+', value) or 0
    if regex_check:
        return value
    raise ValidationError(f'Invalid value .')

