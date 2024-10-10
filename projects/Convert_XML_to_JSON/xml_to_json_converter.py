import json
import xmltodict

if __name__ == "__main__":
    try:
        with open('input.xml') as xml_file:
            xml_data = xml_file.read()
            xml_parsed_data = xmltodict.parse(xml_data)
            json_data = json.dumps(xml_parsed_data)
            with open('output.json', 'w') as json_file:
                json_file.write(json_data)

    except Exception as exp:
        print(f'Error: {str(exp)}')