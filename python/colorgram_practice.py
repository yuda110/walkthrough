import colorgram

colors = colorgram.extract('../images/bastion.png', 6)

first_color = colors[0]
proportion = first_color.proportion
for c in colors:
    rgb = c.rgb
    print(rgb[0], rgb[1])
