from django.db import models


# django 프로젝트의 순서를 정리하는 블로그
# photo -> 저희집 강아지 사진을 추가
# file -> 그날그날 저장한, 한글파일, txt 파일을 올림

class StudyPost(models.Model):
    # 글 제목
    title = models.CharField(max_length=100)

    # 글 내용
    content = models.TextField()

    # 첨부사진, 파일(if / else문으로 ) -> 필수 항목 X
    photo = models.ImageField(upload_to='yoona/images/%Y/%M/%d/', blank=True)
    file = models.FileField(blank=True)

    # 최초 등록 시간
    created_at = models.DateTimeField(auto_now_add=True)

    # 수정한 시간
    updated_at = models.DateTimeField(auto_now=True)

    # 학습일기 올렸니 ?
    studynote = models.BooleanField(verbose_name='학습일기 썼습니까?')

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/yoona/{self.pk}/'
