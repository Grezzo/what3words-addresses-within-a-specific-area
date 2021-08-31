#!/usr/bin/env python3

# May not work in the Southern or Eastern hemisphere (tested only in Northern/Western)

import requests
import sys

url = 'https://mapapi.what3words.com/api/convert-to-3wa'

latitude, longitude = sys.argv[1].split(',')
size = int(sys.argv[2])

squares_to_move = 1
squares_moved = 0
direction = 0
for i in range(size ** 2):
    response = requests.get(url, params={'coordinates': f'{latitude},{longitude}'}).json()
    print(f'///{response["words"]}')
    # Get middle of box
    latitude = response['coordinates']['lat']
    longitude = response['coordinates']['lng']
    # Get size of box
    height = response['square']['northeast']['lat'] - response['square']['southwest']['lat']
    width = response['square']['northeast']['lng'] - response['square']['southwest']['lng']
    if direction == 0:
        latitude += height # Move North
    elif direction == 1:
        longitude += width # Move East
    elif direction == 2:
        latitude -= height # Move South
    elif direction == 3:
        longitude -= width # Move West
    squares_moved += 1
    if squares_moved == squares_to_move:
        squares_moved = 0
        squares_to_move += direction % 2 # Increase number of squares if just moved East or West
        direction = (direction + 1) % 4
