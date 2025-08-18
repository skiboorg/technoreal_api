from django.db import models
from pytils.translit import slugify
from ckeditor_uploader.fields import RichTextUploadingField

# ===========================
# Отзывы клиентов
# ===========================
class ClientReview(models.Model):
    order = models.PositiveIntegerField("Порядок вывода", default=0)
    text = models.TextField("Текст отзыва")
    client_name = models.CharField("Имя клиента", max_length=255)
    client_position = models.CharField("Должность клиента", max_length=255, blank=True, null=True)
    client_photo = models.ImageField("Фото клиента", upload_to="client_reviews/", blank=True, null=True)

    class Meta:
        ordering = ["order"]
        verbose_name = "Отзыв клиента"
        verbose_name_plural = "Отзывы клиентов"

    def __str__(self):
        return self.client_name

class Variant(models.Model):
    name = models.CharField('Название', max_length=255)
    text = models.TextField('Материал')
    text1 = models.TextField('Результат работы')

    def __str__(self):
        return self.name

class VariantOption(models.Model):
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE, related_name='options')
    text = models.TextField()


# ===========================
# Услуги
# ===========================
class Service(models.Model):
    variants = models.ManyToManyField(Variant,blank=True)
    order = models.PositiveIntegerField("Порядок вывода", default=0)
    name = models.CharField("Название услуги", max_length=255)
    slug = models.CharField("Название услуги", max_length=255, editable=False)
    cover = models.ImageField("Обложка", upload_to="services/covers/")
    short_description = models.TextField("Короткое описание", blank=True)
    production_time = models.TextField("Сроки изготовления", blank=True)
    heading_1 = models.TextField("Заголовок 1", blank=True)
    target_audience = models.TextField("Для кого", blank=True)
    recommendation = models.TextField("Рекомендация", blank=True)
    heading_implementation = models.TextField("Заголовок 'Реализация'", blank=True)
    large_photo = models.ImageField("Фото большое 1", upload_to="services/large_photos/", blank=True, null=True)
    large_photo_1 = models.ImageField("Фото большое 2", upload_to="services/large_photos/", blank=True, null=True)
    show_on_main = models.BooleanField("Показывать на главной", default=False)
    projects = models.ManyToManyField("Project", blank=True, related_name="services_attached", verbose_name="Прикрепленные проекты")

    class Meta:
        ordering = ["order"]
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class ServiceGalleryImage(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="images", verbose_name="Проект")
    image = models.ImageField("Фото галереи", upload_to="service/gallery/")

    def __str__(self):
        return f"Gallery image for {self.service.name}"
# ===========================
# Проекты
# ===========================
class ProjectResult(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="results", verbose_name="Проект")
    order = models.PositiveIntegerField("Порядок вывода", default=0)
    title = models.CharField("Название", max_length=255)
    text = models.TextField("Текст", blank=True)
    photo = models.ImageField("Фото", upload_to="projects/results/")

    class Meta:
        ordering = ["order"]
        verbose_name = "Результат проекта"
        verbose_name_plural = "Результаты проекта"

    def __str__(self):
        return f"{self.project.name} - {self.title}"




class ProjectGalleryImage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="gallery_images", verbose_name="Проект")
    image = models.ImageField("Фото галереи", upload_to="projects/gallery/")

    def __str__(self):
        return f"Gallery image for {self.project.name}"


class Project(models.Model):
    name = models.CharField("Название проекта", max_length=255)
    slug = models.CharField("Название услуги", max_length=255, editable=False)
    services = models.ManyToManyField(Service, verbose_name="Связанные услуги")
    task = models.TextField("Задача", blank=True)
    cover = models.ImageField("Обложка", upload_to="projects/covers/")
    large_photo_1 = models.ImageField("Фото большое 1", upload_to="projects/large_photos/", blank=True, null=True)
    large_photo_2 = models.ImageField("Фото большое 2", upload_to="projects/large_photos/", blank=True, null=True)
    heading = models.CharField("Заголовок", max_length=255, blank=True)
    heading_1 = models.CharField("Заголовок 1", max_length=255, blank=True)
    text_1 = models.TextField("Текст 1", blank=True)
    heading_2 = models.CharField("Заголовок 2", max_length=255, blank=True)
    text_2 = models.TextField("Текст 2", blank=True)
    client_review_text = models.TextField("Отзыв клиента", blank=True)
    client_name = models.CharField("Имя клиента", max_length=255, blank=True)
    client_position = models.CharField("Должность клиента", max_length=255, blank=True)
    client_photo = models.ImageField("Фото клиента", upload_to="projects/clients/", blank=True, null=True)
    show_on_main = models.BooleanField("Показывать на главной", default=False)

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)