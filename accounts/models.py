
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db import models
# Create your models here.



class UserManager(BaseUserManager):
    def _create_user(self,email,username,password,**extra_fields):
        if not email:
            raise ValueError('아이디는 이메일 형식이여야 합니다.')
        username = self.model.normalize_username(username)
        user = self.model(email = email,username= username, **extra_fields)
        user.set_password(password)
        user.save(using= self.db)
        return user

    def create_user(self,email,username="",password = None, **extra_fields):
        extra_fields.setdefault('is_admin', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email,username="관리자", password=None , **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('슈퍼유저는 반드시 is_admin가 참이여야합니다')
        return self._create_user(email,username,password,**extra_fields)


class User(AbstractUser):
    email=models.EmailField(
        unique=True,
        verbose_name='이메일',
        max_length=255
    )
    username = models.CharField(
        max_length=10,
        verbose_name='username',
        default=""
    )
    phone=models.CharField(
        verbose_name='전화번호',
        max_length=255
    )
    date_of_birth=models.DateTimeField(
        verbose_name='생년월일',
        null=True
    )
    is_active=models.BooleanField(
        default=True,
        verbose_name='활성화 확인')
    is_admin=models.BooleanField(
        default=False,
        verbose_name='관리자 확인'
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name='슈퍼유저 확인'
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='스태프확인'
    )

    object = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','date_of_birth']

    def __str__(self):
        return self.email



