import cv2
import numpy 
import signal
import math

img = cv2.imread('F:\MiguelGIT\PythonWorkspace\TEST_IMAGE\lunar.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = numpy.array(img)
img = numpy.flipud(img)
sub = img[450:550,600:700]

img = img - numpy.mean(img)
sub = sub - numpy.mean(sub)

sub = numpy.flipud(numpy.fliplr(sub))
numerator = signal.fftconvolve(img, sub, 'valid')

one = numpy.ones(sub.shape)
sigma1 = sqrt(signal.fftconvolve(img*img, one, 'valid'))
sigma2 = sqrt(numpy.sum(sub*sub))
denominator = sigma1*sigma2

correlation = numerator/denominator
found = numpy.where(correlation==numpy.amax(correlation))
print('maximum correlation found in (x,y)=(%d,%d)'%(found[1],found[0]))