###1. IP CAMERA CONTROL USING PYTHON – VIA sensecam_control
##Readme : https://pypi.org/project/sensecam-control/
from sensecam_control import onvif_control

Camera1 = onvif_control.CameraControl('192.168.1.2', 'foscamr2', 'foscamr2')
Camera1.camera_start ()
Camera1.go_home_position()
#Camera1.absolute_move(-1, 0.0, 0.0)
#Camera1.absolute_move(1, 0.0, 0.0)
#Camera1.continuous_move(0.5, 0.0, 0.0)
#Camera1.absolute_move(0, 0.0,1)

#Camera1.camera_start ()
#Camera1.relative_move(-0.5,0,0)

# ###2. IP CAMERA CONTROL USING PYTHON – VIA ONVIF
# ###Readme : https://carlrowan.wordpress.com/2018/12/23/ip-camera-control-using-python-via-onvif-for-opencv-image-processing/
# from time import sleep 
# from onvif import ONVIFCamera
 
# XMAX = 1
# XMIN = -1
# YMAX = 1
# YMIN = -1
 
# def perform_move(ptz, request, timeout):
#   # Start continuous move
#   ptz.ContinuousMove(request)
#   # Wait a certain time
#   sleep(timeout)
#   request.PanTilt = 1
#   # Stop continuous move
#   ptz.Stop(request)#{'ProfileToken': request.ProfileToken})
 
# def move_up(ptz, request, timeout=2):
#   print ('move up...')
#   request.Velocity.PanTilt._x = 0
#   request.Velocity.PanTilt._y = YMAX
#   perform_move(ptz, request, timeout)
 
# def move_down(ptz, request, timeout=2):
#   print ('move down...')
#   request.Velocity.PanTilt._x = 0
#   request.Velocity.PanTilt._y = YMIN
#   perform_move(ptz, request, timeout)
 
# def move_right(ptz, request, timeout=2):
#   print ('move right...')
#   request.Velocity.PanTilt._x = XMAX
#   request.Velocity.PanTilt._y = 0
#   perform_move(ptz, request, timeout)
 
# def move_left(ptz, request, timeout=2):
#   print ('move left...')
#   request.Velocity.PanTilt._x = XMIN
#   request.Velocity.PanTilt._y = 0
#   perform_move(ptz, request, timeout)
 
# def continuous_move():
#   mycam = ONVIFCamera('192.168.1.30', 8080, 'admin', 'admin')
#   # Create media service object
#   media = mycam.create_media_service()
#   # Create ptz service object
#   ptz = mycam.create_ptz_service()
 
#   # Get target profile
#   media_profile = media.GetProfiles()[0];
#   print (media_profile)
 
#   # Get PTZ configuration options for getting continuous move range
#   request = ptz.create_type('GetConfigurationOptions')
#   request.ConfigurationToken = media_profile.PTZConfiguration._token
#   ptz_configuration_options = ptz.GetConfigurationOptions(request)
 
#   request = ptz.create_type('ContinuousMove')
#   request.ProfileToken = media_profile._token
 
#   # ptz.Stop({'ProfileToken': media_profile._token})
 
#   # Get range of pan and tilt
#   # NOTE: X and Y are velocity vector
#   global XMAX, XMIN, YMAX, YMIN
#   XMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Max
#   XMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].XRange.Min
#   YMAX = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Max
#   YMIN = ptz_configuration_options.Spaces.ContinuousPanTiltVelocitySpace[0].YRange.Min
 
#   # move right
#   move_right(ptz, request)
 
#   # move left
#   move_left(ptz, request)
 
#   # Move up
#   move_up(ptz, request)
 
#   # move down
#   move_down(ptz, request)
 
# if __name__ == '__main__':
#   continuous_move()


