from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from website.models import Skills
from django.utils.translation import gettext_lazy as _
# Create your models here.


class JobSeekerManager(BaseUserManager):
    def create_user(self, number, password=None, **extra_fields):
        if not number:
            raise ValueError("The Email field must be set")
        # email = self.normalize_email(email)
        user = self.model(number=number, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user





class Jobseeker(AbstractBaseUser):

    name = models.CharField(max_length=50)
    surename = models.CharField(max_length=50)
    number = models.IntegerField(default=0)
    password = models.CharField(max_length=255)


    objects = JobSeekerManager()

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['name', 'surename']

    def get_my_model_name(self):
        return self._meta.model_name
    def __str__(self):
        return "{firstname} {lastname}".format(firstname=self.name,lastname=self.surename)



class Resume(models.Model):
    surname = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField(default= 0)
    university = models.CharField(max_length=255)
    start_year = models.IntegerField(default= 1351)
    end_year = models.IntegerField(default= 0)
    Workplace = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    mager = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resume/', max_length=100)
    abilities = models.ManyToManyField(Skills)

    class City(models.TextChoices):
        city1 = 'آذربایجان شرقی', _('آذربایجان شرقی')
        city2 = 'آذربایجان غربی', _('آذربایجان غربی')
        city3 = 'اردبیل', _('اردبیل')
        city4 = 'اصفهان', _('اصفهان')
        city5 = 'البرز', _('البرز')
        city6 = 'ایلام', _('ایلام')
        city7 = 'بوشهر', _('بوشهر')
        city8 = 'تهران', _('تهران')
        city9 = 'چهارمحال و بختیاری', _('چهارمحال و بختیاری')
        city10 = 'خراسان جنوبی', _('خراسان جنوبی')
        city11= 'خراسان رضوی', _('خراسان رضوی')
        city12 = 'خراسان شمالی', _('خراسان شمالی')
        city13 = 'خوزستان', _('خوزستان')
        city14 = 'زنجان', _('زنجان')
        city15 = 'سمنان', _('سمنان')
        city16 = 'سیستان و بلوچستان', _('سیستان و بلوچستان')
        city17 = 'فارس', _('فارس')
        city18 = 'قزوین', _('قزوین')
        city19 = 'قم', _('قم')
        city20 = 'کردستان', _('کردستان')
        city21 = 'کرمان', _('کرمان')
        city22 = 'کرمانشاه', _('کرمانشاه')
        city23 = 'کهگیلویه و بویراحمد', _('کهگیلویه و بویراحمد')
        city24 = 'گلستان', _('گلستان')
        city25 = 'گیلان', _('گیلان')
        city26 = 'لرستان', _('لرستان')
        city27 = 'مازندران', _('مازندران')
        city28 = 'مرکزی', _('مرکزی')
        city29 = 'هرمزگان', _('هرمزگان')
        city30 = 'همدان', _('همدان')
        city31 = 'یزد', _('یزد')
    location = models.CharField(
        max_length=50,
        choices=City.choices,
        default=City.city8,
    )

    class Gender(models.TextChoices):
        MALE = 'مرد', _('مرد')
        FEMALE = 'زن', _('زن')

    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
        default=Gender.MALE,
    )


    class Marital_status(models.TextChoices):
        Single = 'مجرد', _('مجرد')
        married = 'متاهل', _('متاهل')

    marital_status = models.CharField(
        max_length=20,
        choices=Marital_status.choices,
        default=Marital_status.Single

    )

    class Degree(models.TextChoices):
        diploma = 'دیپلم', _('دیپلم')
        Bachelor  = 'کارشناسی', _('کارشناسی')
        Master  = 'کارشناسی ارشد', _('کارشناسی ارشد')
        Doctorate  = 'دکترا', _('دکترا')
    degree = models.CharField(
        max_length=20,
        choices=Degree.choices,
        default=Degree.Bachelor,
    )

    class Field(models.TextChoices):
        AI = 'هوش مصنوعی و داده', _('هوش مصنوعی و داده')
        Network= 'شبکه', _('شبکه')
        Security= 'امنیت', _('امنیت')
        uiux = 'طراحی', _('طراحی')
        pro = 'برنامه نویسی و توسعه', _('برنامه نویسی و توسعه')
    field = models.CharField(
        max_length=20,
        choices=Field.choices,
        default=Field.AI,
    )

    class FavoritField(models.TextChoices):
        AI = 'هوش مصنوعی و داده', _('هوش مصنوعی و داده')
        Network = 'شبکه', _('شبکه')
        Security = 'امنیت', _('امنیت')
        uiux = 'طراحی', _('طراحی')
        pro = 'برنامه نویسی و توسعه', _('برنامه نویسی و توسعه')

    Favoritfield = models.CharField(
        max_length=20,
        choices=FavoritField.choices,
        default=FavoritField.AI,
    )



    def __str__(self):
        return "{firstname} {lastname}".format(firstname=self.name, lastname=self.surname)





class Resume_skill(models.Model):
    skill= models.ForeignKey(Skills, on_delete= models.CASCADE,null=True)
    resume = models.ForeignKey(Resume, on_delete= models.CASCADE,null=True)


    def __str__(self):
        return "{resume_Id}_{skill_Id}".format(resume_Id=self.resume, skill_Id=self.skill)

