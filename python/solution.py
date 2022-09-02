#!/usr/bin/env python3

from typing import (
    List,
    Tuple,
    Union
)

from utils.eye_pattern import (
    EYE_PATTERN_1, 
    EYE_PATTERN_2, 
    EYE_PATTERN_3, 
    EYE_PATTERN_4
)

from utils.image import (
    ImageType,
    PackedImage,
    StrideImage,
)

from utils.function_tracer import FunctionTracer



def is_red_eye(image: Union[PackedImage, StrideImage], x: int, y: int, checked_pixels: List):
    status = [1, 1, 1, 1]
    patterns = [EYE_PATTERN_1, EYE_PATTERN_2, EYE_PATTERN_3, EYE_PATTERN_4]
    for index, pattern in enumerate(patterns):   
        break_flag = False
        for i in range(5):
            for j in range(5):
                if i == 0 and j == 0:
                        continue
                is_red = image.pixels[image.resolution.height*(y+i)+(x+j)].red >= 200
                is_white = pattern[i][j] == ' '
                if is_white:
                    continue
                if not is_red:
                    status[index] = 0
                    break_flag = True
            if break_flag:
                break

    #if true add them to checked_pixels 
    print(status)
    if 1 in status:
        result = True
        for i in range(5):
            for j in range(5):
                if i == 0 and j == 0:
                    continue
                checked_pixels.append(image.resolution.height*(y+i)+(x+j))
    else:
        result = False
    return [result, status]


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
                    if image.resolution.width - x-1 <= 5 or image.resolution.height - y-1 <= 5:
                        continue
                    #start checking
                    is_red, status = is_red_eye(image, x, y, checked_pixels)
                    #if checking true: correct
                    if is_red:
                        
                    #continue
                    #if checking false: add coordinates as checked
        break

    

    #TODO fill solution
    del ft
            