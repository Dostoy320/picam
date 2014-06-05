from subprocess import call


def build_command(name, ss, wb):
    location = " -o static/images/{name}".format(name=name)
    quality = " -q 80"
    shutter = " -ss {shutter_speed}".format(shutter_speed=ss)
    balance = " -awb {white_balance}".format(white_balance=wb)
    size = " -w 600 -h 400"
    return "raspistill -t 100" + location + quality + shutter + balance + size


def take_photo(command):
    call([command], shell=True)
