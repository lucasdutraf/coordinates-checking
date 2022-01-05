import numpy as np

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

from geopy import distance

def is_inside(y: np.array, x: np.array) -> bool:
    longitude = np.array([-15.527791, -16.045813, -16.040534, -15.517205])
    latitude = np.array([-48.205135, -48.275706, -47.319257, -47.423697])

    lon_lat_vec = np.column_stack((longitude, latitude))

    polygon = Polygon(lon_lat_vec) # create polygon
    point = Point(y,x) # create point
    return polygon.contains(point) or point.within(polygon) # check if polygon contains point OR check if a point is in the polygon 

def is_in_range(coordinate: tuple) -> bool:
    max_distance = 1000
    reference_point = (-15.799356, -47.912303)

    distance_to_center = distance.distance(coordinate, reference_point).meters

    return distance_to_center <= max_distance


if __name__ == "__main__":
    # Federal District coordinates
    squared_coord = np.array([[-15.527791, -48.205135], [-16.045813, -48.275706], [-16.040534, -47.319257], [-15.517205, -47.423697]])

    # inside
    y_inside, x_inside = (-15.843226, -48.027127)
    inside_range = (-15.800647, -47.909934)
    # outside
    y_outside, x_outside = (-16.378121, -48.947742)
    outside_range = (-15.843226, -48.027127)
    

    print(f"Boundary results:", f"Inside test: {is_inside(y_inside, x_inside)}", f"Outside test: {is_inside(y_outside, x_outside)}", sep="\n")
    print("\n\n")
    print(f"Range results:", f"Inside test: {is_in_range(inside_range)}", f"Outside test: {is_in_range(outside_range)}", sep="\n")