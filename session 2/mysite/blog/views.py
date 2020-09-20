from django.views.generic import TemplateView, CreateView
from .models import BaiViet, BinhLuan
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.db.models import Q

# View đăng ký người dùng
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# View đăng ký người dùng thành công

class SignUpDoneView(TemplateView):
    template_name = 'registration/signup_done.html'
    title = 'Signup successful'


# View hiển thị trang chủ (index.html)
class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = dict()
        baiviets = BaiViet.objects.all()
        context['baiviets'] = baiviets
        return context


# View hiển thị bài viết cụ thể (post.html) theo khóa chính (pk) người dùng gửi từ request (index.html)
def noidung_baiviet(request, pk):
    baiviet = BaiViet.objects.get(pk=pk)
    binhluans = BinhLuan.objects.filter(post=baiviet)
    # print(binhluans)
    context = {
        'baiviet': baiviet,
        'id': pk,
        'binhluans': binhluans
    }
    return render(request, 'post.html', context)

# View gửi bình luận trong 1 bài viết cụ thể (post.html), người dùng gửi từ request bằng giao thức POST
def noidung_comment(request):
    if request.method == 'POST':
        # Lay thong tin tu request gui ve
        id = request.POST.get("id")
        tacgia = request.POST.get("tacgia")
        binhluan_moi = request.POST.get("noidung_binhluan")

        baiviet = BaiViet.objects.get(pk=id)
        binhluan = BinhLuan(post=baiviet, tacgia=tacgia, noidung=binhluan_moi, chapnhan=False)
        # Lưu bình luận vào db
        binhluan.save()
        binhluans = BinhLuan.objects.filter(post=baiviet)
        context = {
            'baiviet': baiviet,
            'id': id,
            'binhluans': binhluans,
            'binhluan_moi': binhluan_moi,
            'tacgia': tacgia,
        }
        return render(request, 'post.html', context)


# View tìm kiếm bài viết, người dùng gửi request bằng giao thức GET
def timkiem_baiviet(request):
    if request.method == 'GET':
        baiviet_kw = request.GET.get('search')
        baiviets = BaiViet.objects.filter(Q(tieude__contains=baiviet_kw) | Q(noidung__contains = baiviet_kw))
        context = dict()
        context['baiviets'] = baiviets
        context['ketquatimkiem'] = baiviets.count
        return render(request, "index.html", context)
    else:
        return render(request, "index.html", {})