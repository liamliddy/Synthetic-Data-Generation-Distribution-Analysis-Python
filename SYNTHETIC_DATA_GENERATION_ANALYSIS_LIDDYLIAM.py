#SYNTHETIC DATA GENERATION & ANALYSIS LIAM LIDDY ISAN 3305.251
import os
import csv


#load file and ask user what file to select
def load_dataset():
    files = os.listdir("0_input")
    folder = "0_input"
    for num,file in enumerate(files,1):
        print(f"{num}:{file}")
    while True:
        try:
            select = int(input("Please select a file: "))
            if 1 <= select <= len(files):
                user_file = files[select - 1]
                break
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please try again.")
    path = os.path.join(folder,user_file)
#handles data and errors within file
    data = []
    errors = []
    with open(path, "r") as f:
        read = csv.reader(f)
        for num, row in enumerate(read, 1):
            if not row:
                errors.append(row)
            else:
                data.append(row)

    if errors:
        errs = ("errors_on_input.csv")
        errs_path = os.path.join(folder,errs)
        with open(errs_path,"w",newline = '')as f:
            write = csv.writer(f)
            write.writerows(errors)
        print("Errors saved.")

    if data:
        print("Data saved.")
    else:
        print("No data found.")
    return data
    
#asks user if the first row is a header
def header_row(data):
    
    header = False
    print("\n Here are the first 5 rows of data:")
    for num,row in enumerate(data[:5],1):
        print(f"{num} : {row}")
    while True:
        header = input("Is the first row is a header?(y/n): ").strip().lower()
        if header == "y":
            return True
        elif header == "n":
            return False

        else:
            print("Please enter 'y' or 'n'.")
    return header
    
#displays the first 50 rows of data from file
def display_data(data,header):
    if header:
        print("\n Here are the first 50 rows of data:")
        for num,row in enumerate(data[1:51],1):
            print(f"{num} : {row}")
    else:
        print("\n Here are the first 50 rows of data:")
        for num,row in enumerate(data[0:50],1):
            print(f"{num} : {row}")

#counts unique values and sorts them into column lists
def count_value_dist(data):
    count = {}
    brand = []
    weight = []
    counts = []
    price = []
    for row in data:
        for var in row:
            if var in count:
                count[var] += 1
            else:
                count[var] = 1
    
    for var,times in sorted(count.items()):
        if times > 1:
            if var.isalpha() or ' ' in var:
                brand.append((var,times))
            elif "." in var:
                price.append((var,times))
            for row in data:
                if var in row[1::4]:
                    counts.append((var,times))
                    break
            for row in data:
                if var in row[2::4]:
                    weight.append((var,times))
                    break
            
            
    return brand,price,counts,weight
    

    
    
#displays column lists up to 50 values and remaining values
def display_distribution(data,brand,price,counts,weight):
    print("\nUnique Values Per Column:")
    print("\nBrand Names:")
    for i in brand[:50]:
        print(i)
    if len(brand) > 50:
        left = len(brand) - 50 
        print(f"Remaining : {left}")
        
    print("\nWeights:")
    for i in weight[:50]:
        print(i)
    if len(weight) > 50:
        left = len(weight) - 50 
        print(f"Remaining : {left}")
        
    print("\nCounts:")
    for i in counts[:50]:
        print(i)
    if len(counts) > 50:
        left = len(counts) - 50 
        print(f"Remaining : {left}")
        
    print("\nPrices:")
    for i in price[:50]:
        print(i)
    if len(price) > 50:
        left = len(price) - 50 
        print(f"Remaining : {left}")
          
#pull random values from original data to generate synthetic data
def gen_synthetic_data(data,brand,price,counts,weight):
    import random
    synthetic_data = []
    print("\nGenerate Synthetic Data:")
    while True:
        try:
            rows = int(input("How many rows of data would you like to generate?: "))
            if rows <= 0:
                print("Please enter a positive non-zero number.")
            else:
                break
        except ValueError:
            print("Invalid input, please enter a positive non-zero number.")

    for row in range(rows):
        srow = []
        srow.append(random.choice(brand)[0])
        srow.append(random.choice(weight)[0])
        srow.append(random.choice(counts)[0])
        srow.append(random.choice(price)[0])
        synthetic_data.append(srow)

    print("\n Here are the first 50 rows of data:")
    for num,row in enumerate(synthetic_data[:50],1):
        print(f"{num} : {row}")

    return synthetic_data

#saves synthetic data to csv file and corrects name        
def save_synth(synthetic_data):
    while True:
        name = input("What would you like to name the file?: ").strip()
        if name == '':
            print("Cannot leave value blank, please name the file.")
        elif ".csv" not in name:
            name += ".csv"
            break
        else:
            break

    with open(name,"w", newline = '') as f:
        write = csv.writer(f)
        write.writerows(synthetic_data)
    print(f"Data saved to {name}.")

#asks for margin, counts values in both sets, and sums them to find percent dist
def check_distribution(data, synthetic_data):
    print("\nMargin of Error:")
    while True:
        try:
            margin = float(input("Please enter an acceptable margin of error as a decimal: "))
            if margin < 0:
                print("Please enter a number larger than 0.")
            else:
                break
        except ValueError:
            print("Please enter the margin of error as a decimal.")
    data_count = {}
    for row in data:
        for var in row:
            if var in data_count:
                data_count[var] += 1
            else:
                data_count[var] = 1
                
    synth_count = {}
    for row in synthetic_data:
        for var in row:
            if var in synth_count:
                synth_count[var] += 1
            else:
                synth_count[var] = 1
                
    total = sum(data_count.values()) + sum(synth_count.values())
    data_total = sum(data_count.values())
    synth_total = sum(synth_count.values())
    differences = []
    total_diff = 0
    count_diff = 0
#compares occurrences in each set, adds differences/margin to list
    for var in data_count:
        if var in synth_count:
            data_per = (data_count[var] / data_total) * 100
            synth_per = (synth_count[var] / synth_total) * 100
            diff = (data_per - synth_per)
            if diff < 0:
                diff *= -1
            total_diff += diff
            count_diff += 1
        

            if diff <= margin * 100:
                differences.append((var, f"{diff:.2f}%", 'Within Margin.'))
            else:
                differences.append((var,f"{diff:.2f}%", 'Not Within Margin.'))
        else:
            differences.append((var, None, "Only in original data."))
    average = total_diff / count_diff
    for var in synth_count:
        if var not in data_count:
            differences.append((var, None, "Only in synthetic data."))

    for var in differences[:25]:
        print(var)
    if len(differences) > 25:
            left = len(differences) - 25
            print(f"Overall Average Difference : {average:.2f}%")
            print(f"Remaining : {left}")
    
    while left:
        view = input("Would you like to view the remaining rows?(y/n): ").strip().lower()
        if view == 'y':
            for var in differences[25:]:
                print(var)
            break
                
        elif view == 'n':
            break
        else:
            print("Please enter 'y' or 'n'.")
        
    
                
#ask user if they would like to exit
def exit_program():
    while True:
        done = input("Would you like to exit?(y/n): ").strip().lower()
        if done == 'y':
            print("Goodbye, thank you for your time!")
            return
        elif done == 'n':
            main()   
        else:
            print("Please enter 'y' or 'n'.")


def main():

    data=load_dataset()
    header = header_row(data)
    display_data(data,header)
    brand,price,counts,weight = count_value_dist(data)
    display_distribution(data,brand,price,counts,weight)
    synthetic_data = gen_synthetic_data(data,brand,price,counts,weight)
    save_synth(synthetic_data)
    check_distribution(data,synthetic_data)
    exit_program()
main()
