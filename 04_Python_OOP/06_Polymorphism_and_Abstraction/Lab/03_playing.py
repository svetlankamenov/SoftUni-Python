def start_playing(o: object):
    return o.play()

class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))