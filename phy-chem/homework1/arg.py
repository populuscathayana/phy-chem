S = 1000
def product_of_numbers(*args, d):
    result = 1
    for num in args:
        result *= (S/4 - num) / (S/4 + int((S*abs(1-2*d))/4) - num)
    return result

p = [0.45, 0.47, 0.49, 0.495,0.50, 0.505, 0.51, 0.53, 0.55]

result = {}
for i in p:
    numbers = range(1, int((S*abs(1-2*i)/4))+1)
    result[i] = product_of_numbers(*numbers, d=i)
print("The product is:", result)

#45%，47%， 49%，49.5%, 50%, 50.5%，51%，53%，55%
#The product is: {0.45: 0.0813320334147723, 0.47: 0.40561678859448674, 0.49: 0.9046501591282005, 0.495: 0.9840956175298805, 0.5: 1, 0.505: 0.9840956175298805, 0.51: 0.9046501591282005, 0.53: 0.40561678859448674, 0.5501: 0.0813320334147723