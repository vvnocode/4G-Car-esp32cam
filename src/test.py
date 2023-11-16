import servos
import time

for i in range(180):
    servos.s_sg90.set_angle(i)
    time.sleep_ms(100)
