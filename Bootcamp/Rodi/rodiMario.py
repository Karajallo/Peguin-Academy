import rodi
import time
import keyboard

robot= rodi.RoDI() #instanciamoms un objeto RoDi

'''
robot.move_forward()
time.sleep(1.0)

robot.move_backward()
time.sleep(1.0)

robot.move_left()
time.sleep(1.0)

robot.move_right()
time.sleep(1.0)

robot.move_stop() #paramos el robot

'''

'''
desafio: utilizando los metodos de movimiento de RoDI, hacer que el robot "dibuje" con su trayectoria
'''
'''
for i in range (4):
    robot.move_forward()
    time.sleep(1)
    robot.move_left()
    time.sleep(0.5)
robot.move_stop()
'''
##leemos el sensor de distancia
#while True:
#   print(robot.see())
#   time.sleep(0.1)

#desafio: esquivar obstaculo. 
'''
while True:
    robot.move_forward()
    time.sleep(1)
    print(robot.see())
    if robot.see() < 5:
        robot.move_right()
        time.sleep(0.5)
        print(robot.see())
'''
#sumofight

while True:
    if keyboard.is_pressed('j'): 
        print('tecla j')
        robot.move_forward()
    elif keyboard.is_pressed('u'): 
        print('tecla u')
        robot.move_backward()
        
        
    elif keyboard.is_pressed('h'): 
        print('tecla h')
        robot.move_left()
        
        
    elif keyboard.is_pressed('k'): 
        print('tecla k')
        robot.move_right()