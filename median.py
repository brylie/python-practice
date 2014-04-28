def median(numbers):
    """Return the median of a list of numbers."""
    length = len(numbers)
    numbers.sort()
    
    if length % 2 == 0:
        place = length / 2
        calculated_median = (numbers[place] + numbers[place - 1]) / 2.0
    else:
        place = (length - 1) / 2
        calculated_median = numbers[place]
    return calculated_median
