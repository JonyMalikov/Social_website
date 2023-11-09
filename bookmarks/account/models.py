from django.conf import settings
from django.db import models


class Profile(models.Model):
    """Профиль пользователя"""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="дата рождения"
    )
    photo = models.ImageField(
        upload_to="users/%Y/%m/%d/", blank=True, verbose_name="фото"
    )

    def __str__(self):
        return f"Profile of {self.user.username}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["user__username"]
