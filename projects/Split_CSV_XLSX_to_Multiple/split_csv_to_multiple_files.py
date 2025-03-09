import pandas as pd
import os

def split_file(file_path, records_per_file, include_header):
    # Determine file type
    file_extension = os.path.splitext(file_path)[-1].lower()
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    print(f'File Name: {file_name}')
    print(f'File Include Header: {include_header}')
    
    if file_extension == ".csv":
        df = pd.read_csv(file_path)
    elif file_extension in [".xls", ".xlsx"]:
        df = pd.read_excel(file_path)
    else:
        print("Unsupported file format. Please provide a CSV or XLSX file.")
        return
    
    # Calculate total number of chunks
    total_records = len(df)
    print(f'Total Records: {total_records}')
    num_files = (total_records // records_per_file) + (1 if total_records % records_per_file != 0 else 0)
    print(f'Num of Files: {num_files}')

    output_folder = "split_files"
    os.makedirs(output_folder, exist_ok=True)
    
    for i in range(num_files):
        start_idx = i * records_per_file
        end_idx = start_idx + records_per_file
        chunk = df.iloc[start_idx:end_idx]
        
        output_file = os.path.join(output_folder, f"{file_name}_{i+1}{file_extension}")
        
        if file_extension == ".csv":
            chunk.to_csv(output_file, index=False, header=include_header)
        else:
            chunk.to_excel(output_file, index=False, header=include_header)
        
        print(f"Created: {output_file}")
    
    print(f"Splitting complete! {num_files} files created in '{output_folder}' directory.")

if __name__ == "__main__":
    file_path = input("Enter the path to the CSV/XLSX file: ").strip()
    records_per_file = int(input("Enter the number of records per file: "))
    include_header = input("Does the input file have a header? (yes/no): ").strip().lower() == "yes"
    split_file(file_path, records_per_file, include_header)
