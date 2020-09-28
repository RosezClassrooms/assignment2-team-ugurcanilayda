from enum import Enum   # We checked the chapter 2 from book

from abc import ABC, abstractmethod





#we read the chapter 2 and reviewed the examples codes from the book ,also looked example codes about builder.py from mycourses and we decided to try this method.

#while doing assigment2, we took reference from the code about PizzaBuilder.



RobotType=Enum('RobotType', 'BIPEDALROBOT QUADRIPEDALROBOT FLYINGROBOT ROBOTONWHEELS')

RobotTraversal=Enum('RobotTraversal','twolegs fourlegs twoarms wings blades fourwheels twowheels')

RobotDetectionSystem=Enum('RobotDetectionSystem', 'cameras infrared')









class Robot:



	def __init__(self, name):

  		self.name=name

  		self.traversal=[]

  		self.detection_systems = []





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





class AndroidBuilder(RobotBuilder):

  def __init__(self):

    self.product=Robot(RobotType.BIPEDALROBOT.name)



  def reset(self):

    self.product = Robot(RobotType.BIPEDALROBOT.name)





  def get_product(self):

    return self.product



  def build_traversal(self):

  	self.product.traversal.append(RobotTraversal.twolegs.name)

  	self.product.traversal.append(RobotTraversal.twoarms.name)



  def build_detection_system(self):

    self.product.detection_systems.append(RobotDetectionSystem.cameras.name)







class AutonomousCarBuilder(RobotBuilder):

  def __init__(self):

    self.product = Robot(RobotType.ROBOTONWHEELS.name)



  def reset(self):

    self.product = Robot(RobotType.ROBOTONWHEELS.name)





  def get_product(self):

    return self.product



  def build_traversal(self):

    self.product.traversal.append(RobotTraversal.fourwheels.name)



  def build_detection_system(self):

    self.product.detection_systems.append(RobotDetectionSystem.infrared.name)





class FlyingRobotBuilder(RobotBuilder):

  def __init__(self):

    self.product = Robot(RobotType.FLYINGROBOT.name)



  def reset(self):

    self.product = Robot(RobotType.FLYINGROBOT.name)



  def get_product(self):

    return self.product



  def build_traversal(self):

    self.product.traversal.append(RobotTraversal.wings.name)

    self.product.traversal.append(RobotTraversal.twoarms.name)



  def build_detection_system(self):

    self.product.detection_systems.append(RobotDetectionSystem.cameras.name)

    self.product.detection_systems.append(RobotDetectionSystem.infrared.name)



class Director:

    def make_android(self, builder):

        builder.build_traversal()

        builder.build_detection_system()

        return builder.get_product()



    def make_autonomous_car(self, builder):

        builder.build_traversal()

        builder.build_detection_system()

        return builder.get_product()





    def make_flying_robot(self, builder):

    	builder.build_traversal()

    	builder.build_detection_system()

    	return builder.get_product()





    @property

    def robot(self):

        return self.builder.product





def main():

	director = Director()



	builder = AndroidBuilder()

	print(director.make_android(builder))



	builder = AutonomousCarBuilder()

	print(director.make_autonomous_car(builder))



	builder=FlyingRobotBuilder()

	print(director.make_flying_robot(builder))





if __name__== '__main__':

	main()

