import csv

file_name = "georef-germany-postleitzahl.csv"

print(file_name)

with open(file_name, mode='r') as source_file:
    csv_reader = csv.DictReader(source_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {",".join(row.keys())}')
            line_count += 1
        zip_code = row['Name']
        zip_kreis_name = row['Kreis name']
        zip_name_short = row['PLZ Name (short)']
        zip_area_points = row['geo_point_2d']#.split(',')
        print(f'zip: {zip_code} in Stadt: {zip_name_short} in kreis: {zip_kreis_name} with points: {zip_area_points}')

