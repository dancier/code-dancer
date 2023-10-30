from services.dancer import RestClient as DancerService
from services.chat_dancer import RestClient as ChatDancerService
from test_data.importer import JsonImporter
from test_data.generator import SimpleGenerator


dc = DancerService()
cdc = ChatDancerService()

ji = JsonImporter()

generator = SimpleGenerator()

print("Ramping up DAST")
print("You are having now...")
print('--> a RestClient to the Dancer with "dc"')
print('--> a RestClient to the ChatDancer with cdc')
print('--> a Test-Data Generator with "generator"')
print('--> a Test-Date Importer for Json-Date with "ji"')
