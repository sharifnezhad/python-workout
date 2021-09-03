class Actor:
    def list_actor():
        actors = []
        while True:
            name_actor=input('actor name: ').lower()
            actors.append(name_actor)
            if int(input('exit or add actor (0 / 1): '))==0:
                break

        return actors

