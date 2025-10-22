from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Order(models.Model):
    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы' 

    WINDOW_TYPES = [
        ('residential', 'Оконная рама (жилое помещение)'),
        ('commercial', 'Витрина (коммерческое помещение)'),
        ('car', 'Автомобильное стекло'),
        ('stained', 'Витражное стекло'),
        ('other', 'Другое'),
    ]

    PREFERRED_TIMES = [
        ('morning', 'Утром (9:00-12:00)'),
        ('afternoon', 'Днем (12:00-17:00)'),
        ('evening', 'Вечером (17:00-20:00)'),
        ('weekend', 'Выходные'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, null=True, verbose_name='Электронная почта')
    window_type = models.CharField(max_length=20, choices=WINDOW_TYPES, verbose_name='Вид работ')
    preferred_time = models.CharField(max_length=20, choices=PREFERRED_TIMES, blank=True, null=True, verbose_name='Назначенное время')
    message = models.TextField(blank=True, null=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    creator = models.ForeignKey( 
        User, 
        on_delete=models.CASCADE,
        default=None,
        verbose_name='Создатель заказа' 
    ) 

    def __str__(self):
        return f"{self.name} - {self.window_type}"
