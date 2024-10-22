import data
import math
# Write your functions for each part in the space below.
#point1 = data.Point(1,2)
#point2 = data.Point(3,4)
#point3 = data.Point(5,6)
# Part 1
def first_element(value:list):
    list1 = []
    for i in range(len(value)):
        if len(value[i]) > 0:
            list1.append(value[i][0])
    return list1


# Part 2
def x_coordinates(value:list[list[data.Point]]):
    list1 = []
    for i in value:
            list1.append(i.x)
    return list1


# Part 3
def are_in_positive_quadrant(value:list[list[data.Point]])->list[list]:
    list1 = []
    for i in value:
        if i.x > 0 and i.y > 0:
            list1.append([i.x,i.y])
    return list1

# Part 4
def distance(value:list[list[data.Point]])->float:
    distance_length = math.sqrt((((value[0].x))-(value[1].x))**2+((value[0].y)-(value[1].y))**2)
    return round(distance_length, 2)


# Part 5
def manhattan_distance(value:list[list[data.Point]])->int:
    manhattan_length = (value[0].x-value[1].x)
    manhattan_length += (value[0].y-value[1].y)
    return abs(manhattan_length)


# Part 6
def distance_all(num:list[list[data.Point]])->float:
    for i in range(len(num)):
        dist_records = (math.sqrt((num[i].x-0)**2+(num[i].y-0)**2))
    return float(round(dist_records, 2))