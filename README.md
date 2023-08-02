Display a preview of media files in the Django admin

## Installation

Add to your installed apps:
```python
# settings.py
INSTALLED_APPS = [
    # ...
    "media_preview",
]
```

Use the class `AdminMediaPreview` in the AdminModels that should have a preview:

```python
from django.contrib import admin
from media_preview.preview import AdminMediaPreview


@admin.register(SomeMediaModel)
class SomeMediaModelAdmin(AdminMediaPreview, admin.ModelAdmin):
    ...
```

## Configuration
```python
# settings.py
MEDIA_PREVIEW_WIDTH = 320 # default width is 320px
```
