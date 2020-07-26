'''
    - $ conda activate py36t21 (tensorflow2.1 가상환경 실행)
'''

from PIL import Image

img = Image.new('RGB', [500,500], 255)
data = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        data[x,y] = (
            x % 255,
            y % 255,
            (x**2-y**2) % 255,
        )

img.save('./img_dn/image.png')
img.show('./img_dn/image.png')

