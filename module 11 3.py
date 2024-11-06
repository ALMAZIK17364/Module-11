import inspect

def introspection_info(obj):
    obj_atributes = {'type': type(obj),'attributes' : inspect.getmembers(obj), 'module' : inspect.getmodule(obj)}

    return obj_atributes

number_info = introspection_info(42)
print(number_info)