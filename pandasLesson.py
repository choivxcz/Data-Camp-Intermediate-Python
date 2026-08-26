import pandas as pd
# Load cars for tasks 4-7
cars = pd.read_csv('cars.csv', index_col = 0)

def task_1():
    print("Task 1")
    # Pre-defined lists
    names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
    dr =  [True, False, False, False, True, True, True]
    cpc = [809, 731, 588, 18, 200, 70, 45]

    # Create dictionary my_dict with three key:value pairs: my_dict
    my_dict = {
        'country' : names,
        'drives_right' : dr,
        'cars_per_cap' : cpc
    }

    # Build a DataFrame cars from my_dict: cars
    cars = pd.DataFrame(my_dict)

    # Print cars
    print(cars)


def task_2():
    print("Task 2")
    # Build cars DataFrame
    names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
    dr =  [True, False, False, False, True, True, True]
    cpc = [809, 731, 588, 18, 200, 70, 45]
    cars_dict = { 'country':names, 'drives_right':dr, 'cars_per_cap':cpc }
    cars = pd.DataFrame(cars_dict)
    print(cars)

    # Definition of row_labels
    row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

    # Specify row labels of cars
    cars.index = row_labels

    # Print cars again
    print(cars)

    # Import the cars.csv data: cars
    cars = pd.read_csv('cars.csv')

    # Print out cars
    print(cars)


def task_3():
    print("Task 3")

    # Fix import by including index_col
    cars = pd.read_csv('cars.csv', index_col = 0)

    # Print out cars
    print(cars)


def task_4():
    print("Task 4")
    # Print out country column as Pandas Series
    print(pd.Series(cars['country']))

    # Print out country column as Pandas DataFrame
    print(pd.DataFrame(cars['country']))

    # Print out DataFrame with country and drives_right columns
    print(pd.DataFrame(cars[['country', 'drives_right']]))


def task_5():
    print("Task 5")
    # Print out first 3 observations
    print(cars[0:3])

    # Print out fourth, fifth and sixth observation
    print(cars[3:6])


def task_6():
    print("Task 6")
    # Print out observation for Japan
    print(cars.iloc[2])

    # Print out observations for Australia and Egypt
    print(cars.iloc[[1, 6]])


def task_7():
    print("Task 7")
    # Print out drives_right value of Morocco
    print(cars.loc['JAP', 'drives_right'])

    # Print sub-DataFrame
    print(cars.iloc[[4, 5], [1, 2]])


# Run each task
task_1()
print("")
task_2()
print("")
task_3()
print("")
task_4()
print("")
task_5()
print("")
task_6()
print("")
task_7()