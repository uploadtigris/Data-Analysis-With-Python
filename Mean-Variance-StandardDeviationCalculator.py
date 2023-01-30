############################################
#   Author: Tigris Mendez
#   Date: 1/29/23
#
#
#
#  
############################################

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

        #-------------------------------------------
        #Assigning Variables

        #Axis1:
        
        #Calculate the mean 
        axis1_mean = np.mean(final_array, axis = 0)
        axis1_mean = axis1_mean.tolist()

        #Axis1 variance
        axis1_variance = np.var(final_array, axis = 0)
        axis1_variance = axis1_variance.tolist()

        #standard deviation
        axis1_std = np.std(final_array, axis = 0)
        axis1_std = axis1_std.tolist()

        #max
        axis1_max = np.max(final_array, axis = 0)
        axis1_max = axis1_max.tolist()


        #min
        axis1_min = np.min(final_array, axis = 0)
        axis1_min = axis1_min.tolist()

        #sum
        axis1_sum = np.sum(final_array, axis = 0)
        axis1_sum = axis1_sum.tolist()

        #-------------------------------------------

        #Axis2:

        #Calculate the mean 
        axis2_mean = np.mean(final_array, axis = 1)
        axis2_mean = axis2_mean.tolist()

        #Axis2 variance
        axis2_variance = np.var(final_array, axis = 1)
        axis2_variance = axis2_variance.tolist()

        #standard deviation
        axis2_std = np.std(final_array, axis = 1)
        axis2_std = axis2_std.tolist()

        #max
        axis2_max = np.max(final_array, axis = 1)
        axis2_max = axis2_max.tolist()

        #min
        axis2_min = np.min(final_array, axis = 1)
        axis2_min = axis2_min.tolist()

        #sum
        axis2_sum = np.sum(final_array, axis = 1)
        axis2_sum = axis2_sum.tolist()

        #-------------------------------------------

        #Flattened:

        #Calculate the mean 
        flat = final_array.flatten()
        mean_flat = np.mean(flat)
        mean_flat = mean_flat.tolist()

        #Flattened variance
        axis_var_flat = np.var(flat)
        axis_var_flat = axis_var_flat.tolist()

        #standard deviation
        axis_std_flat = np.std(flat)
        axis_std_flat = axis_std_flat.tolist()

        #max
        max_flat = np.max(flat)
        max_flat = max_flat.tolist()

        #min
        min_flat = np.min(flat)

        #sum
        sum_flat = np.sum(flat)

        #[axis1_mean[0], axis1_mean[1], axis1_mean[2]]

        results = {
            'mean': [[axis1_mean], [axis2_mean], mean_flat], 
            'variance': [[axis1_variance], [axis2_variance], axis_var_flat], 
            'standard deviation': [[axis1_std], [axis2_std], axis_std_flat], 
            'max': [[axis1_max], [axis2_max], max_flat], 
            'min': [[axis1_min], [axis2_min], min_flat], 
            'sum': [[axis1_sum], [axis2_sum], sum_flat]
        }

    # Below\\\ is useful for printing out the above ^^^
        # print("{")
        # for key, value in results.items():
        #     print("{} : {}".format(key, value))
        # print("}")

        return(results)
    else:
        print('ERROR: Please only list of 9 numbers are allowed')

    


print("\n\n\n\n\n\n{")
for key, value in calculate(input).items():
        print("{} : {}".format(key, value))
print("}\n\n\n\n\n\n")
