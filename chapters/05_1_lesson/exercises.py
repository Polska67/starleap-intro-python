
##### Template for Chapter 5.14, Exercises 1 - 4 ######


print("********** Ch 5 Exercise 1 **********")

def time_since_epoch():
    import time 
    seconds_per_day = 60 * 60 * 24
    seconds_per_hour = 60 * 60
    seconds_per_minute = 60

    t = time.time()
    print("t = ", t)
    days = int(t / seconds_per_day)
    print("days = ", days)
    remainder = t % (days * 60 * 60 * 24)
    print("remainder = ", remainder)
    hours = int(remainder / seconds_per_hour)
    print("hours = ", hours)



time_since_epoch()


print("Ch 5 Exercise 1: Not implemented") # Delete this line when you write your code!



print("********** Ch 5 Exercise 2 **********")

# Do your work for Excercise 2 here.

print("Ch 5 Exercise 2: Not implemented") # Delete this line when you write your code!



print("********** Ch 5 Exercise 3 **********")

def is_triangle(a, b, c):
    print('is_triangle()', a, b, c)
    if a >= b + c:
        print('No')
    elif b >= a + c:
        print('No')
    elif c >= a + b:
        print('No')
    else:
        print("Yes")

is_triangle(3, 4, 5)
is_triangle(2, 1, 1)
is_triangle(0, 0, 0)

# ask user for input - 3 sides of sticks
# then print out whether it's a triangle

a = float(input('How long is side a? '))
print('a is', a, type (a))
b = float(input('How long is side b? '))
print('b is', a, type (b))
c = float(input('How long is side c? '))
print('c is', a, type (c))

is_triangle(a, b, c)



print("Ch 5 Exercise 3: Not implemented") # Delete this line when you write your code!



print("********** Ch 5 Exercise 4 **********")

answer = "oh my god real spiderman"
print(answer)


print("Ch 5 Exercise 4: Not implemented") # Delete this line when you write your code!
