from markdown import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.util import etree
import re


class ImagesTreeprocessor(Treeprocessor):
    def __init__(self, config, md):
        Treeprocessor.__init__(self, md)
        self.re = re.compile(r'^!.*')
        self.config = config

    def run(self, root):
        parent_map = {c: p for p in root.iter() for c in p}
        images = root.getiterator("img")
        for image in images:
            desc = image.attrib["alt"]
            if self.re.match(desc):
                desc = desc.lstrip("!")
                image.set("alt", desc)
                parent = parent_map[image]
                ix = list(parent).index(image)
                div_node = etree.Element('div')
                div_node.set("class", "lightgallery")
                new_node = etree.Element('a')
                new_node.set("href", image.attrib["src"])

                if self.config["show_description_in_lightgallery"]:
                    new_node.set("data-sub-html", desc)

                new_node.append(image)
                div_node.append(new_node)
                parent.insert(ix, div_node)
                parent.remove(image)

                if self.config["show_description_as_inline_caption"]:
                    inline_caption_node = etree.Element('p')
                    inline_caption_node.set("class", self.config["custom_inline_caption_css_class"])
                    inline_caption_node.text = desc
                    parent.insert(ix + 1, inline_caption_node)

class LightGalleryExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            'show_description_in_lightgallery' : [False, 'Adds the description as caption in lightgallery dialog. Default: False'],
            'show_description_as_inline_caption' : [False, 'Adds the description as inline caption below the image. Default: False'],
            'custom_inline_caption_css_class' : ['', 'Custom CSS classes which are applied to the inline caption paragraph. Multiple classes are separated via space. Default: empty']
        }
        super(LightGalleryExtension, self).__init__(**kwargs)


    def extendMarkdown(self, md, md_globals):
        config = self.getConfigs()
        md.treeprocessors.add("lightbox", ImagesTreeprocessor(config, md), "_end")


def makeExtension(*args, **kwargs):
    return LightGalleryExtension(**kwargs)
