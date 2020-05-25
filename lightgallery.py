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
                if self.config["strip_leading_exclamation_mark"]:
                    desc = desc.lstrip("!")
            
                image.set("alt", desc)
                parent = parent_map[image]
                ix = list(parent).index(image)
                div_node = etree.Element('div')
                div_node.set("class", "lightgallery")
                new_node = etree.Element('a')
                new_node.set("href", image.attrib["src"])
                new_node.append(image)
                div_node.append(new_node)
                parent.insert(ix, div_node)
                parent.remove(image)


class LightGalleryExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            'strip_leading_exclamation_mark' : [False, 'Strip leading exclamation mark from description. Default: False']
        }
        super(LightGalleryExtension, self).__init__(**kwargs)


    def extendMarkdown(self, md, md_globals):
        config = self.getConfigs()
        md.treeprocessors.add("lightbox", ImagesTreeprocessor(config, md), "_end")


def makeExtension(*args, **kwargs):
    return LightGalleryExtension(**kwargs)
