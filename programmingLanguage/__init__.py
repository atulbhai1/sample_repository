import basic, sys
from sty import fg
if not sys.stdin.isatty():
    print(str(fg.da_red + 'Use terminal for access to clear function' + fg.rs))
def shell(comm):
    if "QUIT" in comm:
        quit()
    result, error = basic.run('<main>', comm)
    if error:
            return None, str(fg.da_red + error.as_string() + fg.rs)
    elif result: return result, None
while True:
    text = input('basic > ')
    result, error = shell(text)
    if error:print(error)
    elif result:
        print(result)
#############################################################
#
#os.chdir('/Users/srinivasansrinivasan/PycharmProjects/sample_repository')
#
#
#        def execute_terminal(self, exec_ctx):
#         comm = exec_ctx.symbol_table.get('comm')
#         if isinstance(comm, String):
#             d = os.system(str(comm))
#             if d:
#                 return RTResult().success(String(str(d)))
#             return RTResult().success(String('Command Executed Successfully!'))
#         else:
#             return RTResult().failure(RTError(self.pos_start, self.pos_end, 'System commands have to be in String format', String('String Needed')))
#     execute_terminal.arg_names = ['comm']
#
#
#BuiltInFunction.terminal = BuiltInFunction('terminal')
#
#
#global_symbol_table.set('TERMINAL', BuiltInFunction.terminal)
#
