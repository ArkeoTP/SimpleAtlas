import numpy as np
from PIL import Image
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
    prog="simpleatlas",
    description=
    "Create a 2x2 Atlas from up to 4 input textures.\n" + \
    "If textures are named 1.png, 2.png, 3.png, 4.png\n" + \
    "This can be run without any arguments." + \
    ""
    )
    parser.add_argument("-tl", "--top_left"    , default="1.png", help="Top Left Texture, 1.png by default")
    parser.add_argument("-tr", "--top_right"   , default="2.png", help="Top Right Texture, 2.png by default")
    parser.add_argument("-bl", "--bottom_left" , default="3.png", help="Bottom Left Texture, 3.png by default")
    parser.add_argument("-br", "--bottom_right", default="4.png", help="Bottom Left Texture, 4.png by default")
    parser.add_argument("-o", "--output", default="out.png", help="output file name, out.png by default")
    args = parser.parse_args()


    inputs = [args.top_left, args.top_right, args.bottom_left, args.bottom_right]
    outputs = [None, None, None, None]
    
    for i in range(len(inputs)):
        try:
            outputs[i] = np.asarray(Image.open(inputs[i]))
        except:
            pass

    if (all(img is None for img in outputs)):
        sys.exit("At least one image needs to be supplied.\nType \"simpleatlas --help\" for help.")

    # Convert 
    max_layers = max([elem[-1] for elem in (image.shape for image in (image for image in outputs if image is not None))])
    for idx in range(len(outputs)):
        image = outputs[idx]
        if image is None:
            continue
        layer = image.shape
        if (layer[-1] < max_layers):
            shape = [c for c in layer]
            shape[-1] = 1
            opaque = np.full(shape, 255, dtype=np.uint8)
            outputs[idx] = np.concatenate([image, opaque], axis=-1)
    
    res = None
    size = [image.shape for image in outputs if image is not None]
    for s in size:
        if s is not None:
            res = s
    for idx, s in enumerate(size):
        if s is None:
            size[idx] = res
    if (not all(s == res for s in size)):
        sys.exit("Images must match in size")

    for idx, elem in enumerate(outputs):
        if elem is None:
            outputs[idx] = np.full(res, 0, dtype=np.uint8)

    top = np.hstack([outputs[0], outputs[1]])
    bottom = np.hstack([outputs[2], outputs[3]])
    target = np.vstack([top, bottom])

    im  = Image.fromarray(target)

    im.save(f"{args.output}")
    print(f"Exported {args.output}")

if __name__ == "__main__":
    main()