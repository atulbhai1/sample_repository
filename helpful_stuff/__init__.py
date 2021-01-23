import platform
os = 'Unidentified'
if platform.system() == 'Linux':
    os = 'Linux'
elif platform.system() == 'Windows':
    os = 'Windows'
else:
    os = 'Mac'