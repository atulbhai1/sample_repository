import basic
from sty import fg
def shell():
    text = ''
    while True:
        text = input('basic > ')
        result, error = basic.run('<main>', text)
        if error:
            print(fg.da_red + error.as_string() + fg.rs)
        elif result: print(result)
shell()