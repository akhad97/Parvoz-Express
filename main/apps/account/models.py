from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from ..common.models import BaseModel, BaseMeta
from .managers.user import UserManager
from django.conf import settings



class Region(BaseModel):
    title = models.CharField(max_length=200)

    class Meta(BaseMeta):
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')

    def __str__(self):
        return f'{self.title}'

class AgentIDTypeChoices(models.TextChoices):
    NMA10001 = 'NMA1/0001', _('NMA1/0001')
    NMA20001 = 'NMA2/0001', _('NMA2/0001')
    NMA30001 = 'NMA3/0001', _('NMA3/0001')
    NMA40001 = 'NMA4/0001', _('NMA4/0001')
    QQN0001 = 'QQN/0001', _('QQN/0001')
    MRN0001 = 'MRN/0001', _('MRN/0001')
    AZN0001 = 'AZN/0001', _('AZN/0001')
    TAS0001 = 'TAS/0001', _('TAS/0001')
    SKD0001 = 'SKD/0001', _('SKD/0001')


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    phone_number = models.CharField(max_length=255, unique=True,
                             verbose_name=_("Телефонный номер"))
    full_name = models.CharField(
        null=True, blank=True, max_length=50, verbose_name=_("Имя Фамилия"))
    email = models.EmailField()
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='regions', null=True)
    is_moderator = models.BooleanField(default=False)
    is_for_flight = models.BooleanField(default=False)
    is_for_hotel = models.BooleanField(default=False)
    is_for_visa = models.BooleanField(default=False)
    is_working_with_agent = models.BooleanField(default=False)
    is_for_finance = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)
    is_outfit = models.BooleanField(default=False)
    agent_id = models.CharField(max_length=255, choices=AgentIDTypeChoices.choices, null=True, blank=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False, 
        help_text=_(
            "Designates whether the user can log into this admin site.",
        ),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting account."
        ),
    )
    is_superuser = models.BooleanField(_("superuser status"), default=False)
    objects = UserManager()

    USERNAME_FIELD = "phone_number"

    class Meta(BaseMeta):
        ordering = ("-id",)
        verbose_name = _("user")
        verbose_name_plural = _("users")


    def __str__(self):
        return f"{self.full_name}"