#!/bin/bash

echo "updating osu...";

echo "Changing directory...";


mkdir ~/Games ~/Games/osuLazer

cd ~/Games/osuLazer/;

echo "Downloading...";

rm osu.AppImage

wget -c ls--compression=auto https://github.com/ppy/osu/releases/latest/download/osu.AppImage;

chmod +x osu.AppImage
