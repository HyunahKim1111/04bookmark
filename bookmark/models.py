from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL') # url필드는 링크가 자동으로 걸리게 된다. 입력받을 때 사용할 이름을 Site URL 설정한 것임

#인스턴스를 출력했을 때 만드는 내용
    def __str__(self):
        return "이름: "+self.site_name+", 주소 : "+self.url
    
    # from django.urls import reverse 추가!
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)]) # args=[(self.id)] 이렇게 들어가도 상관 없어
