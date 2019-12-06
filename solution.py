import time
import pandas as pd
import numpy as np
import statistics as st

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    #SELECT CITY
    city = input('\nwich city you want to see data for? (Chicago), (New York), or (Washington) ?\n').lower()
    while(True):
        if(city == 'chicago' or city == 'new york' or city == 'washington' or city == 'all'):
            break
        else:
            city = input('Enter Correct city (you can print all): ').lower()
    #SELECT MONTH
    month = input('\n which month? (January), (February), (March), (April), (May), or (June) ?\n').lower()
    while(True):
        if(month == 'january' or month == 'february' or month == 'march' or month == 'april' or month == 'may' or month == 'june' or month == 'all'):
            break
        else:
            month = input('Enter valid month:  (you can print all) \n').lower()
    #SELECT DAY
    day =  input('\nand which day ?\n').lower()    
    while(True):
        if(day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday' or day == 'saturday' or day == 'sunday' or day == 'all'):
            break
        else:
            day = input('Enter Correct day:  (you can print all)').lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # to_datetime is used to convert date into date format
    df['End Time'] = pd.to_datetime(df['End Time'])
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        #used to find index of month.
        month = months.index(month) + 1       
        df = df[df['Start Time'].dt.month == month] 
    #filter data by day.
    if day != 'all': 
        df = df[df['Start Time'].dt.weekday_name == day.title()]
     #print 5 rows.
    print(df.head())
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\n--------{ Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if(month == 'all'):
        mc_month = df['Start Time'].dt.month.value_counts().idxmax()
        print('Most common month is ' + str(mc_month))

    # display the most common day of week
    if(day == 'all'):
        mc_day = df['Start Time'].dt.weekday_name.value_counts().idxmax()
        print('Most common day is ' + str(mc_day))

    # display the most common start hour
    mc_hour = df['Start Time'].dt.hour.value_counts().idxmax()
    print('Most popular hour is ' + str(mc_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\n--------{Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # display most commonly used start station
    mc_start_station = st.mode(df['Start Station'])
    print('\nMost common start station is {}\n'.format(mc_start_station))

    # display most commonly used end station
    mc_end_station = st.mode(df['End Station'])
    print('\nMost common end station is {}\n'.format(mc_end_station))

    # display most frequent combination of start station and end station trip
    combin_trip = df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    mf_trip = combin_trip.value_counts().idxmax()
    print('\nMost popular trip is from {}\n'.format(mf_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n--------{ Calculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    time_1 = total_travel_time
    day = time_1 // (24 * 3600)
    time_1 = time_1 % (24 * 3600)
    hour = time_1 // 3600
    time_1 %= 3600
    minutes = time_1 // 60
    time_1 %= 60
    seconds = time_1
    print('\nTotal travel time is {} days {} hours {} minutes {} seconds'.format(day, hour, minutes, seconds))


    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    time_2 = mean_travel_time
    day2 = time_2 // (24 * 3600)
    time2 = time_2 % (24 * 3600)
    hour2 = time_2 // 3600
    time_2 %= 3600
    minutes2 = time_2 // 60
    time_2 %= 60
    seconds2 = time_2
    print('\nMean travel time is {} hours {} minutes {} seconds'.format(hour2, minutes2, seconds2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\n--------{ Calculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    no_of_subscribers = df['User Type'].str.count('Subscriber').sum()
    no_of_customers = df['User Type'].str.count('Customer').sum()
    print('\nNumber of subscribers are {}\n'.format(int(no_of_subscribers)))
    print('\nNumber of customers are {}\n'.format(int(no_of_customers)))

    # Display counts of gender
    if('Gender' in df):
        male_count = df['Gender'].str.count('Male').sum()
        female_count = df['Gender'].str.count('Female').sum()
        print('\nNumber of male users are {}\n'.format(int(male_count)))
        print('\nNumber of female users are {}\n'.format(int(female_count)))

    # Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        mc_birth_year = df['Birth Year'].mode()
        #most_common_birth_year = st.mode(df['Birth Year'])
        try:
            print('\n Oldest Birth Year is {}\n Youngest Birth Year is {}\n Most popular Birth Year is {}\n'.format(int(earliest_year), int(recent_year), int(mc_birth_year)))
        except TypeError:
    
            print('\n Oldest Birth Year is {}\n Youngest Birth Year is {}\n Most popular Birth Year is {}\n'.format(int(earliest_year), int(recent_year), mc_birth_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        #get_filter = printing the display of selection ----------- code in line 9
        city, month, day = get_filters()
        #load_data = getting the data from user ------------------- code in line 36
        df = load_data(city, month, day) 
        cont = input('\nWould you like to continue to Display (Most Frequent Times of Travel)? Enter yes or no.\n')
        if cont.lower() != 'yes':
            break

        time_stats(df, month, day) #code in line 55
        cont = input('\nWanna Display (most popular stations and trip)? Enter yes or no.\n')
        if cont.lower() != 'yes':
            break

        station_stats(df)          #code in line 79
        cont = input('\nhow about Display (total and average trip duration)? Enter yes or no.\n')
        if cont.lower() != 'yes':
            break

        trip_duration_stats(df)    #code in line 100
        cont = input('\nat last lets Display (statistics on bikeshare users)? Enter yes or no.\n')
        if cont.lower() != 'yes':
            break
        user_stats(df)             #code in line 135

        restart = input('\nWould you like to restart again with another city? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

print('Hello! Let\'s explore some US bikeshare data!')
if __name__ == "__main__":
	main()
