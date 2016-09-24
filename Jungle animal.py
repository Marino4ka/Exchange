def jungle_animal(animal, my_speed):
    if animal == 'zebra':
        result = "Try to ride a zebra!"
    if animal == 'cheetah' and my_speed > 115:
        result = "Run!"
    if animal == 'cheetah' and my_speed < 115:
        result = "Stay calm and wait!"
    else:
        result = "Introduce yourself!"
    print (result)

jungle_animal('zebra', 21)