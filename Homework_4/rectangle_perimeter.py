def segment_length(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def rec_perimeter(num):
    perimeter = segment_length(num[0], num[1], num[2], num[3]) \
                + segment_length(num[2], num[3], num[4], num[5]) \
                + segment_length(num[4], num[5], num[6], num[7]) \
                + segment_length(num[6], num[7], num[1], num[2])
    return perimeter


num = [float(num) for num in input("""Enter Coordinates of rectangle 
example - x1, y1, x2, y2, x3, y3, x4, y4: """).split()]
print(rec_perimeter(num))
