from PIL import ImageGrab


RGB_TOLERANCE = 0.05
PIXEL_CHECK_DENSITY = 0.5
checkZones = {
    'left': (700,400,800,500),
    'up':   (0,0,10,10),
    'right':(0,0,10,10)
}


def main():
    rgb_to_check = (0,0,0)
    while True:
        for z in checkZones:
            if (check_for_pixels(checkZones[z], rgb_to_check, tolerance=0.1)):
                print("found!")


def check_for_pixels(check_box, check_rgb, check_density=PIXEL_CHECK_DENSITY, tolerance=RGB_TOLERANCE):
    pixel_data = _screengrab()
    for i in range(check_box[0], check_box[2], int(1//check_density)): # cols - x1 -> x2
        for j in range(check_box[1], check_box[3], int(1//check_density)): # rows - y1 -> y2
            if _pixel_rgb_match(pixel_data[i,j], check_rgb, tolerance):
                return True
    else:
        return False


def _pixel_rgb_match(pixel_rgb, target_rgb, tolerance):
    max_distance = (255**2 + 255**2 + 255**2)**0.5
    euclidean_dist = \
        ((pixel_rgb[0]-target_rgb[0])**2 + \
        (pixel_rgb[0]-target_rgb[0])**2 + \
        (pixel_rgb[0]-target_rgb[0])**2)**0.5
    return euclidean_dist/max_distance <= tolerance


def _screengrab(box=None):
    im = ImageGrab.grab(bbox=box)
    return im.load()


if __name__=='__main__':
    main()