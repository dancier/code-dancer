def get_zip_to_city_map(filename):
    import csv
    res = dict()
    with open(filename, mode='r') as source_file:
        csv_reader = csv.DictReader(source_file, delimiter=';')
        for row in csv_reader:
            res[row['Name']] = row['PLZ Name (short)']
    return res

def draw(dimension):
    import random
    total_weights = sum(dimension.values())
    shoot = random.randrange(1, total_weights + 1)
    i = 0
    for key in dimension.keys():
        i = i + dimension.get(key)
        if shoot <= i:
            return key


class Generator():

    def __init__(self, csv_filename):
        self.focus_cities = [
            "Dortmund",
            "Essen",
            "Bochum",
            "Düsseldorf",
            "Köln",
            "Hamburg",
            "Frankfurt",
            "Berlin"
        ]

        self.sex = {
            "MALE": 45,
            "FEMALE": 45,
            "DIVERS": 3,
            "NA": 3
        }

        self.dances = {
            "Tango": 2,
            "Salsa": 4,
            "Standard": 7,
            "Lindy-Hop": 1,
            "Swing": 1
        }

        self.month = {
            "02" : 1,
            "03" : 1
        }

        self.day = {
            "01" : 1
        }

        self.size = {
            100 :1
        }

        self.can_do = {
            1: 80
        }

        self.level = {
            "NO_EXPERIENCE": 30,
            "BASIC": 20,
            "INTERMEDIATE": 30,
            "ADVANCED": 10,
            "PRO": 15
        }
        self.age = {
            18 : 1,
            19 : 1,
            20 : 1,
            21 : 1,
            22 : 1,
            23 : 1,
            24 : 1,
            25 : 1,
            26 : 1,
            27 : 1,
            28 : 1,
            29 : 1,
            30 : 1,
            31 : 1,
            32 : 1,
            33 : 1,
            34 : 1,
            35 : 1,
            36 : 1,
            37 : 1,
            38 : 1,
            39 : 1,
            40 : 1,
            41 : 1,
            42 : 1,
            43 : 1,
            44 : 1,
            45 : 1,
            46 : 1,
            47 : 1,
            48 : 1,
            49 : 1,
            50 : 1
        }

        self.zip_to_city = get_zip_to_city_map(csv_filename)
        self.weighted_city_map = self.get_weighted_city_map()

    def get_weighted_city_map(self):
        res = {}
        for zip in self.zip_to_city.keys():
            city = self.zip_to_city[zip]
            focus_city = False
            for fc in self.focus_cities:
                if city in fc:
                    focus_city=True
                    print("Found Focus City: " + city)
                    break
            if focus_city:
                res[zip] = 10
            else:
                res[zip] = 1

        return res

    def get_x_dancer(self, x):
        res = []
        for i in range(x):
            res.append(self.get_one_random_dancer(i+1))
        return res

    def produce_import_file(self, size, output_filename):
        import json
        res_dict = {
            "dancer": self.get_x_dancer(size)
        }

        res_json_str = json.dumps(res_dict, indent=4)
        with open(output_filename, "w") as outfile:
            outfile.write(res_json_str)


    def get_one_random_dancer(self, i):
        res = dict()
        res["email"] = str(i) + "-test@dancier.net"
        res["dancerName"] = str(i) + "-test"
        res["password"] = "secret"
        res["aboutMe"] = "lorem ipsum"
        res["gender"] = draw(self.sex)
        res["birthDate"] = str(2022-draw(self.age)) \
                           + "-" + draw(self.month) \
                           + "-" + draw(self.day)

        res["zipCode"] = draw(self.weighted_city_map)
        res["country"] = "GER"
        res["size"] = draw(self.size)
        self.able_to(res)
        self.wants_to(res)
        return res

    def able_to(self, dancer):
        dances = []
        for i in range(draw(self.can_do)):
            dance = dict()
            dance["dance"] = draw(self.dances)
            dance["level"] = draw(self.level)
            if dancer['gender'] == 'MALE':
                dance['leading'] = 'LEAD'
            else:
                dance['leading'] = 'FOLLOW'
            dances.append(dance)
        dancer["ableTo"] = dances

    def wants_to(self, dancer):
        dances = []
        for able_to in dancer["ableTo"]:
            dance = dict()
            dance['dance'] = able_to['dance']
            if able_to["leading"] in ['LEAD', 'FOLLOW']:
                if able_to['leading'] == 'LEAD':
                    dance['leading'] = 'FOLLOW'
                else:
                    dance['leading'] = 'LEAD'
            else:
                able_to['leading'] = 'BOTH'
            dance['level'] = draw(self.level)
            dances.append(dance)
        dancer["wantsTo"] = dances
