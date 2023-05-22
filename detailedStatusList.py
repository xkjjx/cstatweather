import pyowm

weatherKey = "b3727fa4b9513a107515a372ba389731"
detailedStatuses = []

for i in range(-85,85,5):
    for j  in range(-175,175,5):
        detailedStatus = pyowm.OWM(weatherKey).weather_manager().weather_at_coords(i,j).weather.detailed_status
        if detailedStatus not in detailedStatuses:
            detailedStatuses.append(detailedStatus)
            print((detailedStatus))
            print(i,j)


print(detailedStatuses)

with open("detailedStatusList.txt","w") as outP:
    for status in detailedStatuses:
        outP.write(status + "\n")

