from abc import ABC, abstractmethod  # For Builder classes

# Doesn't need an endless list of arguments when initialized
class Robot:
  # Uses a lot of flag logic here:  Is that necessary?
  # Does the use of this flag logic create other problems?
  def __init__(self):
    self.bipedal = False
    self.quadripedal = False
    self.wheeled = False
    self.flying = False
    self.traversal = []
    self.detection_systems = []

  # Huge decision statement: why is this not good?
  # Can we improve this?
	def __str__(self):

		if self.traversal:
			self.name += "\nTraversal modules installed:\n"
		for module in self.traversal:
			self.name += "- " + str(module) + "\n"
		if self.detection_systems:
			self.name += "Detection systems installed:\n"
		for system in self.detection_systems:
			self.name += "- " + str(system) + "\n"
		return self.name

#'{self.bipedal} BIPEDAL'.format(self=self)
#---------------------------------------------------------------------------

# Concrete classes for componenets
# In a real application, there would be an endless list of these, each one
#   composing additional subcomponents
class BipedalLegs:
    BipedalLegs = None
class QuadripedalLegs:
    QuadripedalLegs = None
class Arms:
    Arms = None
class Wings:
    Wings = None
class Blades:
    Blades = None
class FourWheels:
    FourWheels = None
class TwoWheels:
    TwoWheels = None
class CameraDetectionSystem:
    CameraDetectionSystem = None
class InfraredDetectionSystem:
    InfraredDetectionSystem =None

#----------------------------------------------------------------------------
# Note that this code was place at the top of this program for visibility
#from abc import ABC, abstractmethod

# The abstract superclass for all the builders
# We're using inheritence, but it's shallow
class RobotBuilder(ABC):

  @abstractmethod
  def reset(self):
    pass
  @abstractmethod
  def build_traversal(self):
    pass
  @abstractmethod
  def build_detection_system(self):
    pass
  @abstractmethod
  def getBipedalLegs(self):
    BipedalLegs = BipedalLegs()
    BipedalLegs = "two legs"
  @abstractmethod
  def getQuadripedalLegs(self):
    QuadripedalLegs = QuadripedalLegs()
    QuadripedalLegs = "four legs"
  @abstractmethod
  def getArms(self):
    Arms = Arms()
    Arms = "two arms"
  @abstractmethod
  def getWings(self):
    Wings = Wings()
    Wings = "wings"
  def getBlades(self):
    Blades = Blades()
    Blades = "blades"
  def getFourWheels(self):
    FourWheels = FourWheels()
    FourWheels = "four wheels"
  def getTwoWheels(self):
    TwoWheels = TwoWheels()
    TwoWheels = "two wheels"
  def getCameraDetectionSystem(self):
    CameraDetectionSystem = CameraDetectionSystem()
    CameraDetectionSystem = "cameras"
  def getInfraredDetectionSystem(self):
    InfraredDetectionSystem = InfraredDetectionSystem()
    InfraredDetectionSystem = "infrared"


# Concrete Builder class:  there would be MANY of these
class AndroidBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot()

  def reset(self):
    self.product = Robot()

  # All of the concrete builders have this in common
  # Should it be elevated to the superclass?
  def get_product(self):
    return self.product

  def build_traversal(self):
    self.product.bipedal = True
    self.product.traversal.append(getBipedalLegs())
    self.product.traversal.append(getArms())

  def build_detection_system(self):
    self.product.detection_systems.append(getCameraDetectionSystem())

# Concrete Builder class:  there would be many of these
class AutonomousCarBuilder(RobotBuilder):
  def __init__(self):
    self.product = Robot()

  def reset(self):
    self.product = Robot()

  # All of the concrete builders have this in common
  # Should it be elevated to the superclass?
  def get_product(self):
    return self.product

  def build_traversal(self):
    self.product.wheeled = True
    self.product.traversal.append(getFourWheels())

  def build_detection_system(self):
    self.product.detection_systems.append(getInfraredDetectionSystem())

#-------------------------------------------------------------------------
'''
# Remove # in line above to comment out this section when using Director

# Using the builders to create different robots
builder = AndroidBuilder()
builder.build_traversal()
builder.build_detection_system()
print(builder.get_product())

builder = AutonomousCarBuilder()
builder.build_traversal()
builder.build_detection_system()
print(builder.get_product())
'''
#-------------------------------------------------------
#  Keep line below whether testing builders or director

#-------------------------------------------------------

# Diretor manages all of the Builders
# Do we need separate make methods?
class Director:
    def make_android(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

    def make_autonomous_car(self, builder):
        builder.build_traversal()
        builder.build_detection_system()
        return builder.get_product()

director = Director()

builder = AndroidBuilder()
print(director.make_android(builder))

builder = AutonomousCarBuilder()
print(director.make_autonomous_car(builder))

# comment out line below when testing director
