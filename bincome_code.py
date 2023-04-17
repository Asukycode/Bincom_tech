import statistics

import random
# This dictionary is responsible for matching all week numbers to the week days
week_days = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday"
}


def color_counter(color: list):
    # Here I declared color name variables to store the counts for each color
    arsh_count = 0
    black_count = 0
    blue_count = 0
    brown_count = 0
    cream_count = 0
    green_count = 0
    orange_count = 0
    pink_count = 0
    red_count = 0
    white_count = 0
    yellow_count = 0
    # color count variable end here

    # Here is a for loop to count the occurence of each color
    for i in colors:
        if i.lower() == "arsh":
            arsh_count += 1
        elif i.lower() == "black":
            black_count += 1
        elif i.lower() == "blue":
            blue_count += 1
        elif i.lower() == "brown":
            brown_count += 1
        elif i.lower() == "cream":
            cream_count += 1
        elif i.lower() == "green":
            green_count += 1
        elif i.lower() == "orange":
            orange_count += 1
        elif i.lower() == "pink":
            pink_count += 1
        elif i.lower() == "red":
            print(f"""
    colors and their frequencies
        Arsh {arsh_count} 
        Black {black_count}
        Blue {blue_count}
        Brown {brown_count}
        Cream {cream_count}
        Green {green_count}
        Orange {orange_count}
        Pink {pink_count}
        Red {red_count}
        White {white_count}
        Yellow {yellow_count}
    """)
            red_count += 1
        elif i.lower() == "white":
            white_count += 1
        elif i.lower() == "yellow":
            yellow_count += 1
    # At this point the colors were added into a list
    global cloth_amount  # I had to make the cloth_amount variable global because it will be used in the most_worn function

    cloth_amount = [
        arsh_count,
        black_count,
        blue_count,
        brown_count,
        cream_count,
        green_count,
        orange_count,
        pink_count,
        red_count,
        white_count,
        yellow_count, ]
    # print(cloth_amount)


# This function helps to know Most worn cloth in a day parameter is a list
def most_worn(cloth_worn: list):
    most_worn_cloth = 0
    for x in cloth_worn:
        if x > most_worn_cloth:
            most_worn_cloth = x
    # print(f"Most worn {most_worn_cloth}")

    if most_worn_cloth == cloth_worn[0]:
        print(f"Most worn cloth ARSH")
    elif most_worn_cloth == cloth_worn[1]:
        print(f"Most worn cloth BLACK")
    elif most_worn_cloth == cloth_worn[2]:
        print(f"Most worn cloth BLUE")
    elif most_worn_cloth == cloth_worn[3]:
        print(f"Most worn cloth BROWN")
    elif most_worn_cloth == cloth_worn[4]:
        print(f"Most worn cloth CREAM")
    elif most_worn_cloth == cloth_worn[5]:
        print(f"Most worn cloth GREEN")
    elif most_worn_cloth == cloth_worn[6]:
        print(f"Most worn cloth ORANGE")
    elif most_worn_cloth == cloth_worn[7]:
        print(f"Most worn cloth PINK")
    elif most_worn_cloth == cloth_worn[8]:
        print(f"Most worn cloth RED")
    elif most_worn_cloth == cloth_worn[9]:
        print(f"Most worn cloth WHITE")
    elif most_worn_cloth == cloth_worn[10]:
        print(f"Most worn cloth YELLOW")
    else:
        print("All cloths equal ")


# most worn Function ends here

# Median color here


def median_colors(x: list):
    print(f'The median color is {statistics.median(x)}')


# Enter your colors

# color count variable here
colors = []  # List of colors during the week
staff_number = int(input("How many staff in Industry"))  # Amount of staff in the industry
work_days = int(input("How many days does industry operate in a week"))  # days of work in the industry

# Here a for loop was created to iterate over the staff_number
# so as to enter each staff i also did the same for the work days.
for day in range(work_days):
    for staff in range(staff_number):
        color = input(f'What color did staff {staff + 1} were on {week_days[day + 1]} ? : ')
        colors.append(color)

print(f'Here are all the colors for all the week days -> {colors}')

color_counter(colors)
most_worn(cloth_amount)
median_colors(cloth_amount)

# Fibonacci Sequence Here
def fibonacci_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sum = 0
        fib_n_minus_two = 0
        fib_n_minus_one = 1
        for i in range(2, n+1):
            fib_sum = fib_n_minus_two + fib_n_minus_one
            fib_n_minus_two = fib_n_minus_one
            fib_n_minus_one = fib_sum
        return fib_sum

print(fibonacci_sum(50))




# Generate a random 4-digit binary number
binary_num = ""
for i in range(4):
    digit = random.randint(0, 1)
    binary_num += str(digit)

# Convert the binary number to decimal
decimal_num = int(binary_num,2)
print(decimal_num)