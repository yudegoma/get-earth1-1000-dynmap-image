#!/usr/bin/env python
import minecraft_dynmap_timemachine.dynmap as dynmap
import minecraft_dynmap_timemachine.time_machine as time_machine
import minecraft_dynmap_timemachine.projection as projection
import os
import datetime
import cv2
from dynmap_utils import crop, pil_to_cv2

img_dir = "./images"

base_url = "https://map-s5.minecraftserver.jp/"
world = "world_SW_3"
map_name = "flat"
center = [0, 0, 0]
size = [6, 4]
zoom = 6

dm = dynmap.DynMap(base_url)
maps = dm.worlds[world].maps
dm_map = maps[map_name]
m_loc = projection.MinecraftLocation(center[0], center[1], center[2], dm_map.worldtomap)
tm = time_machine.TimeMachine(dm)


def timerapse_dynmap():
    # 画像保存の設定
    now = datetime.datetime.now()
    imgs = img_dir + "/{0:%Y%m%d}".format(now)
    if not os.path.exists(imgs):
        os.mkdir(imgs)

    print("{0:%Y%m%d_%H%M}.png".format(now))
    dest = imgs + '/dyn_earth_{0:%Y%m%d_%H%M}.png'.format(now)

    img = tm.capture_single(dm_map, m_loc.to_tile_location(zoom), size)
    cv2.imwrite(dest, crop(pil_to_cv2(img)))

if __name__ == '__main__':
    if not os.path.exists(img_dir):
        os.mkdir(img_dir)
    timerapse_dynmap()