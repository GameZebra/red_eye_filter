#!/usr/bin/env python3

from typing import (
    List,
    Tuple,
    Union
)
from utils.eye_pattern import EYE_PATTERN_1

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

from utils.function_tracer import FunctionTracer

import utils.eye_pattern 

def is_eye(image: Union[PackedImage, StrideImage], x: int, y: int, checked_pixels: List):
    result = True
    for i in range(5):
        for j in range(5):
            if i == 0 and j == 0:
                    continue    
        is_red = image.pixels[image.resolution.height*(y+i)+(x+j)].red >= 200
        is_non_white = EYE_PATTERN_1[i][j] != ' '
    
    #if true add them to checked_pixels 
    if result == True:
        for i in range(5):
            for j in range(5):
                if i == 0 and j == 0:
                    continue
                checked_pixels.append(image.resolution.height*(y+i)+(x+j))
    return result


def compute_solution(images: List[Union[PackedImage, StrideImage]]):
    ft = FunctionTracer("compute_solution", "seconds")

    for image in images:
        checked_pixels = []
        for y in range(image.resolution.height):
            for x in range(image.resolution.width):
                if image.resolution.height*y+x in checked_pixels:
                    continue
                else:
                    checked_pixels.append(image.resolution.height*y+x)
                if image.pixels[image.resolution.height*y+x].red >= 200:
                    if image.resolution.width - x < 5 or image.resolution.height - y < 5:
                        continue
                    #start checking
                    #if checking true: correct
                    #continue
                    #if checking false: add coordinates as checked
                    pass
        is_eye(image, x, y, checked_pixels)
        break

    

    #TODO fill solution
    del ft
            