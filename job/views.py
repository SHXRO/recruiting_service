from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Vacancy, Category
from .form import ResponseForm
import telegram
import asgiref.sync


class IndexView(View):
    def get(self, request):
        return render(request, 'job/index.html')


class Success(View):
    def get(self, request):
        return render(request, 'job/success.html')


class Fail(View):
    def get(self, request):
        return render(request, 'job/fail.html')


class VacancyView(View):
    def get(self, request):
        posts = Vacancy.objects.all()
        menu = Category.objects.all()
        return render(request, 'job/job.html', {'vacancy_list': posts, 'menu': menu})

    def post_category(request, url):
        posts = Vacancy.objects.filter(category__url=url)
        menu = Category.objects.all()
        return render(request, 'job/job.html', {'vacancy_list': posts, 'menu': menu})


class PostDetailView(View):
    def get(self, request, pk):
        post = Vacancy.objects.get(id=pk)
        return render(request, 'job/job_detail.html', {'post': post})


class JobApplication(View):

    def send_telegram_message(sel, message):
        bot = telegram.Bot(token='###')
        chat_id = '-###'
        asgiref.sync.async_to_sync(bot.send_message)(chat_id=chat_id, text=message)

    def post(self, request, pk):
        message = f"Новый тикет!"
        form = ResponseForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
            self.send_telegram_message(message)
            return redirect('success')

        else:
            return redirect('fail')
