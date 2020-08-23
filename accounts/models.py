
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.db import models
# Create your models here.

class pree_user_manager(BaseUserManager):
    def create_user(self,email,nick_name,phone,date_of_birth,profile_ph,password=None):
        if not email:
            raise ValueError('아이디는 이메일 형식이여야 합니다.')

        user = self.model(
            email.self.nomailize_email(email),
            date_of_birth = date_of_birth,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user
    def create_superuser(self,email,nick_name,phone,date_of_birth,profile_ph,password):
        user = self.model(
            email.self.nomailize_email(email),
            date_of_birth=date_of_birth,
        )
        user.is_admin =True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email=models.EmailField(unique=True, verbose_name='이메일')
    nick_name=models.CharField(unique=True, verbose_name='닉네임',max_length=255)
    phone=models.CharField(unique=True, verbose_name='전화번호',max_length=255)
    date_of_birth=models.DateTimeField(unique=True, verbose_name='생년월일')
    profile_ph=models.ImageField(unique=True, verbose_name='프로필사진')
    is_active=models.BooleanField(default=True, verbose_name='활성화 확인')
    is_admin=models.BooleanField(default=False, verbose_name='관리자 확인')

    object = pree_user_manager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['닉네임']

    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,perm,obj=None):
        return True

    def is_staff(self):
        return self.is_admin

