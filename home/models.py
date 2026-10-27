from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    pass

class AccueilPage(Page):
    pass

class ContactPage(Page):
    pass

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from django.db import models


class ContactPage(Page):
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    # Address Fields
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name="Address Line 1")
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name="Address Line 2")
    city = models.CharField(max_length=100, blank=True, verbose_name="City")
    postal_code = models.CharField(max_length=20, blank=True, verbose_name="Postal Code")
    country = models.CharField(max_length=100, blank=True, verbose_name="Country")

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("email"),
            FieldPanel("phone"),
        ], heading="Contact Information"),
        
        MultiFieldPanel([
            FieldPanel("address_line_1"),
            FieldPanel("address_line_2"),
            FieldPanel("city"),
            FieldPanel("postal_code"),
            FieldPanel("country"),
        ], heading="Address Details"),
    ]