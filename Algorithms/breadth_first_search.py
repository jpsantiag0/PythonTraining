from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []



def person_is_mango_seller(name):
    return name[-1] == "m"  # Verify person name ends with letter "m"

def breadth_first_search(name):
    search_queue = deque()  # creates a new queue
    search_queue += graph[name]  # Adds all your neighbors to the search queue
    searched = []  # array to keep track of searched elements

    while search_queue:  # queue isn't empty
        person = search_queue.popleft()  # grabs the first person off the queue
        if not person in searched:
            if person_is_mango_seller(person):  # Check if the person is a mango seller
                print(f"{person} is a mango seller!") # yes, they're a mango seller
                return True
            else:
                search_queue += graph[person] # No, they aren't. Add all of this person's friends to the search queue
                searched.append(person)
    return False  # if search queue is empty, no mango seller was found

breadth_first_search("you")