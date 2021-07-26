from django.db import models


class Course(models.Model):
    name_course = models.CharField(max_length=50, unique=True, verbose_name='Название курса')
    slug_course = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    name_subject = models.CharField(max_length=50, verbose_name='Пердмет')
    short_description = models.CharField(max_length=200, verbose_name='Короткое описание')
    long_description = models.TextField(verbose_name='Длинное описание')
    image_course = models.ImageField(verbose_name='Картинка курса')
    pub_date = models.DateField(verbose_name='Дата начала')

    def __str__(self):
        return f'{self.name_course} по {self.name_subject}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Type(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class BaseForArticle(models.Model):
    name_rus = models.CharField(max_length=50, unique=True, verbose_name='Название на рус')
    slug_article = models.SlugField(max_length=200, unique=True, verbose_name='URL')
    short_description = models.CharField(max_length=200, verbose_name='Короткое описание')
    long_description = models.TextField(verbose_name='Длинное описание')
    image = models.ImageField(verbose_name='Картинка месяца', blank=True, null=True)
    type_model = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name='Тип',
                                   related_name='type_model_set')
    pub_date = models.DateField(verbose_name='Дата начала')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс',
                               related_name='bind_course_set')

    def __str__(self):
        return f'{self.type_model} : {self.name_rus}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Homework(models.Model):
    number = models.PositiveSmallIntegerField(default=1, verbose_name='Номер домашнего задания')
    pdf_file_for_student = models.FileField(blank=True, null=True, verbose_name='Домашнее задание без решения')
    pdf_file_for_teacher = models.FileField(blank=True, null=True, verbose_name='Домашнее задание с решением')
    pub_date_for_student = models.DateTimeField(verbose_name='Дата публикации без решения')
    deadline = models.DateTimeField(verbose_name='Дедлайн')
    month = models.ForeignKey(BaseForArticle, on_delete=models.CASCADE, verbose_name='Месяц',
                              related_name='bind_month_set')

    def __str__(self):
        return f'Домашнее задание №{self.number}'

    class Meta:
        verbose_name = 'Домашнее задание'
        verbose_name_plural = 'Домашние задания'
