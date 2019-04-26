from django.contrib import admin


from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'create_time')
    list_filter = ('sex', 'status', 'create_time')
    search_fields = ('name', 'profession')

    fieldsets = (
        (None, {
            'fields': {
                'name',
                ('sex','profession'),
                ('email', 'qq', 'phone'),
                'status',
            }
        })
    )


admin.site.register(Student, StudentAdmin)




