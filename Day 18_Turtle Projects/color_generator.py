import colorgram


# used only to generate a list of color tuples during development
# not used at every run since it takes time for colors to be generated
class ColorGenerator:
    def __init__(self):
        self.color_list = self.generate_colors()

    def generate_colors(self):
        colors = colorgram.extract("hirst_img.jpg", 30)
        colors_rgb = []
        for color in colors:
            r = color.rgb[0]
            g = color.rgb[1]
            b = color.rgb[2]
            new_color = (r, g, b)
            colors_rgb.append(new_color)
        return colors_rgb
