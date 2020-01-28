import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA={'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all':7}
DAY_DATA={'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'saturday':5,  'sunday':6, 'all':7}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
        # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city=''
    while city.lower() not in CITY_DATA:
        city=input('Which city data would you like to explore: New York, Chicago or Washington? \n').lower()
        if city.lower() =='chicago':
            print('You choose Chicago')
        elif city.lower() =='new york':
            print('You choose New York')
        elif  city.lower() =='washington':
            print('You choose Washington')
        else:
            print('Sorry! Please enter a valid name of the city.')
    month=''
    while month.lower() not in MONTH_DATA:
        month=input('Wich month would you like to explore: January, February, March, April, May, June or all ?\n ').lower()
        if month.lower() == 'january':
            print('You choose January')
        elif month.lower() == 'februay':
            print('You choose February')
        elif month.lower() == 'march':
            print('You choose March')
        elif month.lower() == 'april':
            print('You choose April')
        elif month.lower() == 'may':
            print('You choose May')
        elif month.lower() == 'june':
            print('You choose June')
        elif month.lower() == 'all':
            print('You choose all months')
        else:
            print('Sorry! Please enter a valid name of the month.')
    day=''
    while day.lower() not in DAY_DATA:
        day=input('Which day of week would you like to see: monday, tuesday, wednesday, thursday, saturday, sunday or all? \n').lower()
        if day.lower()=='monday':
            print ('You choose Monday')
        elif day.lower()=='tuesday':
            print ('You choose Tuesday')
        elif day.lower()=='wednesday':
            print ('You choose Wednesday')
        elif day.lower()=='thursday':
            print ('You choose Thursday')
        elif day.lower()=='saturday':
            print ('You choose Saturday')
        elif day.lower()=='sunday':
            print ('You choose Sunday')
        elif day.lower()=='all':
            print ('You choose All')
        else:
            print('Sorry! Please enter a valid day of week.')

    print('-'*40)
    return city.lower(), month.lower(), day.lower()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]
    print ('Most common month is:{}'.format(popular_month))

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print ('Most common day of week is:{}'.format(popular_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print ('Most common start hour is:{}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print ('Most commonly used Start Station is: {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print ('Most commonly used End Station is: {}'.format(popular_end_station))


    # display most frequent combination of start station and end station trip
    #first we need to create a new column with the combination between Start Sation and End Station
    df['route'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    popular_route=df['route'].mode()[0]
    print ('Most frequent combination of start station and end station trip is: {}'.format(popular_route))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = df['Trip Duration'].sum()
    mins, sec = divmod(total_travel, 60)
    hour, mins = divmod(mins, 60)
    print('The total travel time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    mins, sec = divmod(mean_travel, 60)
    hour, mins = divmod(mins, 60)
    print('The mean travel time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types is: ', user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        count_male = (df['Gender'] == 'Male').sum()
        count_female = (df['Gender'] == 'Female').sum()
        print('\nThe count of male is: {}'.format(count_male))
        print('\nThe count of female is:{}'.format(count_female))
    else:
        print('The customer gender is not available for this city')

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        b_early = int(df['Birth Year'].min())
        b_recent = int(df['Birth Year'].max())
        b_common = int(df['Birth Year'].mode())
        print('\nThe earliest year of birth:{}'.format(b_early))
        print('\nThe most recent year of birth:{}'.format(b_recent))
        print('\nThe most common year of birth:{}'.format(b_common))
    else:
        print('Year of birth is not available for this city')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    show_data = input("\n Would you like to see 5 lines of a data sample? Please type 'yes' or 'no' \n").lower()
    index1=0
    index2=5
    while True:
        if show_data == 'no':
                return
        elif show_data == 'yes':
                 print(df.iloc[index1:index2])
                 index1 += 5
                 index2 += 5
                 show_data = input("\n Would you like to see more 5 lines of a data sample? Please type 'yes' or 'no' \n").lower()
        else:
            print("This is not a correct answer.").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
