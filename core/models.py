from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class Profile(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField("email address", unique=True)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

class ProfileKid(Profile):
    kid_name = models.CharField(max_length=100, verbose_name='Имя ребенка')
    profile = models.ForeignKey(Profile, related_name='дети', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.kid_name} (родитель: {self.profile})'

class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    children_section = models.ForeignKey('ChildrenSection', on_delete=models.CASCADE)


class Trainer(models.Model):
    trainer_name = models.CharField(max_length=100)
    trainer_last_name = models.CharField(max_length=100)
    trainer_description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.trainer_name} {self.trainer_last_name}"


class ChildrenSection(models.Model):
    CLUB_KINDS_CHOICES = [
        ('1', 'спорт'),
        ('2', 'развитие'),
        ('3', 'искусство')
        # Добавьте другие варианты по вашему усмотрению
    ]
    rating = models.IntegerField(default=0, choices=[(i, str(i)) for i in range(1, 6)])
    name_club = models.CharField(max_length=100)
    trainers = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='sections')
    description = models.TextField()
    club_kinds = models.CharField(max_length=20, choices=CLUB_KINDS_CHOICES)
    record = models.BooleanField(default=False)

    # def filter_by_club_kinds(club_kinds_value):
    #     filtered_sections = ChildrenSection.objects.filter(club_kinds=club_kinds_value)
    #     serializer = ChildrenSectionSerializer(filtered_sections, many=True)
    #     return ({'filtered_sections': serializer.data})
    def __str__(self):
        return f"{self.name_club} ({self.trainers.trainer_name} {self.trainers.trainer_last_name})"


