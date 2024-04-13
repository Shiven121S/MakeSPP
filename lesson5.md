# Ultrasonic Sensors

**These last two lessons are a bit more difficult then what you’re done previously.**

**To start this lesson, we need to explain the ultrasonic sensor.**

<img title="a title" alt="Alt text" src="[https://lh7-us.googleusercontent.com/6p7tP_1HyXoNyM65Sxsb2OWF-PQqqgXWTJH55BTO0WaETV3NpaIxrzDdC9bcOy5ClmVyTl-d8SsHxw9pitL02fmrfDiMzsvNsZFMgs5ST_gDdxmKJ48lu9QwxeZUnw13qK9y5I519NnyQ2zaea50x3I](https://lh7-us.googleusercontent.com/CtgB-4XcvcBUdRwumFc5lZzoaOTZLBDAiVMQf99tAsCabkK7Jyu_alfFJeY7oX70eM3uAqQLy2SlXiYCgTbLS06whgwRsLpGrNt-JvKNvRcSyWxoU5wYXjOVMOVDpcxyFNjp-jXypqp6UmGB8fbvdLo)">


**Interestingly, most ultrasonic sensors have 4 pins instead of 3, with the signal pin on the right being an echo pin and a trigger pin.**

**The ultrasonic sensor works by detecting objects directly ahead of it, which has the real world applications of tech such as motion sensors.**

<img title="a title" alt="Alt text" src="[https://lh7-us.googleusercontent.com/6p7tP_1HyXoNyM65Sxsb2OWF-PQqqgXWTJH55BTO0WaETV3NpaIxrzDdC9bcOy5ClmVyTl-d8SsHxw9pitL02fmrfDiMzsvNsZFMgs5ST_gDdxmKJ48lu9QwxeZUnw13qK9y5I519NnyQ2zaea50x3I](https://lh7-us.googleusercontent.com/QGpg8HLBGaM-PUsYQDn8qXiJxbncaj61fM0eN2L0eUvPYaJTyi4y_dCXqKCm41zu7S3xn9IEzWy5Dw60y3eArS7xWQ74OrLy1586G5_xzWod9mtj5p3Z4zBnIpNX4dDe9IPydowFO45rOXCuqGluCDg)">

**You can use this code for the following challenge. It works by turning the trigger pin on and off really quickly and measuring the distance of the closest object from the sensor in the direction of the “eyes”.**

**Challenge 5:**

**For Challenge 5, have the readings of an ultrasonic sensor control an RGB light, with red corresponding to a long distance, green for a medium distance, and blue for a short distance. Use pin 2 for red, 3 for green, 4 for blue. If distance is greater than 50, display red, if less than 50 but greater than 20 display green, otherwise display blue.**
