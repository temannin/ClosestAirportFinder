# Closest Airport Finder
![](https://img.shields.io/badge/dependencies-0-brightgreen.svg) ![GitHub](https://img.shields.io/github/license/temannin/ClosestAirportFinder.svg) ![](https://img.shields.io/badge/python-3.7-blue.svg)<br><br>

Given a list of airports, this program is able to find the closest airport to the location provided.

This script is primarily for the output of Scott's Cheaps Flights emails. SCF, by default sends **ALL** the FROM locations of a certain deal and it can be hard to decipher which airport is the closest to *you*. 

## Up and Running
1. Download this repository
2. Find your latitude and longitude
3. Change in finder.py to reflect these values here:

        LAT_ORIGIN = radians(39.103119) # YOUR LOCATION LATITUDE IN ( )
        LON_ORIGIN = radians(-84.512016) # YOUR LOCATION LONGITUDE IN ( )
4. Using the default latitude and longitude reading from list.txt

        list.txt
            Chicago (ORD) - $380
            Los Angeles (LAX) - $377
            Miami (MIA) - $363
            Orlando (MCO) - $467
            Philadelphia (PHL) - $357
            San Francisco (SFO) - $367
            Washington DC (IAD) - $363

        The output of python ./finder.py (distance in miles):

        {'name': "Chicago O'Hare International Airport", 'distance': 266.8845815350654}
        {'name': 'Washington Dulles International Airport', 'distance': 378.94208318180785}
        {'name': 'Philadelphia International Airport', 'distance': 497.1326007927064}
        {'name': 'Orlando International Airport', 'distance': 760.169505154458}
        {'name': 'Miami International Airport', 'distance': 951.9721985156232}
        {'name': 'Los Angeles International Airport', 'distance': 1904.7198994898595}
        {'name': 'San Francisco International Airport', 'distance': 2039.6227934846734}
