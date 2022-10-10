import csv

# download this file from: https://public.opendatasoft.com/explore/dataset/georef-germany-postleitzahl/table/

file_name = "georef-germany-postleitzahl.csv"

with open(file_name, mode='r') as source_file:
    csv_reader = csv.DictReader(source_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        zip_code = row['Name']
        zip_kreis_name = row['Kreis name']
        zip_name_short = row['PLZ Name (short)']
        zip_area_points = row['geo_point_2d'].split(',')
        print(f"""
        INSERT INTO location_zip_code (id, zip_code, country, latitude, longitude, city)
            SELECT gen_random_uuid(), {zip_code}, 'GER', {zip_area_points[0]}, {zip_area_points[1]}, '{zip_name_short}'
        WHERE NOT EXISTS(
            SELECT 1 FROM location_zip_code
             WHERE country = 'GER'
               AND zip_code = '{zip_code}'
        );
        """)