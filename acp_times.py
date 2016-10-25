"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math

#  Note for CIS 322 Fall 2016:
#  You MUST provide the following two functions
#  with these signatures, so that I can write
#  automated tests for grading.  You must keep
#  these signatures even if you don't use all the
#  same arguments.  Arguments are explained in the
#  javadoc comments. 
#

brevets = [200,300,400,600,1000]

def open_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  A date-time string indicating
           the official start time of the brevet
    Returns:
       A date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """
   
    open = ""
    # To make sure that brevet values are the official distances
    if brevet_dist_km in brevets:
    	# Computation for open time if controle is less than or equal to 200
    	if control_dist_km <= 200:
    		time = brevet_start_time.replace(hours=+(compute(control_dist_km,34)[0])).replace(minutes=+(compute(control_dist_km,34)[1]))
    		open = time.format('YYYY-MM-DD HH:mm')
    	
    	# Computation for open time if controle is between 200 and 400
    	elif control_dist_km > 200 and control_dist_km <= 400:
    		first = compute(200,34)
    		second = compute(control_dist_km-200,32)
    	
    		time = brevet_start_time.replace(hours=+ (first[0] + second[0])).replace(minutes=+ (first[1] + second[1]))
    		open = time.format('YYYY-MM-DD HH:mm')
    	
    	# Computation for open time if controle is between 400 and 600
    	elif control_dist_km > 400 and control_dist_km <= 600:
    		first = compute (200,34)
    		second = compute(200,32)
    		third = compute(control_dist_km-400,30)
    	
    		time = brevet_start_time.replace(hours=+ (first[0] + second[0] + third[0])).replace(minutes=+ (first[1] + second[1] + third[1]))
    		open = time.format('YYYY-MM-DD HH:mm')
    	
    	# Computation for open time if controle is between 600 and 1000
    	elif control_dist_km > 600 and control_dist_km <= 1000:
    		first = compute (200,34)
    		second = compute(200,32)
    		third = compute(200,30)
    		fourth = compute(control_dist_km-600,28)
    	
    		time = brevet_start_time.replace(hours=+ (first[0] + second[0] + third[0] + fourth[0])).replace(minutes=+ (first[1] + second[1] + third[1] + fourth[1]))
    		open = time.format('YYYY-MM-DD HH:mm')
    	
    	# Computation for open time if controle is greater than 1000
    	elif control_dist_km > 1000:
    		first = compute (200,34)
    		second = compute(200,32)
    		third = compute(200,30)
    		fourth = compute(200,28)
    		fifth = compute(control_dist_km-1000,26)
    	
    		time = brevet_start_time.replace(hours=+ (first[0] + second[0] + third[0] + fourth[0] + fifth[0])).replace(minutes=+ (first[1] + second[1] + third[1] + fourth[1] + fifth[1]))
    		open = time.format('YYYY-MM-DD HH:mm')
    else:
    	print("Invalid brevet distance")
    print("open time: " + open)	
    return open

def close_time( control_dist_km, brevet_dist_km, brevet_start_time ):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet in kilometers,
           which must be one of 200, 300, 400, 600, or 1000 (the only official
           ACP brevet distances)
       brevet_start_time:  A date-time string indicating
           the official start time of the brevet
    Returns:
       A date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """
    close = ""
    # Checks if brevet value is official brevet distance
    if brevet_dist_km in brevets:
    	# Computation for close time if controle is less than or equal to 600
    	if control_dist_km <= 600:
    		time = brevet_start_time.replace(hours=+compute(control_dist_km,15)[0]).replace(minutes=+compute(control_dist_km,15)[1])
    		close = time.format('YYYY-MM-DD HH:mm')
    	
    	# Computation for close time if controle is between 600 and 1000
    	elif control_dist_km > 600 and control_dist_km <= 1000:
    		first = compute(600,15)
    		second = compute(control_dist_km-600,11.428)
    	
    		time = brevet_start_time.replace(hours=+ (first[0] + second[0])).replace(minutes=+ (first[1] + second[1]))
    		close = time.format('YYYY-MM-DD HH:mm')
    	
    	# Computation for close time if controle is greater than 1000
    	elif control_dist_km > 1000:
    		first = compute (600,15)
    		second = compute(200,11.428)
    		third = compute(control_dist_km-1000,13.333)
    	
    		time = brevet_start_time.replace(hours=+ (first[0] + second[0] + third[0])).replace(minutes=+ (first[1] + second[1] + third[1]))
    		close = time.format('YYYY-MM-DD HH:mm')
    else:
    	print("Invalid brevet distance")
    print("close time: " + close)	
    return close

# Method to compute the open and close times that returns an array where the first element
# is the hour that is to be added and the second element is the minutes to be added
def compute(distance, speed):
	array = []
	time = distance / speed
	minutes = (time - math.floor(time)) * 60
	array.append(math.floor(time))
	array.append(int(minutes))
	return array

