# blog/admin.py
from django.contrib import admin
from .models import Blog, BlogImage, Comment, Project, ProjectImage, ProjectComment

# Inline for BlogImage
class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 1  # Number of empty image upload fields to show
    fields = ('image', 'alt_text')  # Fields to display in the inline form
    readonly_fields = ('image_preview',)  # Optional: Add a preview if desired

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px;" />'
        return "No image"
    image_preview.allow_tags = True  # Allows HTML in the admin
    image_preview.short_description = 'Preview'

# Inline for Comment
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # No extra empty forms by default
    fields = ('author', 'text', 'created_at')  # Fields to display
    readonly_fields = ('created_at',)  # Make created_at read-only

# Custom Blog Admin
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'likes', 'total_comments', 'image_count')  # Columns in the list view
    list_filter = ('date',)  # Filter by date
    search_fields = ('title', 'description')  # Searchable fields
    inlines = [BlogImageInline, CommentInline]  # Show images and comments inline
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Metadata', {
            'fields': ('date', 'likes'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )

    # Custom method to display total number of images
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Total Images'

    # Use the total_comments method from the model
    def total_comments(self, obj):
        return obj.total_comments()
    total_comments.short_description = 'Total Comments'

# Register the models
admin.site.register(Blog, BlogAdmin)



# Inline for ProjectImage
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1  # Number of empty image upload fields to show
    fields = ('image', 'alt_text')  # Fields to display in the inline form
    readonly_fields = ('image_preview',)  # Optional: Add a preview if desired

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-height: 100px;" />'
        return "No image"
    image_preview.allow_tags = True  # Allows HTML in the admin
    image_preview.short_description = 'Preview'

# Inline for ProjectComment
class ProjectCommentInline(admin.TabularInline):
    model = ProjectComment
    extra = 0  # No extra empty forms by default
    fields = ('author', 'text', 'created_at', 'is_demo_request', 'demo_type')  # Fields to display
    readonly_fields = ('created_at', 'is_demo_request', 'demo_type')  # Make these read-only

# Custom Project Admin
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'likes', 'total_comments', 'image_count')  # Columns in the list view
    list_filter = ('date',)  # Filter by date
    search_fields = ('title', 'description')  # Searchable fields
    inlines = [ProjectImageInline, ProjectCommentInline]  # Show images and comments inline
    fieldsets = (
        (None, {
            'fields': ('title', 'description')
        }),
        ('Metadata', {
            'fields': ('date', 'likes'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )

    # Custom method to display total number of images
    def image_count(self, obj):
        return obj.images.count()
    image_count.short_description = 'Total Images'

    # Use the total_comments method from the model
    def total_comments(self, obj):
        return obj.total_comments()
    total_comments.short_description = 'Total Comments'

# Register the models
admin.site.register(Project, ProjectAdmin)