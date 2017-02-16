from wagtail.wagtailcore import blocks


class BigTitleBlock(blocks.StructBlock):
    title = blocks.CharBlock(label='Title', required=False)
    description = blocks.CharBlock(label='Description', classname='full', required=False)

    class Meta:
        template = 'blocks/common_blocks/big_title_block.html'