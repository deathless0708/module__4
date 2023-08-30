# # def strcounter(string):
# #     for symbol in string:
# #         counter = 0
# #         for syb_symbol in string:
# #             if symbol == syb_symbol:
# #                 counter += 1
# #         print(symbol, counter )
# #
# #
# # strcounter('abcde')
#
# # def strcounter(string):
# #     for symbol in set(string):
# #         counter = 0
# #         for syb_symbol in string:
# #             if symbol == syb_symbol:
# #                 counter += 1
# #         print(symbol, counter )
# #
# #
# # strcounter('abcde')
#
# def strcounter(string):
#     syms_counter = {}
#     for symbol in string:
#         syms_counter[symbol] = syms_counter.get(symbol, 0) + 1
#     print(syms_counter)
#
#     if string == string[::-1]:
#         print(True)
#     else:
#         print(False)
#
#
# #
#
#
# #31231
# #
# # def Asec():
#     pass
# strcounter('лепсспел')
#

def ask_26(a, b):
    return a>b

print(ask_26(10,16))