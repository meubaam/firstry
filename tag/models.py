from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=32, verbose_name='태그명')
    registed_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fastcampus_tag'
        # 테이블 명 별도지정하는 법 - 기본 생성되는 앱과 구분하기 위해 씀
        verbose_name = '패스트캠퍼스 태그'
        verbose_name_plural = '패스트캠퍼스 태그'
