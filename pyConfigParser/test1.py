from ConfigParser import SafeConfigParser

def initEntryInfo(iniFile="entry.ini"):
    entries = {}
    with file(iniFile, "r") as configFile:
        config = SafeConfigParser()
        config.readfp(configFile)
        
        for section in config.sections():
            if section[:5] == "entry":
                entryID = int(section.split("_")[1])
                entries[entryID] = {
                    "db_host" : config.get(section, "db_host"),
                    "db" : config.get(section, "db"),
                    "user" : config.get(section, "user"),
                    "passwd" : config.get(section, "passwd"),
                }
    
    for entryID, entryInfo in entries.iteritems():
        connections.databases['entry_%s' % entryID] = {
            'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME' : entryInfo['db'],
            'USER': entryInfo['user'],
            'PASSWORD': entryInfo['passwd'],
            'HOST': entryInfo['db_host'],    # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            'PORT': '',                      # Set to empty string for default.
        }
        
    return entries


def ooo(iniFile="entry.ini"):
    entries = {}
    with file(iniFile, 'r') as configFile:
        config = SafeConfigParser()
        config.readfp(configFile)

    for section in config.sections():
        if section[:5] == 'entry':
            entryID = int(section.split("_")[1])
            entries[entryID] = {
                "db_host" : config.get(section, "db_host"),
                "db" : config.get(section, "db"),
                "user" : config.get(section, "user"),
                "passwd" : config.get(section, "passwd"),
            }
    print entries
    for s in entries:
        print s
ooo()