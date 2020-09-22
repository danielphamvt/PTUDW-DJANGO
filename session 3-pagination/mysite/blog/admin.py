from django.contrib import admin
from .models import BaiViet, BinhLuan


class BaiVierAdmin(admin.ModelAdmin):
    list_display = ('tieude', 'id', 'ngay_dang')

    class Meta:
        model = BaiViet


admin.site.register(BaiViet, BaiVierAdmin)


class BinhLuanAdmin(admin.ModelAdmin):
    list_display = ('noidung', 'id', 'tacgia', 'ngay_dang', 'chapnhan')

    class Meta:
        model = BinhLuan


admin.site.register(BinhLuan, BinhLuanAdmin)
