from django.db import models
from django.utils import timezone


class BaiViet(models.Model):
    tieude = models.CharField(max_length=300)
    noidung = models.TextField()
    ngay_dang = models.DateTimeField(default=timezone.now)
    anhbia = models.ImageField(upload_to ="blog")


class BinhLuan(models.Model):
    post = models.ForeignKey('BaiViet', on_delete=models.CASCADE)
    tacgia = models.CharField(max_length=200)
    noidung = models.CharField(max_length=3000)
    ngay_dang = models.DateTimeField(default=timezone.now)
    chapnhan = models.BooleanField(default=False)

