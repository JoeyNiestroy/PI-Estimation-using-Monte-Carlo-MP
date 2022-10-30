import random
from multiprocessing import Pool
from itertools import repeat
from multiprocessing import Pool, freeze_support
import sys

"""Main function creates array of points through sub function and tests through subfunction returns final volume"""
def monte_carlo_estimation(radius_of_sphere = 1, n = 10):
    test_arr = []
    for _ in range(0,n):
        test_cor = gen_random_array(radius= radius_of_sphere)
        test_arr.append(test_cor)
    """Moved checking array to multiproccessing"""
    with Pool() as pool:
        bool_array = pool.starmap(check_cor_in_sphere, zip(test_arr, repeat(radius_of_sphere)))
    counter = 0
    for boolean in bool_array:
        if boolean is True:
            counter += 1
        else:
            pass
    volume =  (((2*radius_of_sphere)**3)*(counter/n))
    return volume/((4/3)*(radius_of_sphere**3))
    
"""Function to generate arrays of points"""
def gen_random_array(radius, dimesions = 3):
    arr = []
    for _ in range(0,dimesions):
        x = random.uniform((-radius), (radius))
        arr.append(x)
    return arr
"""Function to check if points are in sphere, retruns boolean"""
def check_cor_in_sphere(array, radius):
    sum = 0
    for val in array:
        sum += val**2
    if (sum) < radius**2:
        return True
    else:
        return False

if __name__ == "__main__":
    freeze_support()
    print(monte_carlo_estimation(radius_of_sphere= 2, n = int(sys.argv[1])))
    