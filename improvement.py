# Documentation: https://shapely.readthedocs.io/en/stable/manual.html#polygons
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

# Documentation: https://geopy.readthedocs.io/en/stable/
from geopy import distance

# (x, y) tuples
CITIES = {
    "Sao Paulo": [(-23.533773, -46.835503), (-23.548881, -46.456222), (-23.619362, -46.813516), (-23.609295, -46.500196)],
    "Rio de Janeiro": [(-22.909385, -43.226416), (-22.918872, -43.226760), (-22.916342, -43.197901), (-22.910333, -43.197214)],
    "Fortaleza": [(-3.697078, -38.593382), (-3.733736, -38.477281), (-3.786494, -38.620886), (-3.812529, -38.508874)],
    "Distrito Federal": [(-15.527791, -48.205135), (-16.045813, -48.275706), (-16.040534, -47.319257), (-15.517205, -47.423697)],
    "Porto Alegre": [(-29.985271, -51.201407), (-30.122561, -51.257062), (-30.136814, -51.143003), (-29.990029, -51.111396)],
}
MAX_DISTANCE = 1000

def is_inside(point: Point, coordinates: list) -> bool:
    polygon = Polygon(coordinates) # create polygon
    # point.within(polygon) # check if a point is in the polygon 
    return polygon.contains(point) # check if polygon contains point OR check if a point is in the polygon 

def is_in_range(coordinate: tuple) -> bool:
    reference_point = (-15.799356, -47.912303)

    distance_to_center = distance.distance(coordinate, reference_point).meters

    return distance_to_center <= MAX_DISTANCE

def city_name(x: float, y: float) -> str:
    for city in CITIES:
        if is_inside(Point(x, y), CITIES[city]):
            return city
    return "Out of range"


if __name__ == "__main__":
    # Tests: https://www.latlong.net/
    assert city_name(-15.618408, -47.658203) == "Distrito Federal"
    assert city_name(-30.020949, -51.171174) == "Porto Alegre"
    assert city_name(-22.912547, -43.209686) == "Rio de Janeiro"
    assert city_name(-23.551045, -46.633376) == "Sao Paulo"
    assert city_name(-3.743671, -38.529144) == "Fortaleza"
    assert city_name(-10.141932, -48.189835) == "Out of range"
    assert is_in_range((-15.800306, -47.910028)) == True
    assert is_in_range((-15.800285, -47.914262)) == True
    assert is_in_range((-15.799439, -47.911878)) == True
    assert is_in_range((-15.794896, -47.882917)) == False
    assert is_in_range((-15.817690, -47.901125)) == False
    assert is_in_range((-15.798778, -47.848043)) == False
