# from pytz import timezone
# import pandas as pd
#
# def tz_diff(date, tz1, tz2):
#     '''
#     Returns the difference in hours between timezone1 and timezone2
#     for a given date.
#     '''
#     date = pd.to_datetime(date)
#     return (tz1.localize(date) -
#             tz2.localize(date).astimezone(tz1))\
#             .seconds/3600
#
#
# # Complete the time_delta function below.
# def time_delta(t1, t2):
#     pass
#
#
# t = int(input())
#
# for t_itr in range(t):
#     t1 = input()
#     t2 = input()
#     delta = tz_diff()

import datetime

format_string = "%a %d %b %Y %H:%M:%S %z"
T = int(input())

for test in range(T):
    t1 = input()
    t2 = input()

    parsed_t1 = datetime.datetime.strptime(t1, format_string)
    parsed_t2 = datetime.datetime.strptime(t2, format_string)

    diff = parsed_t2 - parsed_t1

    print(int(abs(diff.total_seconds())))


