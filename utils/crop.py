from PIL import Image


def crop_image(image, size):
    img = Image.open(image.path)
    h, w = img.height, img.width
    if h < w:
        img = img.crop(((w - h) / 2, 0, (w - h) / 2 + h, h))
    elif h > w:
        img = img.crop((0, (h - w) / 2, w, (h - w) / 2 + w))

    if w > size:
        img = img.resize((size, size))

    img.save(image)



