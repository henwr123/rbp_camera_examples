from picamera import PiCamera, Color
from time import sleep

camera = PiCamera()

camera.start_preview()


for i in range(5):
    sleep(5)
    camera.annotate_text = 'Hello World'
    camera.annotate_foreground = Color('yellow')
    camera.capture('image%s.png' % i)

camera.start_recording('video.h264')
sleep(10)
camera.stop_recording()

camera.stop_preview()
