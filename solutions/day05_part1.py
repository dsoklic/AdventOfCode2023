from solutions.utils import readFile, extractAllNumbers
from enum import Enum
import sys

Parsing = Enum('Parsing', ['NONE', 'SEED_TO_SOIL', 'SOIL_TO_FERTILIZER', 'FERTILIZER_TO_WATER', 'WATER_TO_LIGHT', 'LIGHT_TO_TEMPERATURE', 'TEMPERATURE_TO_HUMIDITY', 'HUMIDITY_TO_LOCATION'])
seeds = []
seed2soil = []
soil2fertilizer = []
fertilizer2water = []
water2light = []
light2temperature = []
temperature2humidity = []
humidity2location = []

parsing_type: Parsing = Parsing.NONE

def getMapped(mappings, inputVal: int) -> int:
    for mapping in mappings:
        dest_start, src_start, size = mapping
        if src_start <= inputVal < src_start+size:
            return dest_start + (inputVal - src_start)
    return inputVal

lines = readFile('inputs/input05.txt')
for line in lines:
    if not line:
        continue # Skip empty lines

    # Is it a line with text?
    if line.startswith('seeds:'):
        seeds = extractAllNumbers(line)
        continue

    match line:
        case 'seed-to-soil map:':
            parsing_type = Parsing.SEED_TO_SOIL
            continue
        case 'soil-to-fertilizer map:':
            parsing_type = Parsing.SOIL_TO_FERTILIZER
            continue
        case 'fertilizer-to-water map:':
            parsing_type = Parsing.FERTILIZER_TO_WATER
            continue
        case 'water-to-light map:':
            parsing_type = Parsing.WATER_TO_LIGHT
            continue
        case 'light-to-temperature map:':
            parsing_type = Parsing.LIGHT_TO_TEMPERATURE
            continue
        case 'temperature-to-humidity map:':
            parsing_type = Parsing.TEMPERATURE_TO_HUMIDITY
            continue
        case 'humidity-to-location map:':
            parsing_type = Parsing.HUMIDITY_TO_LOCATION
            continue

    # Need to parse mappings
    match parsing_type:
        case Parsing.SEED_TO_SOIL:
            seed2soil.append(extractAllNumbers(line))
        case Parsing.SOIL_TO_FERTILIZER:
            soil2fertilizer.append(extractAllNumbers(line))
        case Parsing.FERTILIZER_TO_WATER:
            fertilizer2water.append(extractAllNumbers(line))
        case Parsing.WATER_TO_LIGHT:
            water2light.append(extractAllNumbers(line))
        case Parsing.LIGHT_TO_TEMPERATURE:
            light2temperature.append(extractAllNumbers(line))
        case Parsing.TEMPERATURE_TO_HUMIDITY:
            temperature2humidity.append(extractAllNumbers(line))
        case Parsing.HUMIDITY_TO_LOCATION:
            humidity2location.append(extractAllNumbers(line))

locations = []
for seed in seeds:
    soil = getMapped(seed2soil, seed)
    fertilizer = getMapped(soil2fertilizer, soil)
    water = getMapped(fertilizer2water, fertilizer)
    light = getMapped(water2light, water)
    temperature = getMapped(light2temperature, light)
    humidity = getMapped(temperature2humidity, temperature)
    location = getMapped(humidity2location, humidity)
    locations.append(location)

locations.sort()
print(locations[0])
