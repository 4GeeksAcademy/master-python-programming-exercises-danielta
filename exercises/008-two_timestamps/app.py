def two_timestamp(hr1, min1, sec1, hr2, min2, sec2):
    second = (hr2 * 3600) + (min2 * 60) + sec2
    first = (hr1 * 3600) + (min1 * 60) + sec1
    return second - first


# Invoke the function and pass two timestamps(6 intergers) as its arguments
print(two_timestamp(1,1,1,2,2,2))
