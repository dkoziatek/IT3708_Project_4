NB_LEDS = 8
ON = 1
OFF = 0
PUSH_TRESHOLD = 500

class retrieval:
    def __init__(self):
        self.left_wheel_speed = 0
        self.right_wheel_speed = 0
        self.LED = [None]*NB_LEDS
        self.converge = False
        self.push = True
        
    def __update_speed(self, IR_number):
        if (IR_number== 0):
            self.left_wheel_speed = self.left_wheel_speed + 700            
        elif(IR_number == 7):
            self.right_wheel_speed = self.right_wheel_speed + 700            
        elif(IR_number ==1):
            self.left_wheel_speed = self.left_wheel_speed + 350
        elif(IR_number == 6):
            self.right_wheel_speed = self.right_wheel_speed + 350            
        elif(IR_number == 2):
            self.left_wheel_speed = self.left_wheel_speed + 550
            self.right_wheel_speed = self.right_wheel_speed - 300            
        elif(IR_number == 5):
            self.right_wheel_speed = self.right_wheel_speed + 550
            self.left_wheel_speed = self.left_wheel_speed - 300            
        elif(IR_number == 3):
            self.left_wheel_speed = self.left_wheel_speed + 500
        elif(IR_number == 4):
            self.right_wheel_speed = self.right_wheel_speed + 500

    def __converge_to_box(self,IR_sensor_value, IR_treshold):
        self.left_wheel_speed = 0
        self.right_wheel_speed = 0
        for i in range (NB_LEDS):
            if (IR_sensor_value[i] < IR_treshold):
                self.LED[i] = ON
                self.update_speed(i)
            else:
                self.LED[i] = OFF
                        
    def __push_box(self, IR_sensor_value, IR_treshold):
        self.left_wheel_speed = 0
        self.right_wheel_speed = 0
        for i in range(NB_LEDS):
            if (self.LED[i] == ON):
                self.LED[i] = OFF
            else:
                self.LED[i] = ON
                
        if(IR_sensor_value[0] < IR_treshold) and (IR_sensor_value[-1] < IR_treshold):
            self.left_wheel_speed = 1000
            self.right_wheel_speed = 1000
                    
    def __select_behaviour(self, IR_sensor_value):
        self.push = False
        self.converge = True
        for i in range(NB_LEDS):
            if (IR_sensor_value[i] < PUSH_TRESHOLD):
                self.push = True
                break

    def swarm_retrieval(self, IR_sensor_value, IR_treshold):
        self.select_behaviour(IR_sensor_value)
        if (self.push):
            self.push_box(IR_sensor_value,  IR_treshold)
        else:
            self.converge_to_box(IR_sensor_value, IR_treshold)

    def get_retrieval_left_wheel_speed(self):
        return self.left_wheel_speed
    def get_retrieval_right_wheel_speed(self):
        return self.right_wheel_speed
    def get_LED_state(self, ledNum):
        return self.LED[ledNum]
