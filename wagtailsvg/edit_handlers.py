from wagtail.admin.panels import FieldPanel
from wagtailsvg.widgets import AdminSvgChooser

class SvgChooserPanel(FieldPanel):
    def __init__(self, field_name, disable_comments=None, permission=None, **kwargs):
        kwargs.pop("widget", None)
        super().__init__(field_name, widget=AdminSvgChooser(), **kwargs)
        self.disable_comments = disable_comments
        self.permission = permission