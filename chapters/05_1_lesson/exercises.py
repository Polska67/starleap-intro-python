
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

# Do your work for Exercise 3 here.

print("Ch 5 Exercise 3: Not implemented") # Delete this line when you write your code!



print("********** Ch 5 Exercise 4 **********")

# Do your work for Exercise 4 here.

print("Ch 5 Exercise 4: Not implemented") # Delete this line when you write your code!
