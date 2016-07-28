import tkinter
import turtle
from time import sleep

class GraphImaginizer(object):
    def __init__(self, graph, techs, canvas=None, title="Social Graph", bg="orange"):
        self.graph = graph
        self.techs = techs
        if canvas == None:
            self.screen = turtle.Screen() #Default screen (created for us)
            self.screen.setup(width=.85, height=0.85, startx=None, starty=None)
        else:
            self.screen = turtle.TurtleScreen(canvas)
        self.screen.mode('logo')
        self.bg = bg
        if title != None: self.screen.title(title)
        if bg != None: self.screen.bgcolor(bg)
        #Consider registering a custom "Shape"
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()

    def set_graph(self):
        return self.graph
    
    def get_graph(self):
        return self.graph
    
    def drawGraph(self):
        """Plot users in the graph with friend-lines & tech color"""
        # First we will do a circular style plot because it is easier to
        #arrange.  Also, this draws fresh version each time, but might
        #make it simply "move" users around later???
        self.screen.reset()
        self.screen.bgcolor(self.bg)
        self.screen.setworldcoordinates(-100,-100,100,100)
        self.screen.delay(1)

        user_list = self.graph.get_users()
        num_users = len(user_list)
        if num_users == 0: return
        
        radius = turtle.Vec2D(80, 0)
        for u, user in enumerate(user_list):
            t = turtle.Turtle()
            user._turtle = t
            user._pos = radius.rotate(u * 360/num_users)
            t.penup();
            t.setpos(user._pos)
            #Apply color from tech
            tech = user.get_tech()
            if tech == None:
                t.color('black')
            else:
                t.color('blue')
                t.fillcolor(tech.color)
                t.begin_fill()
            t.pendown()
            t.circle(10)
            t.end_fill()
            t.hideturtle()
            t.penup()
            t.forward(5)
            t.write(user.get_id(), False, align="center")
        
        for u, user in enumerate(user_list):
            for friend in user.get_friends():
                t = turtle.Turtle() #Each friendship is a Turtle!!!
                t.penup()
                t.setpos(user._pos)
                t.pendown()
                t.setpos(friend._pos)
        
    def demo(population = 8, cConnect = 3, rConnect = 4):
        """Class method to demonstrate a little drawing action"""
        graph = Graph(population)
        graph.circle_connect(cConnect)
        graph.random_connections(rConnect)

        techs_list = [Technology('pythonTutor', 'blue'),
                      Technology('IDLE', 'pink')]
        user_list = graph.get_users()
        user_list[0].set_tech(techs_list[0])
        user_list[-1].set_tech(techs_list[1])
        
        gi = GraphImaginizer(graph, techs_list)
        gi.drawGraph()
        sleep(3)
        graph.time_step()
        gi.drawGraph()
        return gi

gr8 = GraphImaginizer.demo(8,3,4)
