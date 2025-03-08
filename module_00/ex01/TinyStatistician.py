import numpy as np
import math

class TinyStatistician:
    def __init__(self, x):
        self.x = np.array(x)
        self.sorted_data = np.sort(np.array(x))

    def mean(self):
        return np.sum(self.x) / len(self.x)

    def median(self):
        index = int(len(self.x) / 2)
        if len(self.x) % 2 == 0:
            return (self.sorted_data[index] + self.sorted_data[index + 1]) / 2
        else:
            return float(self.sorted_data[index])

    def quartile(self):
        if self.x is None:
            return None
        else:
            index25 = 0.25 * (len(self.x) - 1)
            index75 = 0.75 * (len(self.x) - 1)
            quartile25 = float(self.sorted_data[math.floor(index25)]) + (index25 - math.floor(index25)) * (float(self.sorted_data[math.ceil(index25)]) - float(self.sorted_data[math.floor(index25)]))
            quartile75 = float(self.sorted_data[math.floor(index75)]) + (index75 - math.floor(index75)) * (float(self.sorted_data[math.ceil(index75)]) - float(self.sorted_data[math.floor(index75)]))
            return [quartile25, quartile75]

    def percentile(self, p):
        if self.x is None:
            return None
        else:
            index_p = p / 100 * (len(self.x) - 1)
            percentile_p = float(self.sorted_data[math.floor(index_p)]) + (index_p - math.floor(index_p)) * (float(self.sorted_data[math.ceil(index_p)]) - float(self.sorted_data[math.floor(index_p)]))
            return percentile_p

    def variance(self):
        if self.x is None:
            return None

if __name__ == "__main__":
    a = [1, 42, 300, 10, 59]
    tiny = TinyStatistician(a)
    print(f"mean : {tiny.mean()}")
    print(f"median : {tiny.median()}")
    print(f"quartile : {tiny.quartile()}")
    print(f"percentile(10) : {tiny.percentile(10)}")
    print(f"percentile(15) : {tiny.percentile(15)}")
    print(f"percentile(20) : {tiny.percentile(20)}")

