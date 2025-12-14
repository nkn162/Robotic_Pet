import pybullet as p
import pybullet_data

from hw.servo_interface import ServoInterface


class PyBulletServo(ServoInterface):
    def __init__(self):
        p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0, 0, -9.81)

        p.loadURDF("plane.urdf")

        self.robot_id = self._build_robot()
        self.joint_map = {
            "FL": 0,
            "FR": 1,
            "BL": 2,
            "BR": 3,
        }

        self.angles = {k: 90 for k in self.joint_map}

        # Disable default motors
        for j in range(p.getNumJoints(self.robot_id)):
            p.setJointMotorControl2(
                self.robot_id, j,
                controlMode=p.VELOCITY_CONTROL,
                force=0
            )

    def _build_robot(self):
        body = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.05, 0.03, 0.02])
        body_v = p.createVisualShape(p.GEOM_BOX, halfExtents=[0.05, 0.03, 0.02],
                                     rgbaColor=[0.8, 0.8, 0.8, 1])

        leg = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.005, 0.02, 0.005])
        leg_v = p.createVisualShape(p.GEOM_BOX, halfExtents=[0.005, 0.02, 0.005],
                                    rgbaColor=[0.2, 0.2, 0.8, 1])

        return p.createMultiBody(
            baseMass=1.0,
            baseCollisionShapeIndex=body,
            baseVisualShapeIndex=body_v,
            basePosition=[0, 0, 0.1],

            linkMasses=[0.1]*4,
            linkCollisionShapeIndices=[leg]*4,
            linkVisualShapeIndices=[leg_v]*4,
            linkPositions=[
                [ 0.04,  0.02, 0.0],   # FL
                [ 0.04, -0.02, 0.0],   # FR
                [-0.04,  0.02, 0.0],   # BL
                [-0.04, -0.02, 0.0],   # BR
            ],
            linkOrientations=[[0,0,0,1]]*4,
            linkInertialFramePositions=[[0,0,0]]*4,
            linkInertialFrameOrientations=[[0,0,0,1]]*4,
            linkParentIndices=[0,0,0,0],
            linkJointTypes=[p.JOINT_REVOLUTE]*4,
            linkJointAxis=[[1,0,0]]*4,
        )

    def set_angle(self, name, angle_deg):
        self.angles[name] = angle_deg

    def update(self, dt):
        for name, angle in self.angles.items():
            joint = self.joint_map[name]
            rad = (angle - 90) * 0.02  # ~±36°
            p.resetJointState(self.robot_id, joint, rad)

        p.stepSimulation()