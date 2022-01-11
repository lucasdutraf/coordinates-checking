# Documentation: https://shapely.readthedocs.io/en/stable/manual.html#polygons
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# Documentation: https://geopy.readthedocs.io/en/stable/
from geopy import distance

# Constants
# (x, y) tuples
CITIES = {
    "Sao Paulo": [(-23.564931, -46.654846), (-23.540383, -46.655533), (-23.538652, -46.620008), (-23.563515, -46.617088)],
    "Rio de Janeiro": [(-22.944799, -43.276982), (-22.879655, -43.284196), (-22.879655, -43.186650), (-22.927725, -43.176687)],
    "Fortaleza": [(-3.773819, -38.571732), (-3.693652, -38.583528),(-3.686799, -38.472904), (-3.766282, -38.457101) ],
    "Distrito Federal": [(-16.061650, -48.270701), (-15.511912, -48.204739), (-15.506619, -47.435127), (-16.061650, -47.325190)],
}
MAX_DISTANCE = 1000
REFERENCE_POINT = (-15.799356, -47.912303)


def is_inside(point: Point, coordinates: list) -> bool:
    polygon = Polygon(coordinates) # create polygon
    # point.within(polygon) # check if a point is in the polygon 
    return polygon.contains(point) # check if polygon contains point OR check if a point is in the polygon 

def is_in_range(coordinate: tuple) -> bool:
    distance_to_center = distance.distance(coordinate, REFERENCE_POINT).meters
    return distance_to_center <= MAX_DISTANCE

def city_name(x: float, y: float) -> str:
    for city in CITIES:
        if is_inside(Point(x, y), CITIES[city]):
            return city
    return "Out of range"


if __name__ == "__main__":
    # Tests: https://www.latlong.net/
    assert city_name(-23.551045, -46.633376) == "Sao Paulo"
    assert city_name(-22.912547, -43.209686) == "Rio de Janeiro"
    assert city_name(-3.743671, -38.529144) == "Fortaleza"
    assert city_name(-15.618408, -47.658203) == "Distrito Federal"
    assert city_name(-10.141932, -48.189835) == "Out of range"
    assert is_in_range((-15.800306, -47.910028)) == True
    assert is_in_range((-15.800285, -47.914262)) == True
    assert is_in_range((-15.799439, -47.911878)) == True
    assert is_in_range((-15.794896, -47.882917)) == False
    assert is_in_range((-15.817690, -47.901125)) == False
    assert is_in_range((-15.798778, -47.848043)) == False
