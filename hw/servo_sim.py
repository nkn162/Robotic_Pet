from hw.servo_interface import ServoInterface
class SimServo(ServoInterface):
    def __init__(self):
        self.angles = {
            "FL": 90,
            "FR": 90,
            "BL": 90,
            "BR": 90,
        }

    def set_angle(self, name, angle):
        self.angles[name] = angle

    def update(self, dt):
        pass  # nothing yet