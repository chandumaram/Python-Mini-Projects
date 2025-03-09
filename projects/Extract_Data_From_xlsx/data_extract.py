import pandas as pd

try:
    # Load the Excel file
    file_path = 'C:\My Data\Python Practice\Python-Mini-Projects\projects\Extract_Data_From_xlsx\Hyderabad.xlsx'  # Replace with your file path
    data = pd.read_excel(file_path)

    # Extract the pincode column, sort it, and remove duplicates
    pincode_column = data['Pincode']
    print(len(pincode_column))
    unique_sorted_pincodes = sorted(pincode_column.drop_duplicates())
    print(len(unique_sorted_pincodes))
    # Convert the list to a comma-separated string without spaces
    pincodes = ','.join(map(str, unique_sorted_pincodes))

    with open('pincodoes.txt', 'w') as text_file:
        text_file.write(pincodes)

    # Display the result
    # print(pincodes)
except Exception as exp:
    print(f'Error: {str(exp)}')