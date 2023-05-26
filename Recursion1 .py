#!/usr/bin/env python
# coding: utf-8

# In[2]:


def reverse_string_recursive(s):
    # Base case: if the input string is empty or has only one character, return the input string
    if len(s) < 2:
        return s
    
    # Recursive case: reverse the substring from the second character to the end of the string
    # link first character to the end of string 
    return reverse_string_recursive(s[1:]) + s[0]

def main():
    # Test recursive with example strings in main function
    test_strings = ['hello', 'world', 'racecar', 'python']
    
    for s in test_strings:
        print('Input string:', s)
        reversed_str = reverse_string_recursive(s)
        print('Reversed string:', reversed_str)
        print()

if __name__ == '__main__':
    main()


# In[ ]:


def main():
    # open and read the zip code file
    with open('zipcodelist.txt', 'r') as f:
        zip_codes = f.read().splitlines()

    # open and read the city file
    with open('CityList.txt', 'r') as f:
        cities = f.read().splitlines()

    # create a dictionary of zip codes and cities
    zip_city_dict = dict(zip(zip_codes, cities))

    # prompt the user to enter a zip code
    while True:
        zip_code = input("Please enter a zip code: ")
        if zip_code in zip_city_dict:
            print(f"The town for {zip_code} is {zip_city_dict[zip_code]}.")
            
        else:
            print(f"Error: Zip code {zip_code} not found. Please enter a valid zip code.")

if __name__ == '__main__':
    main()


# In[ ]:




