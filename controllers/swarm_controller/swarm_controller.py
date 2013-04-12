# File:          _crabs.py
# Date:          
# Description:   
# Author:        
# Modifications: 

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
#
# or to import the entire module. Ex:
#  from controller import *
from controller import *
import epuck_basic

# Here is the main class of your controller.
# This class defines how to initialize and how to run your controller.
# Note that this class derives Robot and so inherits all its functions
class _crabs (epuck_basic.EpuckBasic):
  
  # User defined function for initializing and running
  # the _crabs class
  def run(self):
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  led = self.getLed('ledname')
    
    # Main loop
    while True:
      # Perform a simulation step of 64 milliseconds
      # and leave the loop when the simulation is over
      if self.step(64) == -1:
        break
    
    testrun(self)
      
    #Get Sensor Data
    # sensors = get_proximities(self)

    # update_search_speed(sensors, distance_treshold)
    # search_left_wheel_speed = get_search_left_wheel_speed()
    # search_right_wheel_speed = get_search_right_wheel_speed()

    # If Robot Has to Avoid Obstacle
    # if( (search_right_wheel_speed == -300 && search_right_wheel_speed = 700) || (search_right_wheel_speed = 700 && search_right_wheel_speed = -300) )
        # set_wheel_speeds(self, search_left_wheel_speed, search_right_wheel_speed)
    
    # else
    # swarm_retrieval(sensors, ir_treshold)
    # retrieval_left_wheel_speed = get_retrieval_left_wheel_speed()
    # retrieval_right_wheel_speed = get_retrieval_right_wheel_speed()
    
    #If Robot Is Currently in "Push-Mode"
    #if(retrieval_left_wheel_speed == 1000 && retrieval_right_wheel_speed == 1000)
        #validate_pushing()
        #if(get_stagnation_state() == TRUE)
            #stagnation_recovery(sensors, distance_treshold)
            #stagnation_left_wheel_speed = get_stagnation_left_wheel_speed()
            #stagnation_right_wheel_speed = get_stagnation_right_wheel_speed()
        #else
            #set_wheel_speeds(self, retrieval_left_wheel_speed, retrieval_right_wheel_speed)
    #else
       #set_wheel_speeds(self, retrieval_left_wheel_speed, retrieval_right_wheel_speed)
       
     #run_timestep(self, cycles)

# The main program starts from here

# This is the main program of your controller.
# It creates an instance of your Robot subclass, launches its
# function(s) and destroys it at the end of the execution.
# Note that only one instance of Robot should be created in
# a controller program.
controller = _crabs()
controller.run()
