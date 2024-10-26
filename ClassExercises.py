#Program1 Name and Welcome

name = input("Enter your name: ")
print(name)

wc= "Welcome"
print(wc, name)

#Program2 Hours and rate per hours to compute gross pay (gp = h*rph)

user_hours=float(input("How many hours did you work for? "))
rate_ph = float(input(" Per hours: "))

gp= user_hours * rate_ph
print("Gross pay",gp)

#Program3 Width and Height

width=17
height=12.0
a=width//2
b=width/2.0
c=height/3
print("Value of Width//2 is " "'" ,a ,"'" )
print("Value of Width/2.0 is " "'" ,b ,"'" )
print("Value of Height/3 is " "'" ,c,"'" )

#Program4 Celsius Temprature covert Fahreheit

Celsius = float(input("Enter your Celsius: "))
Fahrenheit = (Celsius * 1.8) + 32
print(Fahrenheit)



