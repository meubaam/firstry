from django.db import models
import django.contrib.auth.models
# Create your models here.
class Board(models.Model): # 장고에서 제공하는 models.Model을 상속받음
    objects = models.Manager()
    title = models.CharField(max_length=128, verbose_name='제목')
    contents = models.TextField(verbose_name='내용')
    writer = models.ForeignKey('fcuser.Fcuser', on_delete=models.CASCADE, verbose_name='작성자') 
    #On delete = CASCADE 뜻은 id삭제시 해당 id가 작성한 글도 같이 삭제된다는 뜻. 이외 값으로 SETTINGS_NULL이 있음
    # ForeignKey - 1 대 m(many) 관계를 표시하는 법 (한명의 작성자가 여러 글 작성)
    # 태그의 경우 - m(many) 대 m 한 글에 여러개가 들어갈 수 있고 여러 글에 중복 사용이 가능
    registed_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
# 별도 SQL문서 생성 없이 데이터가 알아서 저장되고 가져와진다
    tags = models.ManyToManyField('tag.Tag', verbose_name='태그')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        # 테이블 명 별도지정하는 법 - 기본 생성되는 앱과 구분하기 위해 씀
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = '패스트캠퍼스 게시글'
