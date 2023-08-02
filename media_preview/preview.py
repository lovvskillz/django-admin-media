from os import path

import django.contrib.admin.utils
from django.conf import settings
from django.db import models
from django.utils.html import format_html

from media_preview.media_preview import constants

MEDIA_PREVIEW_WIDTH = getattr(settings, "MEDIA_PREVIEW_WIDTH", 320)


class AdminMediaPreview:
    def __init__(self, model, admin_site):
        django.contrib.admin.utils.display_for_field = self.preview_display_for_field
        super().__init__(model, admin_site)

    # hacky but it works for the moment :)
    def preview_display_for_field(self, value, field, empty_value_display):
        from django.contrib.admin.utils import display_for_field

        if isinstance(field, models.FileField) and value:
            file_extension = path.splitext(value.name)[1][1:].lower()
            preview_container = ""
            if (
                isinstance(field, models.ImageField)
                or file_extension in constants.IMAGE_EXTENSIONS
            ):
                preview_container = format_html(
                    "<img width='{}' src='{}' alt='{}'/>",
                    MEDIA_PREVIEW_WIDTH,
                    value.url,
                    value.name,
                )
            elif file_extension in constants.AUDIO_EXTENSIONS:
                preview_container = format_html(
                    "<audio controls>"
                    "<source src='{}' type='audio/{}'/>"
                    "Your browser does not support the audio tag."
                    "</audio>",
                    value.url,
                    file_extension,
                )
            elif file_extension in constants.VIDEO_EXTENSIONS:
                preview_container = format_html(
                    "<video width='{}' controls>"
                    "<source src='{}' type='video/{}'>"
                    "Your browser does not support the video tag."
                    "</video>",
                    MEDIA_PREVIEW_WIDTH,
                    value.url,
                    file_extension,
                )
            return format_html(
                '{}<a href="{}">{}</a>', preview_container, value.url, value
            )
        return display_for_field(value, field, empty_value_display)
