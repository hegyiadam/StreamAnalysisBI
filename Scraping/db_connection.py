import xmltodict

def get_db_config(config_filepath):
    with open(config_filepath) as fd:
        db_config_raw = xmltodict.parse(fd.read())
    db_config = db_config_raw['connection']
    return db_config;

def get_db_connection_string(config_filepath):
    db_config = get_db_config(config_filepath)
    return "host="+db_config['host']+" dbname="+db_config['dbname']+" user="+db_config['credentials_user']+" password="+db_config['credentials_pass']