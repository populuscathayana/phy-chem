S = 10000000
def product_of_numbers(*args, d):
    result = 1
    for num in args:
        result *= (S/4 - num) / (S/4 + int((S*abs(1-2*d))/4) - num)
    return result

p = [0.49, 0.499, 0.4999,0.49999,0.50,0.50001, 0.5001, 0.501, 0.51]

result = {}
for i in p:
    numbers = range(1, int((S*abs(1-2*i)/4))+1)
    result[i] = product_of_numbers(*numbers, d=i)
print("The product is:", result)

#49%，49.9%， 49.99%，49.999%，50.001%，50.01%，50.1%，51%
#The product is: {0.49: 1.2e-322, 0.499: 4.5399536297454e-05, 0.4999: 0.9051990446898273, 0.49999: 0.9990004996335086, 0.5: 1, 0.50001: 0.9990400608445181, 0.5001: 0.9051990446898273, 0.501: 4.5399536297454e-05, 0.51: 1.2e-322}


