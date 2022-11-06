from services.dancer import RestClient as DancerService
from test_data.importer import JsonImporter
from test_data.generator import SimpleGenerator


dc = DancerService()

ji = JsonImporter()

generator = SimpleGenerator()

print("Ramping up DAST")
print("You are having now...")
print('--> a RestClient to the Dancer with "dc"')
print('--> a Test-Data Generator with "generator"')
print('--> a Test-Date Importer for Json-Date with "ji"')


