small_size= int(input("How big is the small pizza? "))
xsmall= int(input("How many small pizzas are you buying? "))
small_price= float(input("How much does the small pizza cost? "))

large_size= int(input("How big is the large pizza? "))
xlarge= int(input("How many large pizzas are you buying? "))
large_price= float(input("How much does the large pizza cost? "))

small_area= (3.14*(small_size/2)**2.0)* xsmall
large_area= (3.14*(large_size/2)**2.0)* xlarge

print("Your small pizza is", small_area)
print("Your large pizza is", large_area)

print("The small pizza costs", small_area/small_price, "per square inch")
print("The large pizza costs", large_area/large_price, "per square inch")

if small_area < large_area:
    print("The large pizza is a better deal")
else:
    print("The small pizza is a better deal")
    
