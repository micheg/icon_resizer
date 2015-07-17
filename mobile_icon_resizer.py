#!/usr/bin/env python

# mobile incon resizer, use a 1024x1024 source image
# based on https://github.com/dexman/ios-icon-generator

# NEED A VIRTUALENV WITH PIL
# Note for install pil on osx:
# ln -s /usr/local/include/freetype2 /usr/local/include/freetype
# pip install PIL --allow-external PIL --allow-unverified PIL

import os
import os.path
from PIL import Image
import sys

ICONS = {
    'iphone': {
        'Settings': (29, [1, 2, 3]),
        'Spotlight': (40, [2, 3]),
        'App-5-6': (57, [1, 2]),
        'App-7-8': (60, [2, 3]),
    },
    'ipad': {
        'Settings': (29, [1, 2]),
        'Spotlight-5-6': (60, [1, 2]),
        'Spotlight-7-8': (40, [1, 2]),
        'App-5-6': (72, [1, 2]),
        'App-7-8': (76, [1, 2]),
    },
    'android': {
        'ldpi': (36, [1]),
        'mdpi': (48, [1]),
        'hdpi': (72, [1]),
        'xhdpi': (96, [1]),
        'xxhdpi': (144, [1]),
        'xxxhdpi': (192, [1]),
    }
}


class MobileIconResizer:

    def _image_name(self, image_type, device_name, scale, size):
        if device_name == 'iphone' or device_name == 'ipad':
            scale_string = '' if scale == 1 else "@%dx" % (scale)
            if size == 29:
                size_string = 'small'
            else:
                size_string = str(size)
            return 'icon-%s%s.png' % (size_string, scale_string)
        elif device_name == 'android':
            return 'icon-%s.png' % (image_type)
        else:
            raise ValueError('Unknow device')

    def __init__(self):
        def iter_icons():
            for device_name, device_icons in ICONS.items():
                for image_type, image_specs in device_icons.items():
                    size = image_specs[0]
                    scales = image_specs[1]
                    for scale in scales:
                        yield image_type, device_name, size, scale
        if len(sys.argv) != 3:
            print("Usage: %s <input image> <destination directory>" %
                  (sys.argv[0]))
            exit(1)

        src_file_path = sys.argv[1]
        dst_path = sys.argv[2]
        dst_path_ios = dst_path + '/ios'
        dst_path_android = dst_path + '/android'

        if not os.path.isdir(dst_path):
            os.makedirs(dst_path)

        if not os.path.isdir(dst_path_ios):
            os.makedirs(dst_path_ios)

        if not os.path.isdir(dst_path_android):
            os.makedirs(dst_path_android)

        im = Image.open(src_file_path)
        for image_type, device_name, size, scale in iter_icons():
            new_size = size * scale
            im_resized = im.resize((new_size, new_size), Image.ANTIALIAS)

            dst_name = self._image_name(image_type, device_name, scale, size)
            if device_name == 'iphone' or device_name == 'ipad':
                dst_file_path = os.path.join(dst_path_ios, dst_name)
            elif device_name == 'android':
                dst_file_path = os.path.join(dst_path_android, dst_name)
            else:
                dst_file_path = os.path.join(dst_path, dst_name)

            im_resized.save(dst_file_path)

tmp = MobileIconResizer()
