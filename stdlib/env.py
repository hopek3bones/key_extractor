import os

def get_env_var(var_name, default_value=None):
    """ Program that is used to recovery the environment data """
    try:
        return os.environ.get(var_name, default_value);
    except:
        return None;


pass;
