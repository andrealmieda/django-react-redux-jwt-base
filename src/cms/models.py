from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

from cms.wagtail_models.page_streams import HomePageStream


class HomePage(Page):

    body = StreamField(HomePageStream)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body')
    ]

    template = 'pages/homepage.html'
