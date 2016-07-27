from ConfigParser import SafeConfigParser


def load_config_file(connect_path):
    config = SafeConfigParser()
    config.read(connect_path)
    list_keys = {'database': config.get('db_connection', 'database'),
                 'port': config.get('db_connection', 'port'),
                 'host': config.get('db_connection', 'host'),
                 'sslmode': config.get('db_connection', 'sslmode'),
                 'user': config.get('db_connection', 'user'),
                 'password': config.get('db_connection', 'password')}
    return list_keys