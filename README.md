# Simple image perspective transformation
# Простая трансформация перспективы фотографии

Dependencies: cv2, numpy ,matplotlib, sys

*change ***./myPhoto.jpg*** to your image location     
Usage: 
```
python main.py ./myPhoto.jpg 
```

Then:
1) Press "q" button when you're done
2) Press  "1/2/3/4" button to select corresponding vertex to be changed
3) Press on image part to change vertex location

On init (right side is transformed part of image): 
<br />
<br />
<img width="1440" alt="Screenshot 2023-08-17 at 01 42 06" src="https://github.com/vilgeforc5/image-perspective-transformation/assets/57109127/5680c8f5-aeb1-4f21-88f3-825ff8ceb66a">
<br />
<br />
On result (vertex is green because I selected it. Right image is transformed part of origin):
<br />
<img width="1440" alt="Screenshot 2023-08-17 at 01 42 40" src="https://github.com/vilgeforc5/image-perspective-transformation/assets/57109127/15eda0a8-cb9d-481c-b058-c8a11cd0f652">

