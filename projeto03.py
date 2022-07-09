# input speed
# compare speed to 80km/h
# if speed > 80 && <= 90
#   print "light ticket!"
# elif speed > 90 && <= 100
#   print "heavy ticket!"
# elif speed > 100
#   print "License suspended!"
# else
#   print "no infringement."

maxSpeed = 80
speed = int(input("Digite a velociade: "))

if speed > maxSpeed and speed <= maxSpeed + 10:
    print("Light ticket.")
elif speed > maxSpeed + 10 and speed <= maxSpeed + 20:
    print("Heavy ticket!")
elif speed > maxSpeed + 20:
    print("License suspended!")
else:
    print("No infringement.")