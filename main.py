""" This module contains the code for drawing the lab one shape """
import cairo
import math

OUTPUT_DIR = "output/"
WIDTH, HEIGHT = 800, 600
BG_COLOR = (0.8, 0.8, 0.8)

# Set up the surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
ctx = cairo.Context(surface)
ctx.set_source_rgb(*BG_COLOR)
ctx.paint()


# Draw the shape
ctx.set_source_rgb(0, 0, 1)
ctx.set_line_width(1)
ctx.arc_negative(400, 280, 100, math.radians(0), math.radians(180))

# House outline
ctx.move_to(200, 280)
ctx.line_to(600, 280)
ctx.line_to(600, 330)
ctx.line_to(550, 330)
ctx.line_to(550, 500)
ctx.line_to(450, 500)
ctx.line_to(250, 500)
ctx.line_to(250, 330)
ctx.line_to(200, 330)
ctx.close_path()
ctx.stroke()

# Windows and doors
ctx.set_source_rgb(0, 0.5, 0)
ctx.set_line_width(2)

# Left window
ctx.rectangle(270, 360, 60, 60)
# Door
ctx.rectangle(360, 360, 80, 140)
# Right window
ctx.rectangle(470, 360, 60, 60)
ctx.stroke()

# Window lines
ctx.set_source_rgb(0, 0, 1)
ctx.set_line_width(1)

# Left window lines
ctx.move_to(300, 360)
ctx.line_to(300, 420)
ctx.move_to(270, 390)
ctx.line_to(330, 390)

# Right window lines
ctx.move_to(500, 360)
ctx.line_to(500, 420)
ctx.move_to(470, 390)
ctx.line_to(530, 390)

ctx.stroke()

# Door knob
ctx.arc(430, 430, 5, 0, math.radians(360))
ctx.set_source_rgb(0, 0.1, 0.8)
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 0.5)
ctx.set_line_width(3)
ctx.stroke()

# Crescent moon gradient
gradient = cairo.RadialGradient(600, 120, 50, 600, 120, 0)
gradient.add_color_stop_rgb(0, 1.0, 0.84, 0)
gradient.add_color_stop_rgb(0.5, 1.0, 0.76, 0.03)
gradient.add_color_stop_rgb(1, 0.85, 0.65, 0.13)
ctx.set_source(gradient)
ctx.arc(600, 120, 50, math.radians(0), math.radians(360))
ctx.fill_preserve()
ctx.set_source_rgb(0, 0, 1)
ctx.set_line_width(2)
ctx.stroke()

# Superimposing circle
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.arc(620, 100, 50, math.radians(0), math.radians(360))
ctx.fill()

# Arc to complete the crescent
ctx.arc(620, 100, 50, math.radians(60), math.radians(210))
ctx.set_source_rgb(0, 0, 1)
ctx.set_line_width(2)
ctx.stroke()

# Output
surface.write_to_png(f"{OUTPUT_DIR}lab_one_img.png")