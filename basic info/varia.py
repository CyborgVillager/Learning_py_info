#variables

def story_example():
        name = "John"
       
        age = 25
        para0 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In interdum, odio et feugiat auctor, ante leo t" \
                "incidunt tortor, sed lacinia leo augue vel lorem. In rutrum est libero"
        para1 = "Nunc euismod magna in diam finibus sollicitudin. Aliquam commodo tortor lorem, in tincidunt quam dapibus " \
                "fringilla. Duis vitae sem ut ligula efficitur varius."

        print(name, 'is age', str(age),  para0, '\n', name, para1)


def story_start():
        story_example()


story_start()