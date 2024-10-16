""" This module contains the code for drawing the lab one shape """
import cairo

OUTPUT_DIR = "output/"
WIDTH, HEIGHT = 600, 400
BG_COLOR = (0.8, 0.8, 0.8)

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_source_rgb(*BG_COLOR)
ctx.paint()

# Output
surface.write_to_png(f"{OUTPUT_DIR}lab_one_img.png")