from abc import ABC, abstractmethod

class ServoInterface(ABC):
    @abstractmethod
    def set_angle(self, name: str, angle_deg: float):
        pass

    @abstractmethod
    def update(self, dt: float):
        pass