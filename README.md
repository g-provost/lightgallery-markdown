# Lightgallery markdown Extension

Markdown extension to wrap images in a lightbox.

Will only wrap images by adding **"!"** right after the opening **"["** bracket of the image.

```
![!Description](/img/pic1.png)
```

This will Output :

```html
<p>
  <div class="lightgallery">
    <a href="../img/pic1.png" data-sub-html="Description">
      <img alt="Description" src="../img/pic1.png" />
    </a>
  </div>
</p>
```

The extension is made to work with [lightgallery.js](https://github.com/sachinchoolur/lightgallery.js) a full featured JavaScript lightgallery/lightbox with no dependencies.

*Extension inspired by : [mardown-lightbox](https://github.com/AliciaSchep/markdown-lightbox)*

**To test the extension:**

```python
import markdown
from lightgallery import LightGalleryExtension

print(markdown.markdown('![!description](/img/pic1.png)', extensions=[LightGalleryExtension()]))
```


## Install

```bash
$ pip install lightgallery
```

## How to make it works with Mkdocs

**1.** Create a **theme** folder will the following structure in your Mkdocs folder

```
theme/
|_ css/
|_ fonts/
|_ img/
|_ js/
````

**2.** Go to [lightgallery.js GitHub](https://github.com/sachinchoolur/lightgallery.js) or [JSDELIVR](https://www.jsdelivr.com/package/npm/lightgallery.js) to download the following files to the **theme** sub-folders as listed below

- dist/js/lightgallery.min.js **->** theme/js/
- dist/css/lightgallery.min.css **->** theme/css/
- dist/fonts/lg.* **->** theme/fonts/
- dist/img/loading.gif **->** theme/img/

**3.** Create a **theme/main.hml** file and add the following code to the file

```html
{% extends "base.html" %}

{% block styles %}
    {{ super() }}
    <link rel="stylesheet" href="{{ base_url }}/css/lightgallery.min.css">
{% endblock styles %}

{% block libs %}
    {{ super() }}
    <script src="{{ base_url }}/js/lightgallery.min.js"></script>
{% endblock libs %}

{% block scripts %}
    {{ super() }}
    <script>
    var elements = document.getElementsByClassName("lightgallery");
    for(var i=0; i<elements.length; i++) {
       lightGallery(elements[i]);
    }
    </script>
{% endblock scripts %}
```

**4.** Modify the **mkdocs.yml** file to add the following settings

```
# Documentation and theme
theme:
  custom_dir: 'theme'
```


```
# Extensions
markdown_extensions:
  - lightgallery
```

**5.** Change extension settings in **mkdocs.yml**

All settings of the extension are optional and can be omitted.

```
# Extensions
markdown_extensions:
  - lightgallery:
      show_description_in_lightgallery: true | false
      show_description_as_inline_caption: true | false
      custom_inline_caption_css_class: 'my-caption-class'
```

| Setting | Description | Default Value |
|-|-|-|
| `show_description_in_lightgallery` | Adds the description as caption in lightgallery dialog. | `true` |
| `show_description_as_inline_caption` | Adds the description as inline caption below the image. | `false` |
| `custom_inline_caption_css_class` | Custom CSS classes which are applied to the inline caption paragraph. Multiple classes are separated via space. | Empty |


## License

MIT License
