#!/usr/bin/env python
# -*- coding: utf-8 -*-

# calcultes the euclidean shortest distnace
# between two polygons or lines for that matter
# geom_a.distance(geom_b)
from shapely.geometry import Polygon, LineString, Point

from shapely.ops import snap

from matplotlib import pyplot
from descartes import PolygonPatch
from shapely.ops import polygonize
from shapely.geometry import Polygon, LineString, Point

from utils import SIZE, BLUE, RED, GREEN, GRAY, YELLOW
from utils import plot_coords_line
from utils import plot_line
from utils import set_plot_bounds

line = LineString([(0.5, 0.5), (2.0, 1.5), (3.0, 0.5)])
point = Point(3, 1.8)
pt_snap_res = snap(point, line, 4)
shplySnapPoint = line.interpolate(line.project(point))

print "point"
print point
print "pt_snap_res"
print pt_snap_res
print "shplySnapPoint"
print shplySnapPoint


# setup matplotlib figure that will display the results
fig = pyplot.figure(1, figsize=SIZE, dpi=90, facecolor="white")

# add a little more space around subplots
fig.subplots_adjust(hspace=.5)

# ###################################
# first plot
# display sample line and circle
# ###################################

# first figure upper left drawing
# 121 represents the number_rows, num_cols, subplot number
ax = fig.add_subplot(121)

# add line using our function above
plot_line(ax, line)

# draw the line nodes using our function
# plot_coords_line(ax, line)

plot_coords_line(ax, point, BLUE, 'x', 'original-pt')
plot_coords_line(ax, pt_snap_res, RED, 'o', 'snap-res')
plot_coords_line(ax, shplySnapPoint, GRAY, 'o', 'good-snap')


#plot_coords_line(ax, square.exterior)



# plot_coords_line(ax, pt_snap_res, GREEN)

# subplot title text
ax.set_title('Snap Point to Line')

# define axis ranges as list [x-min, x-max]
# added 1.5 units around object so not touching the sides
x_range = [square.bounds[0] - 1.0, square.bounds[2] + 1.5]

# y-range [y-min, y-max]
y_range = [square.bounds[1] - 1.0, square.bounds[3] + 1.0]

# set the x and y axis limits
ax.set_xlim(x_range)
ax.set_ylim(y_range)

# assing the aspect ratio
ax.set_aspect(1)

# ax.legend(loc='upper center', bbox_to_anchor=(1, 0.5),
#           ncol=2, fancybox=True, shadow=True)

ax.legend()

pyplot.show()
