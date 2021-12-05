from django.db import models


# app에서 사용할 모델 만들기 (1) django 프로젝트 정리 블로그

class StudyPost(models.Model):
    # 글 제목
    title = models.Charfieid(max_lenght=100)
    # 글 내용
    content = models.textfieild()

    # 첨부 사진, 파일 (if /else문으로 구현) - > 필수 항목X
    photo = models.ImageField(blank=True, NULL=True)
    file = models.FileField(blank=True, NULL=True)

    # 최초 등록 시간
    created_at = models.DateTimeField(auto_now_add=True)

    # 수정 시간
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'
