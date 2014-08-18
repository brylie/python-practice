def median(numbers):
    """Return the median of a list of numbers."""
    length = len(numbers)
    numbers.sort()
    
    if length % 2 == 0:
        place = int(length / 2) # index must be integer
        calculated_median = (numbers[place] + numbers[place - 1]) / 2.0
    else:
        place = int((length - 1) / 2) # index must be integer
        calculated_median = numbers[place]
    return calculated_median
