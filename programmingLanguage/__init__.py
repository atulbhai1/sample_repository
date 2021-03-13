import basic
from sty import fg
def shell():
    text = ''
    while text != 'quit':
        text = input('basic > ')
        if text == 'quit':continue
        result, error = basic.run('<main>', text)
        if error:
            print(fg.da_red + error.as_string() + fg.rs)
        else: print(result)
shell()