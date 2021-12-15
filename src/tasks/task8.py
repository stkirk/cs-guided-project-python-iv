# Given a number...
# determine whether the number has 3, 5, and/or 7 as a factor
# if it does, add the corresponding raindrop sound string to the result
# 3 is a factor, add "Pling"
# 5 is a fact, add "Plang"
# 7 is a factor, add "Plong"
# none of the above is a factor, return the input as a str

def csRaindrop(number):
    rain_sound = ""
    if number % 3 == 0:
        rain_sound += "Pling"
    if number % 5 == 0:
        rain_sound += "Plang"
    if number % 7 == 0:
        rain_sound += "Plong"
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        rain_sound = str(number)
    return rain_sound


print(csRaindrop(28)) #--> "Plong"
print(csRaindrop(30)) #--> "PlingPlang"
print(csRaindrop(34)) #--> "34"