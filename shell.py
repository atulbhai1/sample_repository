import programmingLanguage, sys
from sty import fg
if not sys.stdin.isatty():
    print(str(fg.da_red + 'Use terminal for access to clear function' + fg.rs))
while True:
    text = input('basic > ')
    result, error = programmingLanguage.shell(text)
    if error:print(error)
    elif result:
        print(result)
