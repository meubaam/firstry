from django.db import models
import django.contrib.auth.models
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
class Fcuser(models.Model): # 장고에서 제공하는 models.Model을 상속받음
    objects = models.Manager()
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자 이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registed_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
# 별도 SQL문서 생성 없이 데이터가 알아서 저장되고 가져와진다

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'fastcampus_fcuser'
        # 테이블 명 별도지정하는 법 - 기본 생성되는 앱과 구분하기 위해 씀
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'