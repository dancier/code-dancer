import os

def evn_or_default(var_name, default):
    envioronment_variable = os.getenv(var_name)
    if envioronment_variable:
        return envioronment_variable
    return default

dancer_hostname = evn_or_default("DAST_DANCER_HOST", "http://localhost:8080")



