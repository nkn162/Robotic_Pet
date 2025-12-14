from motion.interpolator import Interpolator
class Behaviour:
    def __init__(self, servo):
        from motion.poses import STAND
        self.servo = servo
        self.state = "IDLE"
        self.interpolator = None
        self.action_queue = []
        self.current_pose = STAND.copy()

    def command(self, cmd):
        if self.state != "IDLE":
            return

        if cmd == "SIT":
            from motion.poses import STAND, BOW

            self.action_queue = [BOW, STAND]
            self.start_next_motion()
            self.interpolator = Interpolator(self.servo, duration=0.8)
            self.interpolator.start_move(self.current_pose, BOW)
            self.state = "MOVING"
        
        elif cmd == "WIGGLE":
            from motion.poses import WIGGLE_LEFT, WIGGLE_RIGHT, STAND

            self.action_queue = [WIGGLE_LEFT, WIGGLE_RIGHT, WIGGLE_LEFT, STAND]
            self.start_next_motion()
    
    def start_next_motion(self):
        if not self.action_queue:
            self.state = "IDLE"
            return

        next_pose = self.action_queue.pop(0)
        self.interpolator = Interpolator(self.servo, duration=0.6)
        self.interpolator.start_move(self.current_pose, next_pose)
        self.state = "MOVING"

    def update(self, dt):
        if self.state == "MOVING":
            done = self.interpolator.update(dt)
            if done:
                self.current_pose = self.interpolator.target.copy()
                self.start_next_motion()