import main_module as mm
def main():  
    # To Open the CSV file  
    with open('basic_data.csv', newline = '') as csv_file:  
        csv_read = mm.csv.reader( csv_file, delimiter = ',')  

        # To Read and display each row  
        for row in csv_read:  
            print(row)  
if __name__ == '__main__':  
    main()  
    print (mm.module_name)