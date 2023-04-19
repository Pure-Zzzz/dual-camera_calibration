# dual-camera_calibration
calibrate dual-camera by using opencv,python

## Need
1.chess board pattern print on a4 paper  https://github.com/opencv/opencv/blob/4.x/doc/pattern.png  
2.a dual camera  
![Snipaste_2023-04-18_21-08-28](https://user-images.githubusercontent.com/73814732/232944214-3400c4c0-6d4b-460d-98f2-9fb6352acff0.png)

## testing camera
runnning cam_test.py ensure camera is working
![snipast](https://user-images.githubusercontent.com/73814732/232943352-44106e72-8f68-4c8f-9c77-c03eade96a1a.png)
## preparing chess_board pattern and print it on A4 paper
Download below  
https://github.com/opencv/opencv/blob/4.x/doc/pattern.png  
or generate your own pattern  
https://docs.opencv.org/4.x/da/d0d/tutorial_camera_calibration_pattern.html
![0](https://user-images.githubusercontent.com/73814732/232944358-59e13861-ab45-40da-bcf7-137107eadf44.jpg)
## take photo
using take_photo.py to get photos  
press SPACE to save image  
run get_corner.py to check  
![Snipaste_2023-04-18_22-06-07](https://user-images.githubusercontent.com/73814732/232944882-9a0cdaec-66f9-4753-9739-9aa120068b4a.png)
## Intrinsics & Extrinsics
run gpt_get_mywrite.py to get  
![Snipaste_2023-04-18_22-10-32](https://user-images.githubusercontent.com/73814732/232945120-80a1d757-27e6-49ea-98e6-f8f85615936a.png)  
copy and replace in calibration_final.py run to get result  
![Snipaste_2023-04-19_09-48-48](https://user-images.githubusercontent.com/73814732/232945603-3b5086b9-75ed-4fbc-a46d-1e09d5c48b69.png)
