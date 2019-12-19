#Obtain number of seconds from the user
custom_seconds = float(input('Enter a number of seconds you would like to have: '))

#Obtain total number of hours each hour has 3600 second
obtain_hours = custom_seconds // 3600

#Remaining minutes
minutes = (custom_seconds // 60) % 60

#Remaining seconds
remaining_seconds = custom_seconds % 60

#Display result
print('''''Here's'''' your time in hours, minutes, and seconds')
print('Hours: ' , obtain_hours)
print('Minutes: ' , minutes)
print('Seconds: ' , remaining_seconds)