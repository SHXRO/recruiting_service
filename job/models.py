from django.db import models


class Category(models.Model):
    name = models.CharField("Название региона", max_length=150)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"


class Vacancy(models.Model):
    Y = True
    N = False

    """Вакансии"""
    available = models.BooleanField("Отображать вакансию", default=True)
    name = models.CharField("Название вакансии", max_length=150)
    city = models.CharField("Город", max_length=150)
    category = models.ForeignKey(Category, verbose_name="Регион", on_delete=models.SET_NULL, null=True)
    pay = models.CharField("Введите зарплату", max_length=150)
    snippet = models.TextField("Сниппет карточки", max_length=300)
    objects = models.Manager()
    # Информация для полной страницы
    work_busy = models.CharField("Тип занятости", max_length=150, default='')
    work_experience = models.CharField("Опыт работы", max_length=150, default='', null=True, blank=True)
    Responsibilities_1 = models.TextField("Введите обязанности", max_length=150, default='-', null=True, blank=True)
    Responsibilities_2 = models.TextField("Введите обязанности", max_length=150, default='-', null=True, blank=True)
    Responsibilities_3 = models.TextField("Введите обязанности", max_length=150, default='-', null=True, blank=True)
    Responsibilities_4 = models.TextField("Введите обязанности", max_length=150, default='-', null=True, blank=True)
    Responsibilities_5 = models.TextField("Введите обязанности", max_length=150, default='-', null=True, blank=True)
    Requirements_1 = models.TextField("Введите требования", max_length=150, default='-', blank=True)
    Requirements_2 = models.TextField("Введите требования", max_length=150, default='-', blank=True)
    Requirements_3 = models.TextField("Введите требования", max_length=150, default='-', blank=True)
    Requirements_4 = models.TextField("Введите требования", max_length=150, default='-', blank=True)
    Requirements_5 = models.TextField("Введите требования", max_length=150, default='-', blank=True)
    Terms_1 = models.TextField("Введите условия", max_length=150, default='', null=True, blank=True)
    Terms_2 = models.TextField("Введите условия", max_length=150, default='', null=True, blank=True)
    Terms_3 = models.TextField("Введите условия", max_length=150, default='', null=True, blank=True)
    Core_skills_1 = models.TextField("Введите ключевые навыки", max_length=150, default='', null=True, blank=True)
    Core_skills_2 = models.TextField("Введите ключевые навыки", max_length=150, default='', null=True, blank=True)
    Core_skills_3 = models.TextField("Введите ключевые навыки", max_length=150, default='', null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class JobResponse(models.Model):
    N = 'Новый отклик'
    I = "В процессе рассмотрения"
    C = "Закрытый отклик"

    RESPONSE_STATUS = [
        ('N', 'Новый отклик'),
        ('I', 'В процессе рассмотрения'),
        ('C', 'Закрытый отклик')
    ]

    COMMENTS = [
        ('A', 'Некорректно заполнен отклик'),
        ('B', 'Штат сотрудников уже полон'),
        ('C', 'Дублирующий отклик'),
        ('D', 'Кандидат не подходит по критериям'),
        ('E', 'Кандидат подходит')
    ]

    name = models.CharField('Имя', max_length=50)
    email = models.EmailField()
    surname = models.CharField('Фамилия', max_length=50, default='')
    number = models.CharField("Номер телефона", max_length=12)
    job_application = models.FileField(upload_to="Uploaded Files/", default='')
    status = models.CharField("Статус рассмотрения", max_length=1, choices=RESPONSE_STATUS, default='N')
    comments = models.CharField("Решение по отклику", max_length=1, choices=COMMENTS, default=' ')
    post = models.ForeignKey(Vacancy, verbose_name="Вакансия", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name},{self.post}'

    class Meta:
        verbose_name = "Тикет"
        verbose_name_plural = "Тикетов"
