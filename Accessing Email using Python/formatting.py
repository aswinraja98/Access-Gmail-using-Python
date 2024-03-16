msg_template = """Hello This is {name},and register your complaints at {website}. We are not going to help you but you no have no choice.""" # .format(name="Hades", website='ash.burn')

def format_msg(my_name="Hades", my_website="ash.burn"):
    my_msg = msg_template.format(name=my_name, website=my_website)
    return my_msg

print(format_msg())