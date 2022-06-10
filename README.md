# SimpleAtlas
Command line tool for creating a simple texture atlas for VRChat

## Installation

```
python -m pip install git+https://github.com/ArkeoTP/SimpleAtlas.git
```

## Usage

```
simpleatlas [-h] [-tl TOP_LEFT] [-tr TOP_RIGHT] [-bl BOTTOM_LEFT] [-br BOTTOM_RIGHT] [-o OUTPUT]

Create a 2x2 Atlas from up to 4 input textures. If textures are named 1.png, 2.png, 3.png, 4.png This can be run   
without any arguments.

optional arguments:
  -h, --help            show this help message and exit
  -tl TOP_LEFT, --top_left TOP_LEFT
                        Top Left Texture, 1.png by default
  -tr TOP_RIGHT, --top_right TOP_RIGHT
                        Top Right Texture, 2.png by default
  -bl BOTTOM_LEFT, --bottom_left BOTTOM_LEFT
                        Bottom Left Texture, 3.png by default
  -br BOTTOM_RIGHT, --bottom_right BOTTOM_RIGHT
                        Bottom Left Texture, 4.png by default
  -o OUTPUT, --output OUTPUT
                        output file name, out.png by default
```

Images must be of same dimensions and have the same number of channels.

