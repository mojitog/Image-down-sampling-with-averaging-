from PIL import Image


def get_inputs():
    pass


def down_sampling(img, first_pixel, size):
    size_x, size_y = img.size
    count = 0
    accumulative_rgb = [0, 0, 0]
    avg_rgb = [0, 0, 0]
    for i in range(size):
        for j in range(size):
            if (first_pixel[0]+i < size_x) and (first_pixel[0]+j < size_y):
                pixel = (first_pixel[0]+i, first_pixel[1]+j)
                pixel_rgb = img.getpixel(pixel)
                count += 1
                for k in range(len(accumulative_rgb)):
                    accumulative_rgb[k] += pixel_rgb[k]
    for i in range(len(accumulative_rgb)):
        avg_rgb[i] = int(round(accumulative_rgb[i]/count, 0))
    return avg_rgb[0], avg_rgb[1], avg_rgb[2]


def image_grid(img, sample_size):
    img_grid = []
    size_x, size_y = img.size
    for x in range(0, size_x, sample_size):
        column = []
        for y in range(0, size_y, sample_size):
            column.append((x, y))
        img_grid.append(column)      
    return img_grid

sample_size = 10
img = Image.open("Heath_Ledger_as_the_Joker.JPG.webp")


#print(down_sampling(img, (0,0), 10))
print(image_grid(img, 500))