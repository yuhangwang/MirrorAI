Follow this tutorial for installing OpenCV 3.2 with
Miniconda/python3.5.

https://www.solarianprogrammer.com/2016/09/17/install-opencv-3-with-python-3-on-windows/

This tutorial uses the binary from http://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv

I downloaded: opencv_python‑3.2.0‑cp35‑cp35m‑win_amd64.whl.

I got this error when importing openCV
```
>>> import cv2
ImportError: numpy.core.multiarray failed to import
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: numpy.core.multiarray failed to import
```
According to this stackoverflow post,
I have to upgrade my numpy
http://stackoverflow.com/questions/28157976/importing-opencv-and-getting-numpy-core-multiarray-failed-to-import .
To fix this, I had to do
```
conda upgrade numpy
```
Then everything was fine.

Installation verification:
```
import cv2

image = cv2.imread("clouds.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Over the clouds", image)
cv2.imshow("Over the clouds - gray", gray_image)
cv2.waitKey(0)
cv2.destroyAllwindows()
```
The first time I did this, I mistyped the 
file name and got the error:
```
File ".\try.py", line 4, in <module>
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.error: D:\Build\OpenCV\opencv-3.2.0\modules\imgproc\src\color.cpp:9748: error: (-215) scn == 3 || scn == 4 in function cv::cvtColor
```

According to this post, the reason is that
I have to type the correct file path
http://stackoverflow.com/questions/30506126/open-cv-error-215-scn-3-scn-4-in-function-cvtcolor

Everything works after fixing the file name,
no need to type full file path.
