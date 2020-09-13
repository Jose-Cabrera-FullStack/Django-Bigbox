"""Bigbox model."""

# Django
from django.contrib import admin

# Models
from bigbox.models import Activity, Category, Box, Reason

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Activity admin."""
    fields = ['name', 
    'internal_name',
    'description',
    'category',
    'reasons',
    'purchase_available',
    ]

    list_display = (
        'id',
        'name', 
        'internal_name', 
        'description',
        'get_name',
        'activities_name',
        'purchase_available')

    def get_name(self, obj):
        return obj.category

    def activities_name(self,obj): 
        return ', '.join([a.name for a in obj.reasons.all()]) 
 
@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    """Box admin."""
 
    list_display = ('id',
        'name', 
        'internal_name', 
        'description',
        'get_name',
        'price',
        'activities_name',
        'purchase_available',
        'slug'
        )
    def activities_name(self,obj): 
        return ', '.join([a.name for a in obj.activities.all()]) 

    def get_name(self, obj):
        return obj.category.name


    fields = ['name', 
        'internal_name',
        'description',
        'activities',
        'category',
        'price',
        'purchase_available',
        'slug'
        ]

    
        

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin."""
    list_display = (
        'id',
        'name', 
        'slug',
        'order',
        'description'
        )

    fields = [
        'name', 
        'slug',
        'order',
        'description'
        ]

@admin.register(Reason)
class ReasonAdmin(admin.ModelAdmin):
    """Reason admin."""
    list_display = (
        'id',
        'name', 
        'slug',
        'order',
        )

    fields = [
        'name', 
        'slug',
        'order',
        ]
