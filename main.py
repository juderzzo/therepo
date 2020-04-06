from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
polygons = []
top = new_matrix()
ident(top)
cstack = [top]
print cstack
transform = new_matrix()

parse_file( 'script2', edges, polygons, transform, cstack, screen, color )
