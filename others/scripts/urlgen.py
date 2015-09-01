__author__ = 'HaoBin'
# A script for downloading LICD comics
# Generates list of URLs based on wordpress content link formats

import urllib.request
import datetime
import time
import os


def urlgen():
    print("Custom URL downloader script")
    s_year = int(input("Starting year: "))
    s_mon = int(input("Starting month: "))
    s_day = int(input("Starting day: "))
    url_base = str(input("Base URL: "))
    ext = str(input("Extension: "))
    # example: abc.com/wp-content/uploads/
    slash = "/"
    ext = ".gif"
    urls = []
    m31 = [1,3,5,7,8,10,12]
    m30 = [1,4,6,9,11]
    monmax = 31

    for year in range(s_year, 2015):

        if year == s_year:
            for month in range(s_mon,13):
                if month == s_mon:
                    for day in range(s_day,32):
                        urls.append(url_base + str(year) + slash + str(month).zfill(2) + slash + \
                              str(year) + str(month).zfill(2) + str(day).zfill(2) + ext)
                else:
                    if month in m31:
                        monmax = 31 + 1
                    elif month in m30:
                        monmax = 30 + 1
                    else:
                        if month == 2:
                            if leap_year(year) == 1:
                                monmax = 29 + 1
                            elif leap_year(year) == 0:
                                monmax = 28 + 1
                            else:
                                monmax = 28 + 1

                    for day in range(1, monmax):
                        urls.append(url_base + str(year) + slash + str(month).zfill(2) + slash + \
                              str(year) + str(month).zfill(2) + str(day).zfill(2) + ext)
        else:
            for month in range(1,13):

                #check how many days in that month
                if month in m31:
                    monmax = 31 + 1
                elif month in m30:
                    monmax = 30 + 1
                else:
                    if month == 2:
                        if leap_year(year) == 1:
                            monmax = 29 + 1
                        elif leap_year(year) == 0:
                            monmax = 28 + 1
                        else:
                            monmax = 28 + 1

                for day in range(1, monmax):
                    if year == datetime.date.today().year:
                        if month == datetime.date.today().month:
                            if day > datetime.date.today().day:
                                break
                        elif month > datetime.date.today().month:
                            break
                    urls.append(url_base + str(year) + slash + str(month).zfill(2) + slash + \
                              str(year) + str(month).zfill(2) + str(day).zfill(2) + ext)

    i = 0
    for url in urls:

        filepath = "/Users/HaoBin/Downloads/tmp/" + str(url[-12:-8]) + "/"
        if not os.path.exists(filepath):
            os.makedirs(filepath)
        filename = str(url[-12:])
        final_file = filepath + filename

        i += 1
        progress = str(int(i / len(urls) * 100))
        print(">>> " + progress + "% - Downloading " + filename, end='\r')
        try:
            urllib.request.urlretrieve(url, final_file)
        except:
            print("HTTPError: " + filename)
        time.sleep(0.005)

    print("Files downloaded at /Users/HaoBin/Downloads/tmp/")
    #initialising file
    file = open('urlgen.txt', 'w')
    file.write('URL\n')
    file.close()

    file = open('urlgen.txt', 'a')
    for item in urls:
        file.write(str(item) + '\n')
    file.close()
    print("URLs generated in urlgen.txt")


def leap_year(y):
        """
        @purpose Returns whether the year is leap year or not
        @param y: the year to test for leap year
        @complexity:
            Best Case: O(2): When user input a year before 1582
            Worst Case: O(7): When user enter a year after 1582
        @precondition Passing a valid year in integer/numerical
        @postcondition Return whether the year is leap or not
        """
        if y >= 1582:
            if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
                return 1
            else:
                return 0
        else:
            return -1


try:
    urlgen()
except KeyboardInterrupt:
    print("User interrupted.")
