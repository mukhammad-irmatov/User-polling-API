from django.contrib import admin
from .models import Poll,Question,Answer,Choice

admin.site.site_header = "Администратор сайта опроса"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the Admin Area"

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Choice)
