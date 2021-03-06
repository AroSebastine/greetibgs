from page_functions import greetings


print(greetings.aro())


for greeting in greetings.Testing().greetings_list():
    print(greeting.title() + "!")
