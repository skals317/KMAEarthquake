import requests, json

eq = "https://ska1001api.run.goorm.io/api/korearecent"  #한국 지진정보 API 불러오기

response = requests.get(eq)
message = response.text
data = json.loads(message)

status = response.status_code

if status == 200:# 지진정보가 정상적으로 불러와졌을경우
    if str(data["micro"] = "True"):
        print("한국 최근 미소지진정보")
    else :
        print("한국 최근 지진정보")
    print("번호 : "+str(data["occurnum"]))
    print("발생시각 : "+str(data["time"]))
    print("규모 : "+str(data["magnitude"]))
    print("깊이 : "+str(data["depth"]))
    print("최대진도 : "+str(data["jindo"]))
    print("발생지역 : "+str(data["place"]))
    print("위도 : "+str(data["lat"]))
    print("경도 : "+str(data["lon"]))
    print("지도 : "+str(data["map"]))
else :
    print("오류코드 : "+str(status))
