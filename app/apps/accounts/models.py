from __future__ import unicode_literals
from datetime import timezone
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

from ..erp_data.models import Counterparty


class User(AbstractBaseUser, PermissionsMixin):
    login = models.CharField(_('login'), max_length=100, unique=True)
    email = models.EmailField(_('email address'), blank=True, null=True)
    name = models.CharField(_('name'), max_length=150, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_staff = models.BooleanField(_('is staff'), default=True)
    is_active = models.BooleanField(_('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'login'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_counterparty_guid(self):
        counterparty = Counterparty.objects.filter(counterparty_inn=self.login)
        if not counterparty:
            return None
        return counterparty[0].guid


