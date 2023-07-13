from PIL import Image
import numpy as np
def collage_marker(image1, image2, name):
    i1 = np.array(image1)
    i2 = np.arange(image2)
    collage = np.vstack([i1, i2])
    image = Image.fromarray(collage)
    image.save(name)

collage_marker("image1.jpg", "image2.ipg", "new.jpg")
