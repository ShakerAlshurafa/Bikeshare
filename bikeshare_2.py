import time
import pandas as pd
import numpy as np

##############################
# Bikeshare Analysis Project #
##############################

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    
    while True:
        city = input("Enter the city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("*Invalid city* \nPlease choose from (chicago, new york city, washington).")


    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Enter the month (january, february, ... , june) or 'all': ").lower()
        if month == 'all' or month in months:
            break
        else:
            print("*Invalid month* \nPlase choose a valid month or 'all'.")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Enter the day of the week (monday, tuesday, ... sunday) or 'all': ").lower()
        if day in days or day == 'all':
            break
        else:
            print("*Invalid day* \nPlease choose a valid day or 'all'.")

    print('-'*40)
    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()
    
    if month != 'all':
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common Month: {common_month.title()}")

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {common_day.title()}")

    # display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(f"Most common start hour: {common_hour}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(f"Most common start Station: {common_start}")

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(f"Most common end station: {common_end}")

    # display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['trip'].mode()[0]
    print(f"Most common trip: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travelTime = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travelTime} seconds")

    # display mean travel time
    mean_travelTime = df['Trip Duration'].mean()
    print(f"Mean travel time : {mean_travelTime:.2f} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(f"User types: {df['User Type'].value_counts()}")

    # Display counts of gender
    if 'Gender' in df.columns:
        print(f"\nGender distribution: {df['Gender'].value_counts()}")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print(f"\nEarliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {recent_year}")
        print(f"Most common year of birth: {common_year}")
    else:
        print("\nBirth year data is not available.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    start = 0  # Initialize the starting index for displaying rows of data
    # Ask the user if they want to see the first 5 lines of raw data
    display = input('\nWould you like to see 5 lines of raw data? Enter (yes or no).\n').lower()
    
    # Keep showing 5 lines of data until the user chooses 'no' or all data is displayed
    while display == 'yes':
        # Display 5 rows of data starting from the current 'start' index
        print(df.iloc[start:start + 5])
        
        # Check if there are fewer than 5 rows remaining in the dataset
        if start + 5 >= len(df):
            print('\nNo more data to display.')  # Inform the user that all data has been shown
            break  # Exit the loop if there is no more data to display
        
        # Ask the user if they want to see 5 more lines of data
        display = input('\nWould you like to see 5 more lines of raw data? Enter (yes or no).\n').lower()
        start += 5  # Increment the start index by 5 for the next set of rows

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
