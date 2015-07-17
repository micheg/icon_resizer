# Mobile icon resizer

## prerequisites

*PIL*

Note for install PIL on osx:
ln -s /usr/local/include/freetype2 /usr/local/include/freetype
pip install PIL --allow-external PIL --allow-unverified PIL

## using:

python mobile_icon_resizer.py {source_file.png} {dest_dir}

## output:

        {dest_dir}
        ├── android
        │   ├── icon-hdpi.png
        │   ├── icon-ldpi.png
        │   ├── icon-mdpi.png
        │   ├── icon-xhdpi.png
        │   ├── icon-xxhdpi.png
        │   └── icon-xxxhdpi.png
        └── ios
            ├── icon-40.png
            ├── icon-40@2x.png
            ├── icon-40@3x.png
            ├── icon-57.png
            ├── icon-57@2x.png
            ├── icon-60.png
            ├── icon-60@2x.png
            ├── icon-60@3x.png
            ├── icon-72.png
            ├── icon-72@2x.png
            ├── icon-76.png
            ├── icon-76@2x.png
            ├── icon-small.png
            ├── icon-small@2x.png
            └── icon-small@3x.png