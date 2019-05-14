import json
import re
import

from math import sin, cos, sqrt, atan2, radians

def main():

    LAT_ORIGIN = radians(39.103119)  # YOUR LOCATION LATITUDE IN ( )
    LON_ORIGIN = radians(-84.512016)  # YOUR LOCATION LONGITUDE IN ( )

    radius_of_earth = 6378.0

    results = []

    with open("list.txt") as airports:
        with open('airports.json') as json_file:
            data = json.load(json_file)
            for line in airports:
                if line.strip():
                    regex = r"\((.*)\)"
                    matches = re.search(regex, line)
                    if matches:
                        DEST = "K" + matches.group(1)

                        for airport in data:
                            if DEST == airport:
                                lat2 = radians(data[airport]["lat"])
                                lon2 = radians(data[airport]["lon"])

                                dlon = lon2 - LON_ORIGIN
                                dlat = lat2 - LAT_ORIGIN

                                a = sin(dlat / 2)**2 + cos(LAT_ORIGIN) * \
                                    cos(lat2) * sin(dlon / 2)**2
                                c = 2 * atan2(sqrt(a), sqrt(1 - a))

                                
                                if (len(sys.argv) > 1):
                                    if (sys.argv[1] == "-km"):
                                        distance = radius_of_earth * c
                                    else:
                                        distance = radius_of_earth * c * .621371
                                else:
                                    distance = radius_of_earth * c * .621371
                                 

                                result = {
                                    "name": data[airport]["name"],
                                    "distance": distance
                                }

                                results.append(result)

        results = sorted(results, key=lambda k: k['distance'])

    for result in results:
        print(result)


if __name__ == "__main__":
    main()
