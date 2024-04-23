from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_mobile_number(value):
    if not value.isdigit() or len(value) != 10:
        raise ValidationError(
            _('Mobile number must be exactly 10 digits long.'),
            params={'value': value},
        )


class ContactDetail(models.Model):
    address = models.TextField(max_length=1000, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    mobile_number = models.CharField(max_length=10, validators=[validate_mobile_number])

    def __str__(self):
        return self.mobile_number


class ContactForm(models.Model):

    name = models.CharField(max_length=100, blank=False)
    subject = models.TextField(max_length=1000, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    message = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return self.name
