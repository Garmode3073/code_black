import cv2
import numpy as np
import requests
import io
import json

img=cv2.imread("hey1.jpg")
url_api="https://api.ocr.space/parse/image"
url_conv="https://api.cloudconvert.com/v2/jobs"
contracted=requests.post(url_conv, files={"hey1.jpg": 90},
              data={"apikey":"eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjdkMDFlYmYzOWM3NWU1NGVkZjk3MzY0MmFmNDc5NDEzYzUxOTk1ZTA5ODhhMmZkNzhjZDMyM2RkY2I2NmM2YWU5ZTNkODc4ZWZiODVmNDAyIn0.eyJhdWQiOiIxIiwianRpIjoiN2QwMWViZjM5Yzc1ZTU0ZWRmOTczNjQyYWY0Nzk0MTNjNTE5OTVlMDk4OGEyZmQ3OGNkMzIzZGRjYjY2YzZhZTllM2Q4NzhlZmI4NWY0MDIiLCJpYXQiOjE1ODM1NjgwODAsIm5iZiI6MTU4MzU2ODA4MCwiZXhwIjo0NzM5MjQxNjgwLCJzdWIiOiI0MDY2NjQxMyIsInNjb3BlcyI6WyJ1c2VyLnJlYWQiLCJ1c2VyLndyaXRlIiwidGFzay5yZWFkIiwidGFzay53cml0ZSIsInByZXNldC5yZWFkIiwicHJlc2V0LndyaXRlIiwid2ViaG9vay53cml0ZSIsIndlYmhvb2sucmVhZCJdfQ.gyMzqPtALQteLJyXvsdy_g4MfVrtszc5lG43T1F3hc1HnshcwCibhGRSbYxd2XCDHeFxOVMH3Qtd9k3aSonnqGYJGk3QzxUZ6EPgyavfRoJjCVmjgCLRApgN0u-OJAxMS5ZQhmDXcLkiqNGtwQadMDHbAn9Db0L7VTt4W_40C8kWEohzS09w5mUSvp3gPY_0A9YtGOCoF1DvSyqdmVaMRQvYmR6E0yJyoHM7f7I-flZzs9gYQVhzSTJne4ydJc6iI0Huqu7Ny1Cl8iH1Qn23FxpwqvnrDRIESrR5pEUjw2j8CjIQ33cQ-L5YkqA9XZgdBSSca2ysDeQytZbjRcDWwlH5ysn4romtlFX4Q4V-uu80iRCc5CGV4uN36VJt501c2jDJs26z8Of-4-ooTjAdQCd7ojtfN-O7I54sbS7C0xBQqox_t8euVNHLxFgyAJB3uhFJuYGCPHFuZCE7hD8a_xRoCUgATqyZH9UT7fn2G4m1jlKvOeIDujdFxbtkzs0f4YYQiIf6hAtRbmYuedZWc6vyIYF9M99Fr87OkxtD7bQYm3Mi1FKc7XQpuytwkGI_5bczy3dUoN59OGLBVqwq0Eewqpp498W8Ax05gWI5Ezbui5qUW-jyNxU6vFL2XhSEmvFzn0trNp4qvRju0VfT9yd8H2rso6YhbJ1XOiI3KWk"}
             )
_, compressedimage=cv2.imencode(".jpg",img, [1,90])
file_bytes=io.BytesIO(compressedimage)
result=requests.post(url_api, files={"hey1.jpg": file_bytes},
              data={"apikey":"f581fd256b88957"}
             )
result=result.content.decode()
result=json.loads(result)

text_detected=result.get("ParsedResults")[0]
text_detected=text_detected.get('ParsedText')
print(result)
cv2.imshow("Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
