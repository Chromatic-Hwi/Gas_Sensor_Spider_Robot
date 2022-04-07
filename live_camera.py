#taking shot n save program

import picamera
#import time
#import datetime

def record():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        #now = datetime.datetime.now()
        #filename = now.starftime('%Y-%m-%d %H:%M:%S')
        filename = 'live_video'
        camera.start_recording(output = filename + '.mpeg')
        camera.wait_recording(1)
        camera.stop_recording()
        
while True:
    record()
    
#raspivid -o video.mp4 -t 10000 -d
    # this code run well, captured the video
#omxplayer video.mp4
    # play checked through this player
