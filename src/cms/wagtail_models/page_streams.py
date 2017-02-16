from wagtail.wagtailcore import blocks

from cms.wagtail_models.common_blocks import BigTitleBlock


class HomePageStream(blocks.StreamBlock):
    title = BigTitleBlock(label='title')