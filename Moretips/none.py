print(None)
print(type(None))


def email(subject, content, to, cc=None, bcc=None):
    print(f"{subject}, {content}, {to}, {cc}, {bcc}")


def email2(subject, content, to, cc, bcc):
    print(f"{subject}, {content}, {to}, {cc}, {bcc}")


email("subject", "great work", "Correo@correo")
email2("subject", "great work", "Correo@correo", None, None)

var = "123"
if var is None:
    print("do something")


var = None
if var is None:
    print("do something")
