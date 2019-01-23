sum_kasia = 0
sum_stasia = 0
iterate = 20
for i in range(1,31):
    if(i == 1):
        sum_kasia = iterate
        print("Dzien: " + str(i) + ", Kasia: " + str(sum_kasia))
    elif(i % 2 == 0):
        iterate = iterate * 1.05
        sum_stasia += iterate
        print("Dzien: " + str(i) + ", Stasia: " + str(sum_stasia) + " Iterate: " + str(iterate))
    elif(i % 1 == 0):
        iterate = iterate * 1.05
        sum_stasia += iterate
        print("Dzien: " + str(i) + ", Kasia: " + str(sum_kasia) + " Iterate: " + str(iterate))
