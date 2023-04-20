stage = 'open_main_menu'


def get_settings():
    settings_file = open("Resources/Settings.txt")
    settings_ = []
    for i in settings_file:
        settings_.append(i.rstrip())
    settings_file.close()
    if len(settings_) < 4:
        settings_.clear()
        settings_.append('unknown')
        settings_.append('red')
        settings_.append('black')
        settings_.append('40')
        settings_file = open("Resources/Settings.txt", 'w')
        settings_file.write(settings_[0] + '\n' + settings_[1] + '\n' + settings_[2] + '\n' + settings_[3])
        settings_file.close()
    return settings_


def set_settings(settings):
    settings_file = open("Resources/Settings.txt", 'w')
    new_content = str()
    for i in settings:
        new_content += i + '\n'
    settings_file.write(new_content)
    settings_file.close()
