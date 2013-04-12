from random import randint
ON = 1
OFF = 3
IR_DIFF_TRESHOLD = 4
DISTANCE_DIFF_TRESHOLD = 10
REVERSE_LIMIT = 20
TURN_LIMIT = 10
FORWARD_LIMIT = 40
NEIGHBOR_LIMIT = 300

ALIGN_STRAIGHT_TRESHOLD = 10
LOW_DIST_VALUE = 10

YES = 1
NO = 0
NEUTRAL = 3

class stagnation:
    def __init__(self):
        self.left_wheel_speed = 0
        self.right_wheel_speed = 0
        self.has_recovered = False
        self.turn_left = NEUTRAL
        self.green_LED_state = OFF
        self.reverse_counter = 0
        self.turn_counter = 0
        self.forward_coutner = 0
        self.twice = 0
        self.align_counter = 0
        

    def __LED_blink(self):
        if(self.green_LED_state == ON):
            self.green_LED_state = OFF
        else:
            self.green_LED_state = ON
    
    def __realign(self, distance_value):
        dist_diff_front = distance_value[-1] - distance_value[0]
        
        if (abs(dist_diff_front) > ALIGN_STRAIGHT_TRESHOLD):
            if (distance_value[0] < LOW_DIST_VALUE):
                self.right_wheel_speed = -500
                self.left_wheel_speed = 500
            elif(distance_value[-1] <  LOW_DIST_VALUE):
                self.left_wheel_speed = 500
                self.right_wheel_speed = -500
            elif(distance_value[1] < LOW_DIST_VALUE):
                self.right_wheel_speed = -1000
                self.left_wheel_speed = 700
            elif(distance_value[-2] < LOW_DIST_VALUE):
                self.right_wheel_speed = 700
                self.left_wheel_speed = -1000
        
        else:
            if (randint(0,1) == 1): #50/50
                self.right_wheel_speed = -500
                self.left_wheel_speed = 500
            else:
                self.right_wheel_speed = 500
                self.left_wheel_speed = -500
        
        self.has_recovered = True
        self.green_LED_state = OFF

    def find_new_spot(self, distance_value, DIST_TRESHOLD):
        if (self.twice == 2):
            self.has_recovered = True
            self.green_LED_state = OFF
            self.align_counter = 0

        elif(self.reverse_counter != REVERSE_LIMIT):
            self.reverse_counter += 1
            self.left_wheel_speed = -800
            self.right_wheel_speed = -800

        elif(self.turn_counter != TURN_LIMIT):
            self.turn_counter +=  1
            self.forward_counter = 0
            if (self.turn_left = NEUTRAL):
                if (randint(0,1) == 1): # 50/50
                    self.turn_left = OFF
                else:
                    self.turn_left = ON
                    
            if (self.turn_left == ON):
                self.left_wheel_speed = -300
                self.right_wheel_speed = 700
            else:
                self.left_wheel_speed = 700
                self.right_wheel_speed = -300

        elif(self.forward_counter != FORWARD_LIMIT):
            self.forward_counter += 1
            if (self.forward_counter == FORWARD_LIMIT -1):
                self.twice =  self.twice + 1
                self.turn_counter = 0
                if (self.turn_left == ON):
                    self.turn_left = OFF
                else:
                    self.turn_left = ON
                    
            update_search_speed(distance_value, DIST_TRESHOLD)
            self.left_wheel_speed = get_search_left_speed()
            self.right_wheel_speed = get_search_right_speed()
            
            if (self.left_wheel_self > 0) and (self.right_wheel_speed > 0):
                self.left_wheel_speed = 1000
                self.right_wheel_speed = 1000
                


    def 
    
