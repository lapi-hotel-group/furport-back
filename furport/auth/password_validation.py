from unicodedata import east_asian_width
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MultibyteCharacterValidator:
    """
    Validate whether the password contains multibyte character.
    """

    def validate(self, password, user=None):
        for c in password:
            if east_asian_width(c) != "Na":
                raise ValidationError(
                    _("This password contains multibyte character."),
                    code="password_contains_multibyte_character",
                )
        pass

    def get_help_text(self):
        return _("Your password can't contain multibyte character. ")
