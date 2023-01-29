from django.db import models


class Subscription(models.Model):
    """Подписка"""
    email = models.EmailField()

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.email


class Contact(models.Model):
    """Контакты"""
    name = models.CharField("Имя", max_length=50)
    number = models.CharField("Номер телефона", max_length=50)
    email = models.EmailField("Email")
    message = models.TextField("Сообщения")

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Запись'

    def __str__(self):
        return self.name
