'''Xử lý JSON File, Chuyển đổi Python Object qua String Json
Yêu cầu:
Cho Python Object có cấu trúc sau:
pythonObject = {
 "ten": "Trần Duy Thanh",
 "tuoi": 50,
 "ma": "nv1"
}
Hãy viết mã lệnh chuyển đổi qua String json.
'''
import json
pythonObject = {
 "ten": "Trần Duy Thanh",
 "tuoi": 50,
 "ma": "nv1"
}
jsonString = json.dumps(pythonObject)
# the result is a JSON string:
print(jsonString)