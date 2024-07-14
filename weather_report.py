import random

temperatures = []
days_of_the_week=["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
good_days_count = 0
highest_temp_day = ""
highest_temp = 0
lowest_temp_day = ""
lowest_temp = 50
sum_temp = 0
avg_temp = 0
above_avg = []

#getting the temperatures
for i in range(7):
	temperatures.append(random.randint(26,41))

#getting the good days count
for i in range(7):
	if temperatures[i] % 2 == 0:
		good_days_count = good_days_count + 1

#finding the highest and lowest temperatures
for i in range(7):
	if temperatures[i] > highest_temp:
		highest_temp = temperatures[i]
		highest_temp_day = days_of_the_week[i]

	if temperatures[i] < lowest_temp:
		lowest_temp = temperatures[i]
		lowest_temp_day = days_of_the_week[i]

#getting the temperatures above the average
for i in range(7):
	sum_temp += temperatures[i]

avg_temp = float(sum_temp) / 7.0
#getting the temperatures that are above the average
for i in range(7):
	if temperatures[i] > avg_temp:
		above_avg.append(days_of_the_week[i])

print("The weather report:")
for i in range(7):
	print(f"    {days_of_the_week[i]}:{temperatures[i]}")
print("*")
print("*")
print(f"shelly had {good_days_count} good days")
print("*")
print("*")
print(f"the hottest temperature was: {highest_temp} on {highest_temp_day}")
print(f"the lowest was: {lowest_temp} on {lowest_temp_day}")
print("*")
print("*")
print(f"the average temperature was: {avg_temp}")
print(f"the days with above average temperature: {above_avg}")


