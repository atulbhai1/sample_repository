import basic
from sty import fg
def shell(comm):

    result, error = basic.run('<main>', text)
    if error:
            return None, str(fg.da_red + error.as_string() + fg.rs)
    elif result: return result, None
while True:
    text = input('basic > ')
    result, error = shell(text)
    if error:print(error)
    elif result:
        print(result)