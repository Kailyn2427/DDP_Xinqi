"""
Date Scheduler Function

Objective:
Write a function named 'date_passed' to determine the relationship between two dates.

Function Parameters:
1. todays_date (string): The current date in the format 'day Month'.
2. scheduled_date (string): The scheduled date to compare, in the same format.

Instructions:
- The function should compare todays_date and scheduled_date and print whether the scheduled date has passed, is yet to pass, or is today.
- Assume the dates are in the same year.
- The dates are in a format like '26th March'. Consider how to convert these for comparison.
- https://www.w3schools.com/python/python_datetime.asp

Example Test Cases:
1. date_passed('26th March', '25th March') should indicate that the scheduled date has passed.
2. date_passed('26th March', '26th March') should indicate that the scheduled date is today.
3. date_passed('26th March', '27th March') should indicate that the scheduled date is yet to pass.
"""
import datetime


def date_passed(todays_date, scheduled_date):
    # Convert the dates to datetime objects; %d means day& "th" is the Abbreviation of date;%B is the full name of the month
    todays_datetime = datetime.datetime.strptime(todays_date, "%dth %B")
    scheduled_datetime = datetime.datetime.strptime(scheduled_date, "%dth %B")

    # Compare the dates
    if todays_datetime > scheduled_datetime:
        print("Scheduled date has passed")
    elif todays_datetime < scheduled_datetime:
        print("Scheduled date is yet to pass")
    else:
        print("Scheduled date is today")

    # x2 = datetime.datetime(x1, 5, 17)
    # Your code goes here
    # Implement the logic to compare the dates and print the appropriate message
    # pass  # Delete this after implementing some code inside this function


# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
