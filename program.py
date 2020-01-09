import requests

def main():
    #print the header
    print_the_header()
    #get zipcode from user
    zcode = input('What is the zipcode you want to see the weather? [XXXXX]: ')

    #get HTML form web
    get_html_from_web(zcode)
    gusts = response.text
    #display the gust information
    print(f'The gusts in area code {zipcode} are {gusts}')
    quitting = input('Would you like to quit? y or n : ')
    if quitting == n:
        main()
    else:
        print('Cheers')

def print_the_header():
    print('--------------------------')
    print('     Weather App')
    print('--------------------------')
    print()

def get_html_from_web(zipcode):
    url = f'http://www.wunderground.com/weather-forecast/{zipcode}'
    response = requests.get(url)
    print(response)
    print('Cheers')

if __name__ == '__main__':
    main()

