if re.match('.*terminal.*', window.get_active_class()):
    keyboard.send_keys("<shift>+<ctrl>+c")
else:
    keyboard.send_keys("<ctrl>+c")

