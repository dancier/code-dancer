import numpy as np
from scipy.stats import truncnorm
import matplotlib.pyplot as plt
from scipy.stats import norm
import random
import typing
import collections

def get_normal_distributed_heights(height_mean, standard_deviation, sample_size):
    heights =  norm.rvs(loc=height_mean, scale=standard_deviation, size=sample_size)
    return [ round(h) for h in heights]

def get_genders_divers_or_not_sample( sample_size )->typing.List[str]:
    pool_divers = ["d"]*2
    pool_not_divers = ["nd"] * 998
    pool_divers.extend(pool_not_divers)
    complete_pool_divers = pool_divers
    return random.choices(complete_pool_divers,k=sample_size)

def get_genders_man_or_woman_sample(sample_size)->typing.List[str]:
    pool_men = ["m"]*105
    pool_woman = ["w"]*100
    pool_men.extend(pool_woman)
    complete_pool_men_woman = pool_men
    result_men_woman = random.choices(complete_pool_men_woman,k=sample_size)
    return result_men_woman

def get_genders_samples( sample_size):
    gender_divers_list = get_genders_divers_or_not_sample( sample_size )
    distribution_gender = collections.Counter(gender_divers_list)
    divers_samples = distribution_gender['d']
    divers_list = ['d']*divers_samples
    not_divers_samples = distribution_gender['nd']
    gender_man_woman_list = get_genders_man_or_woman_sample( not_divers_samples )
    gender_man_woman_list.extend(divers_list)
    return gender_man_woman_list


def assign_city()->str:
    return "Hamburg"

# wohnort unabhängig von Geschlecht und Körpergröße
def get_bezirk_hamburg(
    sample_size:int,
    p_ham_mitte = 0.16,
    p_altona = 0.14,
    p_eimsbuettel = 0.14,
    p_hamb_nord = 0.17,
    p_wandsbek = 0.23,
    p_bergedorf = 0.07,
    p_harburg = 0.09,
):
    population = ["ham_mitte", "altona", "eimsbuettel", "hamb_nord", "wandsbek", "bergedorf", "harburg" ]
    weights = [p_ham_mitte, p_altona, p_eimsbuettel, p_hamb_nord, p_wandsbek, p_bergedorf, p_harburg ]
    random_bezirke = random.choices( population, weights,k=sample_size )
    return random_bezirke


def distribution_residents_hamburg_bezirk(sample_size):
    gesamt_residents = 1906500
    hamburg_mitte_p = 300000 /gesamt_residents
    altona_p = 275000 / gesamt_residents
    eimsbuettel_p = 270000 / gesamt_residents
    hamburg_nord_p = 316000 / gesamt_residents
    wandsbek_p = 444000 / gesamt_residents
    bergedorf_p = 131000 / gesamt_residents
    harburg_p = 170500 / gesamt_residents


def get_plz_and_street_for_bezirk( bezirk ):
    bezirk_plz_map = {
        "ham_mitte":[
            ("20457","Alter Wall") ,
            ("20539","Am Zollhafen"),
        ], 
        "altona":[
            ("20359","Feldstrasse"),
            ("22765","Holstenplatz"),
        ], 
        "eimsbuettel":[
            ("20144","Beim Schlump"),
            ("20253","Goebenstraße"),
        ], 
        "hamb_nord":[
            ("22335","Alsterberg"),
            ("22339","Am Backofen"),
        ], 
        "wandsbek":[
            ("22041","Am Neumarkt"),
            ("22047","Westerlandstraße"),
        ], 
        "bergedorf":[
            ("21029","Holzhude"),
            ("21031","Am Blumenhof"),
        ],   
        "harburg":[
            ("21073","Zweite Twiete"),
            ("21075","Talwinkel"),
        ],
    }
    return random.choice(bezirk_plz_map[bezirk])

def get_wohnorte_for_city(city:str, sample_size:int):
    if city == "Hamburg":
        hamburg_bezirke = get_bezirk_hamburg( sample_size )
    wohnort_objects = []
    for b in hamburg_bezirke:
        plz, street = get_plz_and_street_for_bezirk( b )
        wohnort_objects.append ( 
            {
                "city":city,
                "plz":plz,
                "street":f"{street} {random.randint(1,9)}",
            }
        )
    return wohnort_objects


def generate_dancers( 
    sample_size:int,
    mean_height_men:int = 178,
    standard_deviation_height_men:int = 5,
    mean_height_women:int = 166,
    standard_deviation_height_women:int = 5,

 ):
    dancers = {}
    gender_list = get_genders_samples( sample_size )
    distribution_gender = collections.Counter(gender_list)
    men_heights = get_normal_distributed_heights(
        mean_height_men, 
        standard_deviation_height_men, 
        distribution_gender['m']
    )
    women_heights = get_normal_distributed_heights( 
        mean_height_women, 
        standard_deviation_height_women, 
        distribution_gender['w']
    )
    divers_heights = get_normal_distributed_heights( 
        round(np.mean([mean_height_men,mean_height_women])), 
        standard_deviation_height_women, 
        distribution_gender['d']
    )
    men_objects = [ { "Geschlecht":"m", "Koerpergroesse":k } for k in men_heights  ]
    women_objects = [ { "Geschlecht":"w", "Koerpergroesse":k } for k in women_heights  ]
    divers_objects = [ { "Geschlecht":"d", "Koerpergroesse":k } for k in divers_heights  ]
    men_objects.extend(women_objects)
    men_objects.extend(divers_objects)
    all_objects = men_objects
    random.shuffle(all_objects)
    city = "Hamburg"
    wohnorte = get_wohnorte_for_city(city, sample_size)
    for i,o in enumerate(all_objects):
        o["Stadt"] = wohnorte[i]["city"]
        o["PLZ"] = wohnorte[i]["plz"]
        o["Strasse"] = wohnorte[i]["street"]
    return all_objects
    

if __name__ == "__main__":    
    sample_size = 1000
    dancers = generate_dancers(sample_size)
    print(dancers[:10])

    