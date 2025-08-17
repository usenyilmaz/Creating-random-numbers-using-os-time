import datetime

def generaterandomwithsystemtime(min, max):
    current_time = datetime.datetime.now()
    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    num1 = hour % 10
    num2 = hour // 10
    num3 = minute % 10
    num4 = minute // 10
    num5 = second % 10
    num6 = second // 10

    if(num1 == 0):
        num1 = 1
    if(num2 == 0):
        num2 = 1
    if(num3 == 0):
        num3 = 1
    if(num4 == 0):
        num4 = 1
    if(num5 == 0):
        num5 = 1
    if(num6 == 0):
        num6 = 1
    
    product = num1 * num2 * num3 * num4 * num5 * num6

    if(max > min):
        possible_number_count = max - min + 1
        modulus = product % possible_number_count
        return min + modulus

    else:
        #else bloğunda value error fırlatılacak
        raise ValueError("max must be greater than min")


print("random number: ", generaterandomwithsystemtime(17, 23))

#eğer possible_number_count değişkeni asal sayılara eşitse algoritma randomness a yaklaşabiliyor
#fakat  possible_number_count küçük bir sayıysa product değişkeni büyük ihtimalle bu sayıya tam bölündüğünden randomness  tan sapıyor, ve modulus 0 geleceğinden minimum sayıyı dönğyor.
# possible_number_count değişkeni bğyğk bir asal sayıysa kullanılabilir