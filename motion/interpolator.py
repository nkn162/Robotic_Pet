class Interpolator:
    def __init__(self, servo, duration):
        self.servo = servo
        self.duration = duration
        self.elapsed = 0
        self.start = {}
        self.target = {}

    def start_move(self, start_pose, target_pose):
        self.start = start_pose.copy()
        self.target = target_pose.copy()
        self.elapsed = 0

    def update(self, dt):
        self.elapsed += dt
        t = min(self.elapsed / self.duration, 1.0)

        for k in self.start:
            a = self.start[k] + (self.target[k] - self.start[k]) * t
            self.servo.set_angle(k, a)

        return t >= 1.0