import hashlib
import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta


SALT = '_SaLt'


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=256, null=False)
    ts_create = models.DateTimeField(null=False, default=timezone.now)
    auth_token = models.CharField(max_length=36, unique=True, blank=True)
    auth_expired = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} ({self.name})'

    @classmethod
    def _get_session_token(cls) -> uuid:
        """
        Метод класса для генерации ключа сессии
        :return: uuid
        """
        return str(uuid.uuid4())

    @classmethod
    def _get_session_expire_time(cls) -> str:
        """
        Метод класса для вычисления даты окончания сессии
        :return: str date
        """
        return str(timezone.now() + timedelta(hours=1))

    @classmethod
    def salt_password(cls, password) -> str:
        """
        Метод класса для шифрования пароля пользователя для сохранения в БД
        :param password:
        :return:
        """
        return hashlib.sha224(str(str(password) + SALT).encode('utf-8')).hexdigest()

    @classmethod
    def get_user_by_session(cls, request) -> object:
        """
        Метод класса для получения объекта пользователя по сессионному ключу
        :param request:
        :return: User
        """
        token = request.COOKIES.get('fcsid')
        if token is None:
            return None
        user = User.objects.filter(auth_token=token).first()
        if user is None:
            return None
        if user is None or timezone.now().timestamp() > user.auth_expired.timestamp():
            return None
        return user
