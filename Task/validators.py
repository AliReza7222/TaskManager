import re
from django.core.exceptions import ValidationError


# This validator checked the text: contains words and numbers and _ but starts with words.
def check_text(value):
    # check the value against the regex pattern. If the pattern does not match, regex_check is 0
    regex_check = re.match('^[^\d_][a-zA-Z_\d]+', value) or 0
    if regex_check:
        return value
    raise ValidationError(
        'Title is invalid Please enter a valid title that starts with words and contains words, numbers, and \'_\' '
    )

