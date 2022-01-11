
import geopy
import geopy.distance as distance

from shapely.geometry import Polygon
from shapely.geometry import Point


def create_polygon(base_distance: int, initial_coordinate: tuple) -> Polygon:
    #Assume each site is 100km 
    d = distance.distance(kilometers=base_distance)

    # Going clockwise, from lower-left to upper-left, upper-right...
    p1 = geopy.Point(initial_coordinate)
    p2 = d.destination(point=p1, bearing=0)
    p3 = d.destination(point=p2, bearing=90)
    p4 = d.destination(point=p3, bearing=180)

    points = [(p.latitude, p.longitude) for p in [p1,p2,p3,p4]]
    polygon = Polygon(points)
    return polygon

def is_inside(point: Point, polygon: Polygon) -> bool:
    # point.within(polygon) # check if a point is in the polygon 
    return polygon.contains(point) # check if polygon contains point OR check if a point is in the polygon 

if __name__ == "__main__":
    polygon = create_polygon(100, (-16.061650, -48.270701))
    inside_point = Point(-15.618408, -47.658203)
    outside_point = Point(-23.551045, -46.633376)

    assert is_inside(inside_point, polygon) == True
    assert is_inside(outside_point, polygon) == False
