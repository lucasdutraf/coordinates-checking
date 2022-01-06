import numpy as np

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from geopy import distance

def is_inside(x: float, y: float) -> bool:
    latitude = np.array([-15.527791, -16.045813, -16.040534, -15.517205]) # x
    longitude = np.array([-48.205135, -48.275706, -47.319257, -47.423697]) # y
    # Federal District coordinates
    squared_coord = [(-15.527791, -48.205135), (-16.045813, -48.275706), (-16.040534, -47.319257), (-15.517205, -47.423697)]

    polygon = Polygon(squared_coord) # create polygon
    point = Point(x, y) # create point
    return polygon.contains(point) # check if polygon contains point OR check if a point is in the polygon 

def is_in_range(coordinate: tuple) -> bool:
    max_distance = 1000
    reference_point = (-15.799356, -47.912303)

    distance_to_center = distance.distance(coordinate, reference_point).meters

    return distance_to_center <= max_distance


if __name__ == "__main__":
    # inside
    x_inside, y_inside = (-15.843226, -48.027127)
    inside_range = (-15.800647, -47.909934)
    # outside
    x_outside, y_outside = (-16.378121, -48.947742)
    outside_range = (-15.843226, -48.027127)
    

    print(f"Boundary results:", f"Inside test: {is_inside(x_inside, y_inside)}", f"Outside test: {is_inside(x_outside, y_outside)}", sep="\n")
    print("\n\n")
    print(f"Range results:", f"Inside test: {is_in_range(inside_range)}", f"Outside test: {is_in_range(outside_range)}", sep="\n")

    # Tests
    assert is_inside(-15.618408, -47.658203) == True  # Planaltina
    assert is_inside(-15.734101, -47.870532) == True  # Lago Norte 
    assert is_inside(-15.817360, -48.110467) == True  # Ceilândia
    assert is_inside(-16.299051, -47.944201) == False # Luziânia
    assert is_inside(-23.765237, -46.755133) == False # São Paulo
    assert is_inside(-13.025966, -38.531872) == False # Salvador
    assert is_in_range((-15.800306, -47.910028)) == True
    assert is_in_range((-15.800285, -47.914262)) == True
    assert is_in_range((-15.799439, -47.911878)) == True
    assert is_in_range((-15.794896, -47.882917)) == False
    assert is_in_range((-15.817690, -47.901125)) == False
    assert is_in_range((-15.798778, -47.848043)) == False