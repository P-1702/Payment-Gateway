from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display=('name','instagram','amount',"paid")

    def user_info(self,obj):
        return obj.description
    
admin.site.register(Payment,PaymentAdmin)
