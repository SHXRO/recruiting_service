from django.db.models import QuerySet
from django.contrib import admin
from .models import JobResponse
from .models import Category
from .models import Vacancy


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Vacancy)
class VacacyAdmin(admin.ModelAdmin):
    list_display = ('name', 'city','available')
    actions = ['hide_post', 'show_post']

    @admin.action(description="Скрыть вакансию")
    def hide_post(self, request, qs: QuerySet):
        count_updated = qs.update(available=Vacancy.N)
        self.message_user(
            request,
            f'Был обновлен статус у {count_updated} вакансий'
        )
    @admin.action(description="Показать вакансию")
    def show_post(self, request, qs: QuerySet):
        count_updated = qs.update(available=Vacancy.Y)
        self.message_user(
            request,
            f'Был обновлен статус у {count_updated} вакансий'
        )



@admin.register(JobResponse)
class ResponseAdmin(admin.ModelAdmin):
    list_display = ('get_id_display', 'name', 'post', 'status')
    list_editable = ['status']
    list_filter = ['post']
    search_fields = ['name']
    actions = ['set_new', 'set_progress', 'set_close']
    list_per_page = 20

    def get_id_display(self, obj):
        return 'A#{}'.format(obj.id)

    get_id_display.short_description = 'Отклик'

    @admin.action(description="Проставить статус 'Новый тикет'")
    def set_new(self, request, qs: QuerySet):
        count_updated = qs.update(status=JobResponse.N)
        self.message_user(
            request,
            f'Был обновлен статус у {count_updated} тикетов'
        )

    @admin.action(description="Проставить статус 'Тикет на рассмотрение'")
    def set_progress(self, request, qs: QuerySet):
        count_updated = qs.update(status=JobResponse.I)
        self.message_user(
            request,
            f'Был обновлен статус у {count_updated} тикетов'
        )

    @admin.action(description="Проставить статус 'Закрытый тикет'")
    def set_close(self, request, qs: QuerySet):
        count_updated = qs.update(status=JobResponse.C)
        self.message_user(
            request,
            f'Был обновлен статус у {count_updated} тикетов'
        )

