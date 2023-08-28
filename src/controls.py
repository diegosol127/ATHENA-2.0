import RPi.GPIO as GPIO
from time import sleep
from math import sin, cos, atan2, sqrt, pi

class Controller:
	"""
	Methods for controlling the motion of a robot
	"""
	
	def __init__(self):
		print("Initializing Controller...")
		self.ENA = 5
		self.IN1 = 6
		self.IN2 = 13
		self.ENB = 17
		self.IN3 = 27
		self.IN4 = 22
		
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.IN1,GPIO.OUT)
		GPIO.setup(self.IN2,GPIO.OUT)
		GPIO.setup(self.IN3,GPIO.OUT)
		GPIO.setup(self.IN4,GPIO.OUT)
		GPIO.setup(self.ENA,GPIO.OUT)
		GPIO.setup(self.ENB,GPIO.OUT)
		
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.LOW)
		
		self.pA = GPIO.PWM(self.ENA,30)
		self.pB = GPIO.PWM(self.ENB,30)
		self.dcA = 0
		self.dcB = 0
		self.pA.start(self.dcA)
		self.pB.start(self.dcB)
		
	def move_forward(self,time):
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.HIGH)
		GPIO.output(self.IN4,GPIO.LOW)
		sleep(time)
		
	def move_backward(self,time):
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.HIGH)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.HIGH)
		sleep(time)
		
	# verify direction... (my right or your right)
	def move_right(self,time):
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.HIGH)
		GPIO.output(self.IN3,GPIO.HIGH)
		GPIO.output(self.IN4,GPIO.LOW)
		sleep(time)
		
	# verify direction... (my left or your left)
	def move_left(self,time):
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.HIGH)
		sleep(time)

	def stop_moving(self,time):
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.LOW)
		sleep(time)

	def set_speed(self,duty_cycle):
		self.pA.ChangeDutyCycle(duty_cycle)
		self.pB.ChangeDutyCycle(duty_cycle)

	def move_360(self,x,y,time):
		vel = min(100,sqrt(x**2 + y**2))
		ang = abs(atan2(abs(y),abs(x)) - pi/2)

		velBool = vel >= 75
		angBool = (ang >= pi/2 - 15*pi/180)

		print('\nVALS\n---------')
		print(f'vel: {vel}')
		print(f'ang: {ang*180/pi}')
		print(f'vel Bool: {velBool}')
		print(f'ang Bool: {angBool}\n')

		v_fast = vel
		v_slow = vel*abs(cos(ang))

		# Create deadzone to stop jerkiness
		if not (velBool and angBool):
			if x >= 0:
				self.pA.ChangeDutyCycle(v_slow)
				self.pB.ChangeDutyCycle(v_fast)

			elif x < 0:
				self.pA.ChangeDutyCycle(v_fast)
				self.pB.ChangeDutyCycle(v_slow)

			if y >= 0:
				self.move_forward(time)
				print('forward')

			elif y < 0:
				self.move_backward(time)
				print('backward')
		else:
			self.stop_moving(time)
			print('stopped')