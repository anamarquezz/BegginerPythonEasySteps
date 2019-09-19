def example_method(mandatory_parameter, default_parameter="Default", *args, **kwargs):
    print(f"""
    mandatory_parameter = {mandatory_parameter} {type(mandatory_parameter)}
    default_parameter = {default_parameter} {type(default_parameter)}
    args = {args} {type(args)}
    kwargs = {kwargs} {type(kwargs)}
    """)

   # example_method()
example_method(15)
example_method(mandatory_parameter=10)
example_method(25, 45)
example_method(25, "Ana")
example_method(25, "String 1", "String 2", "string 3")
example_method(25, "String 1", "String 2", "string 3", key='a', key2='b')
example_method(25, "String 1", key='a', key2='b')
example_method(key='a', key2='b', mandatory_parameter=25,
               default_parameter="String 1")
example_method(key='a', key2='b', mandatory_parameter=25,
               default_parameter="String 1")

example_list = [1, 2, 3, 4, 5, 6]
example_method(example_list[0], example_list[1], example_list[2])
example_method(*example_list)  # all values pass as arguments

# keyworkarguments
example_dict = {'a': '1', 'b': '2'}
example_method(*example_list, **example_dict)
