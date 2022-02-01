global Preferences
Preferences = {
    'appsettings':{
        'theme':'light',
        'region':'india',
    },
    'usersettings':{
        'rememberID':'yes',
    }

}

def provide(dict_name,property):
    return Preferences[dict_name][property]


