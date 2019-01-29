import ast

# string list > list
sl = "['a', 'b', 'c', 'd']"
converted_sl = ast.literal_eval(sl)
print(converted_sl, type(converted_sl))

sd = """{"a": 1, "b": 2, "c": 3, "d": 4}"""
converted_sd = ast.literal_eval(sd)
print(converted_sd, type(converted_sd))
