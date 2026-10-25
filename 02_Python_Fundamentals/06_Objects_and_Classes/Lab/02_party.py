class Party:
    def __init__(self):
        self.people = []

party_list = Party()

while True:
    name = input()
    if name == "End":
        print(f"Going: {', '.join(party_list.people)}")
        print(f"Total: {len(party_list.people)}")
        break

    party_list.people.append(name)