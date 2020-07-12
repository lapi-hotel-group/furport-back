from unicodedata import east_asian_width

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MultibyteCharacterValidator:
    """
    Validate whether the password contains multibyte character.
    """

    def validate(self, password, user=None):
        valid = re.search(r"^[a-zA-Z0-9!-/:-@¥[-`{-~]*$", password)

        if valid is None:
            raise ValidationError(
                _("This password contains multibyte character."),
                code="password_contains_multibyte_character",
            )

    def get_help_text(self):
        return _("Your password can't contain multibyte character. ")
