from django.db import models


NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):

    title = models.CharField(max_length=150, verbose_name='заголовок')

    preview = models.ImageField(upload_to='helper', verbose_name='превью', **NULLABLE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = "Категории"


class Helper(models.Model):
    STATUS_NEW = 'new'
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'

    STATUSES = (
        (STATUS_NEW, 'новая'),
        (STATUS_DRAFT, 'черновик'),
        (STATUS_PUBLISHED, 'опубликовано'),
    )

    title = models.CharField(max_length=150, verbose_name='заголовок')
    body = models.TextField(verbose_name='содержимое')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    status = models.CharField(choices=STATUSES, default=STATUS_NEW, max_length=10, verbose_name='статус')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Шпаргалка'
        verbose_name_plural = "Шпаргалки"

