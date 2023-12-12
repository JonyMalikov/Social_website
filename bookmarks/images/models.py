from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Image(models.Model):
    """Изображения"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="images_created",
        on_delete=models.CASCADE,
        verbose_name="пользователь",
    )
    title = models.CharField(max_length=200, verbose_name="заголовок")
    slug = models.SlugField(max_length=200, blank=True, verbose_name="слаг")
    url = models.URLField(max_length=200, verbose_name="URL")
    image = models.ImageField(
        upload_to="images/%Y/%m/%d/", verbose_name="изображение"
    )
    description = models.TextField(blank=True, verbose_name="описание")
    created = models.DateField(auto_now_add=True, verbose_name="создан")
    user_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="images_liked",
        blank=True,
        verbose_name="лайкнул",
    )

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"
        indexes = [
            models.Index(fields=["-created"]),
        ]
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """создание слага"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
