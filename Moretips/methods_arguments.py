def example_method(mandatory_parameter, default_parameter="Default", *args, **kwargs):
    print(f"""
    mandatory_parameter = {mandatory_parameter}
    default_parameter = {default_parameter}
    args = {args}
    kwargs = {kwargs}
    """)


   # example_method()
example_method(15)
example_method(mandatory_parameter=10)
example_method(25, 45)
example_method(25, "Ana")
example_method(25, "String 1", "String 2", "string 3")
