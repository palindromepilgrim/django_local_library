from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'status', 'borrower', 'due_back', 'id']
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Basic Information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
class GenreAdmin(admin.ModelAdmin):
    pass
class LanguageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Language, LanguageAdmin)