from django.utils.html import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import gettext_lazy


def preview_image(image):
    if image:
        return mark_safe(
            f'<img src="{image.url}" width="32" style="position:absolute;margin-top:-8px"/>'
        )
    return mark_safe(
        '<img src="/static/avatar/noimage.jpg" width="32" style="border-radius:50%;position:absolute;margin-top:-8px">'
    )


# @TODO joriy yuklanayotgan rasmga nazar shuni tugirlashim kere
class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None, **kwargs):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)
            output.append(
                u' <a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"  style="object-fit: cover;"/></a> %s ' % \
                (image_url, image_url, file_name, gettext_lazy('')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))
