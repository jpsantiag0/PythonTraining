graph={}
graph["start"] = {}
graph["start"]["a"] = 2
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

print(graph["start"].keys())

infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None

processed = []