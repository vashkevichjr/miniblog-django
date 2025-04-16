from django.db import models

class Post(models.Model):
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField("Текст записи")
    author = models.CharField("Имя автора", max_length=100)
    date = models.DateField("Дата публикации")
    image = models.ImageField("Изображение", upload_to = "image/%Y")
    def __str__(self):
        return f"{self.title} + {self.author}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

class Comment(models.Model):
    email = models.EmailField("Email")
    name = models.CharField("Имя", max_length=100)
    text = models.CharField("Текст", max_length=500)
    post = models.ForeignKey(Post, verbose_name="Публикация", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} + {self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Likes(models.Model):
    ip = models.CharField("IP-адрес", max_length=100)
    post = models.ForeignKey(Post, verbose_name="Публикация", on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.name} + {self.post}"

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"
# Create your models here.
