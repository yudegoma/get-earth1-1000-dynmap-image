#!/usr/bin/env python
import cv2
import numpy as np


def pil_to_cv2(pil_img):
    cv2im = np.asarray(pil_img)
    return cv2.cvtColor(cv2im, cv2.COLOR_BGR2RGB)


# 画像の切り取り
def crop(img: np.ndarray) -> np.ndarray:
    crop_img = img[50:722, 96:1440]
    return crop_img