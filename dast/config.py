import os


def env_or_default(var_name, default):
    environment_variable = os.getenv(var_name)
    if environment_variable:
        return environment_variable
    return default


DANCER_HOSTNAME = env_or_default("DAST_DANCER_HOST", "http://localhost:8080")
DANCER_ADMIN_USER = env_or_default("DANCER_ADMIN_USER", "marc@gorzala.de")
DANCER_ADMIN_PASS = env_or_default("DANCER_ADMIN_PASS", "secret")