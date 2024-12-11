book = dict()
book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49

print(book)
print(book["avocado"])



phone_book = {}  # or phone_book = dict()
phone_book["jenny"] = 1234
phone_book["emergency"] = 911

print(phone_book["jenny"])


voted = {}

def check_voter(name):
    value = voted.get(name)

    if value:
        print(f"{name} Already voted")
    else:
        voted[name] = True
        print(f"Let {name} vote")

check_voter("tony")
check_voter("sam")
check_voter("tony")

