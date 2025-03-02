from django.contrib import admin
from .models import Teacher

# Register your models here.
from .models import TeacherProfile

class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "is_approved")  # Show approval status in admin panel
    list_filter = ("is_approved",)
    actions = ["approve_teachers"]

    def approve_teachers(self, request, queryset):
        queryset.update(is_approved=True)
    approve_teachers.short_description = "Approve selected teachers"

admin.site.register(TeacherProfile, TeacherProfileAdmin)
