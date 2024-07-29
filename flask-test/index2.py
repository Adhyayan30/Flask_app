import importlib
from Test_Model import predictions

importlib.reload(predictions)

print(predictions.detect_in_image("test image.jpg"))