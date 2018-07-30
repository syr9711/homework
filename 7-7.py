def fahrenheit_to_celsius(fahrenheit):
    calcius=(fahrenheit-32)*5/9
    return(calcius)

sample_temperature_list=[40,15,32,64,-4,11]

print("화씨온도 리스트:"+str(sample_temperature_list))

i=0
while i<len(sample_temperature_list):
    result=float(fahrenheit_to_celsius(sample_temperature_list[i]))
    result=round(result,2)
    sample_temperature_list[i]=result

    i=i+1

print("섭씨 온도 리스트:"+str(sample_temperature_list))