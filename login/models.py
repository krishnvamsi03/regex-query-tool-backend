from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
import pytz
import datetime
import uuid
import os
import binascii

# Create your models here.


class userDetails(models.Model):
    userId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=15)
    passward = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    isUserVerified = models.BooleanField(default=False)
    createdOn = models.DateTimeField(default=timezone.now)
    modifiedOn = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class language(models.Model):
    languageId = models.UUIDField(
        primary_key=uuid.uuid4, default=uuid.uuid4, editable=False)
    languageName = models.CharField(max_length=50)

    def __str__(self):
        return self.languageName


class regex(models.Model):
    regexId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    regexName = models.CharField(max_length=100)
    regexPattern = models.CharField(max_length=100)
    regexLanguage = models.ForeignKey(
        to=language, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.regexName


class savedRegex(models.Model):
    savedRegexId = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.ForeignKey(
        to=userDetails, on_delete=models.SET_NULL, null=True)
    regexId = models.ForeignKey(to=regex, on_delete=models.SET_NULL, null=True)


class authToken(models.Model):
    key = models.CharField(_("Key"), max_length=40, primary_key=True,
                           default=binascii.hexlify(os.urandom(20)).decode())
    user = models.OneToOneField(userDetails, on_delete=models.CASCADE)
    created = models.DateTimeField(_("Created"), auto_now_add=True)

    class Meta:
        verbose_name = _("Token")
        verbose_name_plural = _("Tokens")

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key
