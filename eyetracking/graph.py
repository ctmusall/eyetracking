import flot

class Fx(flot.Series):
    data = [(1,2), (2,3), (3,4)]

class MyGraph(flot.Graph):
    fx = Fx()

my_Graph = MyGraph()
