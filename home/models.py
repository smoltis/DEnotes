from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailcore.models import Orderable, Page

from django.utils.encoding import python_2_unicode_compatible

from modelcluster.fields import ParentalKey

class CardsColumn(models.Model):
    icon = models.CharField(max_length=30)
    header = models.CharField(max_length=30)
    text = models.CharField(max_length=255)
    site_path = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    tooltip = models.CharField(max_length=255)
    panels = [
        FieldPanel('icon'),
        FieldPanel('header'),
        FieldPanel('text'),
        FieldPanel('site_path'),
        FieldPanel('label'),
        FieldPanel('tooltip'),
    ]
    class Meta:
        abstract = True

@python_2_unicode_compatible  # provide equivalent __unicode__ and __str__ methods on Python 2
class HomePage(Page):
    body = RichTextField(blank=True)

    headline = models.CharField(blank=True, max_length=250)

    intro1 = models.CharField(max_length=250, blank=True)
    intro2 = models.CharField(max_length=250, blank=True)
    intro3 = models.CharField(max_length=250, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('headline', classname="title"),
        FieldPanel('intro1', classname="title"),
        FieldPanel('intro2', classname="title"),
        FieldPanel('intro3', classname="title"),
        InlinePanel('related_cards', label='Related Cards'),
        FieldPanel('body', classname="full"),
    ]
class HomePageRelatedCards(Orderable, CardsColumn):
    page = ParentalKey(HomePage, related_name='related_cards')