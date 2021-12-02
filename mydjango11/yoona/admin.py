from django.contrib import admin
# Register your models here.
from yoona.models import pets



class PetsAdmin(admin.ModelAdmin):
    list_display = ('name','breed', 'size','birthday','neutraOX', 'weight','sleep_time','morning_time','dinner_time','character_of_pets'
)
    #
    # def make_published(self, request, queryset):
    #     updated_count = queryset.upate(status='p')
    #     self.message_user(request, '{}개 관심 리스트'.format(updated_count))
    # make_published.short_description = '관심 리스트에 추가'

admin.site.register(pets)