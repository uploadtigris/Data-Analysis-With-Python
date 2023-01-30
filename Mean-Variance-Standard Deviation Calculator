
import numpy as np

input = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def calculate(a):
    if len(input) <= 9:

        z = np.array(a)
        threebythree = np.zeros((3, 3))
        threebythree[0] = z[0:3]
        threebythree[1] = z[3:6]
        threebythree[2] = z[6:9]
        final_array = np.array(threebythree, dtype='int16')

        #Axis1:
        #Calculate the mean 
        axis1_mean = np.mean(final_array, axis = 0)

        #Axis1 variance
        axis1_variance = np.var(final_array, axis = 0)
        print(axis1_variance)

        #standard deviation
        axis1_std = np.std(final_array, axis = 0)
        print(axis1_std)

        #max
        #min
        #sum

        #Axis2:
        #Calculate the mean 
        axis2_mean = np.mean(final_array, axis = 1)

        #Axis2 variance
        axis2_variance = np.var(final_array, axis = 1)
        print(axis2_variance)

        #standard deviation
        axis2_std = np.std(final_array, axis = 1)
        #max
        #min
        #sum

        #Flattened:
        #Calculate the mean 
        axis_flat = final_array.flatten()
        axis_mean_flat = np.mean(axis_flat)

        #Flattened variance
        axis_var_flat = np.var(axis_flat)
        print(axis_var_flat)

        #standard deviation
        axis_std_flat = np.std(axis_flat)
        print(axis_std_flat)


        #max
        #min
        #sum


        results = {
            'mean': [[axis1_mean[0], axis1_mean[1], axis1_mean[2]], [axis2_mean[0], axis2_mean[1], axis2_mean[2]], axis_mean_flat], 
            'variance': [[axis1_variance[0], axis1_variance[1], axis1_variance[2]], [axis2_variance[0], axis2_variance[1], axis2_variance[2]], axis_var_flat], 
            'standard deviation': [axis1_std[0], [axis1_std[1], [axis1_std[2]], [axis2_std[0], axis2_std[1], [axis2_std[2]]],]], 
            'max': [[0, 0, 0], [0, 0, 0], 0], 
            'min': [[0, 0, 0], [0, 0, 0], 0], 
            'sum': [[0, 0, 0], [0, 0, 0], 0]
        }

        print("{")
        for key, value in results.items():
            print("{} : {}".format(key, value))
        print("}")

        return()
    else:
        print('ERROR: Please only list of 9 numbers are allowed')



calculate(input)
