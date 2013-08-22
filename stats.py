# stats.py - Statistics utility module.
import math

def main ():
    s = Series ([1, 2, 3])
    print s.mean

# Functions:

def avg (series):
    return mean (series)

def mean (series):
    m = sum (series) / float (len (series))
    return m

def variance (series):
    m = mean (series)
    v = sum ([(s - m)**2 for s in series]) / (len (series) - 1.0)
    return v

def avedev (series):
    # measure of central tendency
    measure = mean
    m = measure (series)
    ad = sum ([abs(i - m) for i in series]) / float (len (series))
    return ad

class Series:
    mean = 0.0
    variance = 0.0
    SD = 0.0
    length = 0
    series = None
    num_reversions = 0
    reversions = 0

    def __init__(self, series):
        # Save series
        self.series = series
        self.length = len (series)

        # Calculate mean
        total = 0.0
        for i in series:
            total += i
        mean = total / len(series)
        self.mean = mean

        # Calculate variance + SD
        squared_sums = 0.0
        for i in series:
            squared_sums += (i - mean) * (i - mean)
        variance = squared_sums / (len(series) - 1)
        self.variance = variance
        SD = math.sqrt (variance)
        self.SD = SD

        # Count mean reversions
        is_crossed = (series[0] >= mean)
        num_reversions = 0
        time_count = 0
        reversions = list()
        for i in series:
            time_count += 1
            if (is_crossed != (i >= mean)):
                reversions.append(time_count)
                time_count = 1
                num_reversions += 1
                is_crossed = (i >= mean)
        self.reversions = reversions
        self.num_reversions = num_reversions

if __name__ == "__main__":
    main()
