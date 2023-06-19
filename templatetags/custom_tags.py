from django import template
from PIL import Image

register = template.Library()

@register.simple_tag
def showImage(image):
    img = Image.open(image)
    return img.show()