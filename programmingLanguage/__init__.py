import sys
from sty import fg
from programmingLanguage import basic
def shell(comm):
    if "QUIT" in comm:
        quit()
    result, error = basic.run('<main>', comm)
    if error:
            return None, str(fg.da_red + error.as_string() + fg.rs)
    elif result: return result, None