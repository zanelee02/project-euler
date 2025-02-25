# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# model day of week as number 0-6
# 0 = Sunday
# 1 = Monday
# ...
# 6 = Saturday

# leap year is divisible 4 but not a century (unless a 400 century)
def is_leap_year(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

# Testing
# assert is_leap_year(1) == False
# assert is_leap_year(1900) == False
# assert is_leap_year(1904) == True
# assert is_leap_year(2000) == True

# get array of counts of days in months based on if it is a leap year or not
leap_year_day_counts = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
reg_year_day_counts = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# returns the count of days per month for a given year. Accounnts for leap years
def get_days_for_year(year):
    if is_leap_year(year):
        return leap_year_day_counts
    return reg_year_day_counts

# go through year. Starting on Jan 1, determine if it is a Sunday (day_of_week % 7 == 0)
# and increment count if so. Add number of days in current month and repeat.

def count_sundays_on_first_of_month(starting_day, monthly_day_counts):
    count = 0
    curr_day_of_week = starting_day
    for i in range(len(monthly_day_counts)):
        if curr_day_of_week % 7 == 0 :
            count = count + 1
        curr_day_of_week = (curr_day_of_week + monthly_day_counts[i]) % 7
    return count, curr_day_of_week

# Testing
# Year 1900- 2 Sunday the 1st
# January 1, 1900 is a Monday(1)
# January 1, 1901 is a Tuesday (2)
# count_sundays, ending_day = count_sundays_on_first_of_month(1, get_days_for_year(1900))
# assert count_sundays == 2
# assert ending_day == 2

# Loop through years in range
start_year = 1901
start_day = 2 # Tuesday
end_year = 2000

def count_sundays_on_first_of_month_in_year_range(starting_day, starting_year, ending_year):
    count = 0
    curr_day = starting_day
    curr_year = starting_year
    while curr_year <= ending_year:
        curr_count, new_day = count_sundays_on_first_of_month(curr_day, get_days_for_year(curr_year))
        count = count + curr_count
        curr_day = new_day 
        curr_year = curr_year + 1
    return count

res = count_sundays_on_first_of_month_in_year_range(start_day, start_year, end_year)
print(f'Sundays on 1st of month in 20th century: {res}')
