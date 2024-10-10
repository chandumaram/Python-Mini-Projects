import json
import csv

if __name__ == '__main__':
    try:
        # Opening JSON file and loading data into the json_data variable
        with open('input.json') as json_file:
            json_data = json.load(json_file)
            # print(json_data)
            # now open a csv file for write the data
            with open('output.csv', 'w', newline="") as csv_file:
                # create the csv writer object
                csv_writer = csv.writer(csv_file)
                # counter variable used for writing Headers to the csv file
                count = 0
                for data in json_data:
                    if count == 0:
                        # writing headers of CSV file
                        headers = data.keys()
                        csv_writer.writerow(headers)
                        count += 1

                    # writing data of CSV file
                    csv_writer.writerow(data.values())

    except Exception as exp:
        print(f'Error: {str(exp)}')