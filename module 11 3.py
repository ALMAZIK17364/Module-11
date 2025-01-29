import inspect

def introspection_info(obj):
    attributes = []
    methods = []
    
    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            methods.append(attr)
        else:
            attributes.append(attr)

    obj_attributes = {
        'type': type(obj),
        'attributes': attributes,
        'methods': methods,
        'module': inspect.getmodule(obj)
    }

    return obj_attributes

number_info = introspection_info(42)
print(number_info)
