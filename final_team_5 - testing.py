## Team 5
## Team members: Jianguo Li    Tiancong,Gu    Ziguang,Niu

import random
class Technology(object):
    
    def __init__(self, label, color = "red"):
        """Each technology should be constructed with
         a text label and a color for display purposes"""
        self.label=label
        self.color=color


class User(object):

    def __lt__(self, other):
        """this is a built in comparison function, so that
        user1 < user2 always returns False.  You may not need
        this method at all, but it can sometimes be handy
        for sorting lists that contain users without throwing
        errors"""
        return False

    def __init__(self,number):
        self.user_id = number
        self.tech = None

    def get_friends(self): 
        """returns a list of the user's friends,
        which are also users"""
        self.friend_list = []
        for i in range(len(Graph.final_matrix)):
            if Graph.final_matrix[self.user_id][i] == 1:
                self.friend_list.append(Graph.user_list[i])
        return self.friend_list

    def is_friend(self, other):
        """returns True if this User and other are friends.
            returns False otherwise"""
        if other in self.get_friends():
            return True
        else:
            return False

    def get_id(self):
        """Returns this User's id"""
        return self.user_id

    def get_tech(self): 
        """Returns the Technology used by the User, or None if
        the User has no Technlology"""
        return self.tech

    

class Graph(object):
    

    def __init__(self, population):
        """create a new graph with population users and no connections.
        no users in the new graph should have any technology"""
        self.population = population
        self.userlist = []
        for i in range(self.population):
            temp = User(i)
            self.userlist.append(temp)
        self.matrix = []
        for i in range(self.population):
            self.matrix.append([])
            for j in range(self.population):
                self.matrix[i].append(0)
        Graph.final_matrix = self.matrix
        Graph.user_list = self.userlist
        
    def circle_connect(self, n):
        """connect each user i to the next n users, that is
        users (i+1)%population, (i+2)%population,...,
        (i+n)%population."""
        self.n=n
        for i in range (0,self.population):
            for j in range (1,self.n+1):
                self.matrix[i][(i+j)%self.population]=1
                self.matrix[(i+j)%self.population][i]=1
            
    def random_connections(self, num_connections):
        """add num_connections new connections randomly to the graph"""
        self.num_connections = num_connections
        i = self.num_connections
        while i > 0:
            j = random.randint(0,self.population-1)
            k = random.randint(0,self.population-1)
            if self.matrix[j][k] == 0 and j!= k:
                self.matrix[j][k] = 1
                self.matrix[k][j] = 1
                i -= 1
            flag=0
            for a in range (0,self.population):
                for b in range (0,self.population):
                    if self.matrix[a][b]==0 and a!=b:
                        flag=1
            if flag==0:
                break

    def is_connected(self):
        """returns True if there is a path from every graph User to
        every other user"""
        def path(position_number,final_number):
            for i in range(position_number + 1,self.population):
                if self.matrix[position_number][i] == 1:
                    if i == final_number:
                        return 1
                    else:
                        judge = path(i,final_number)
                        if judge == 1:
                            return 1
            return 0
        position_number = 0
        for final_number in  range(1,self.population):
            final_judge = path(position_number,final_number)
            if final_judge == 0:
                return False
        if final_judge == 1:
            return True

    def time_step(self):
        """move the simulation forward by one time period.
        Each user adopts the most popular technology among
        themselves and their friends.  If there are multiple
        technologies that are tied for most popular, the user
        selects one at random."""
        # To find the most common tech in a subset of users,
        # you cannot build a frequency table using a
        # dictionary since Technologies are mutable objects.
        # If you want to follow a similar strategy, you can
        # import the collections package and use a Counter
        # object, which works like a (slow) dictionary for
        # mutable objects.  However, there are many other
        # strategies that you could use to do the same thing.
        self.final_tech = []
        for i in range (self.population):
            if self.userlist[i].get_tech() == None:
                self.friends_tech = []
                n = 0
                for j in range(len(self.userlist[i].get_friends())):
                    if self.userlist[i].get_friends()[j].get_tech() != None:
                        self.friends_tech.append(self.userlist[i].get_friends()[j].get_tech())
                count_list = [0 for i in range(len(self.friends_tech))]
                
                for k in range(len(self.friends_tech)):
                    for times in range(len(self.friends_tech)):
                        if self.friends_tech[k] == self.friends_tech[times]:
                            count_list[k] = count_list[k] + 1
                max = 0
                for count_times in range(len(self.friends_tech)):
                    if count_list[count_times] > max:
                        max = count_list[count_times]
                        n = count_times
                if self.friends_tech != []: 
                    self.final_tech.append(self.friends_tech[n])
                else:
                    self.final_tech.append("0")
            else:
                self.final_tech.append(self.userlist[i].get_tech())
        for count_time in range(self.population):
            if self.final_tech[count_time] != '0':
                self.userlist[count_time].tech = self.final_tech[count_time]
            if self.userlist[count_time].get_tech() != None:
                print(self.userlist[count_time].get_tech().label)
            else:
                print(self.userlist[count_time].get_tech()) 
        
    def get_users(self):
        """returns a list containing the users in the graph, in
        order of their IDs"""
        self.user = []
        for i in range(0,self.population):
            self.user.append(self.userlist[i])
        return self.user
    


class GraphAnalyzer(object):

    def __init__(self, graph, my_tech):
        """Contruct a new analyzer to study a provided graph,
        where my_tech represents the given company's technology"""
        self.graph=graph
        self.my_tech=my_tech
        self.matrix = []
        self.userid=0
        self.userfriend=[]
        self.N=0
        for i in range(self.graph.population):
            self.matrix.append([])
            for j in range(self.graph.population):
                self.matrix[i].append(0)
        self.user_list=self.graph.get_users()
        for i in range (0,self.graph.population):
            self.userid = self.user_list[i].get_id()
            self.userfriend = self.user_list[i].get_friends()
            self.N = len(self.userfriend)
            for j in self.userfriend:
                self.matrix[j.get_id()][self.userid] = 1/self.N
        self.vector = []
        
    def choose_user(self):
        """returns a user that does not currently have
        a technology, to serve as a first-adopter for
        this analyzer's technology"""
        def matrixMul(A, B):
            res = [[0] * len(B[0]) for i in range(len(A))]
            for i in range(len(A)):
                for j in range(len(B[0])):
                    for k in range(len(B)):
                        if A[i][k] * B[k][j] != 0:
                            res[i][j] += A[i][k] * B[k][j]
            return res
        
        self.vector = [[1 / len(self.matrix)] for i in range(len(self.matrix))]
        count = 0
        while count < 15:
            self.vector =  matrixMul(self.matrix,self.vector)
            count = count + 1

        flag = 0
        while flag == 0:
            for i in range(0,self.graph.population):
                if self.vector[i] == max(self.vector):
                    locat = i
            if self.user_list[locat].tech == None:
                mvp_user = self.user_list[locat]
                self.vector[locat] = [0]
                self.user_list[locat].tech = self.my_tech
                flag = 1
            else:
                self.vector[locat] = [0]   
        return mvp_user



population = int(input("Enter the population:"))
graph_1 = Graph(population)
n = int(input("Enter circle connection number:"))
graph_1.circle_connect(n)
num_connections = int(input("Enter random connection number:"))
graph_1.random_connections(num_connections)

label = input("Technology label:")
label2 = input("Technology label:")
technology = Technology(label)
technology2 = Technology(label2)

analyzer = GraphAnalyzer(graph_1,technology)
analyzer.choose_user()
print(analyzer.vector)
analyzer = GraphAnalyzer(graph_1,technology)
analyzer.choose_user()
print(analyzer.vector)
analyzer = GraphAnalyzer(graph_1,technology)
analyzer.choose_user()
print(analyzer.vector)
analyzer = GraphAnalyzer(graph_1,technology2)
analyzer.choose_user()
print(analyzer.vector)
analyzer = GraphAnalyzer(graph_1,technology2)
analyzer.choose_user()
print(analyzer.vector)
analyzer = GraphAnalyzer(graph_1,technology2)
analyzer.choose_user()
print(analyzer.vector)

flag = 0
while flag == 0:
    gogo = input("For next step(yes or no):")
    if gogo == "yes":
        analyzer.graph.time_step()
    else:
        flag = 1
    counter1 = 0
    counter2 = 0
    for i in range(0,analyzer.graph.population):
        if analyzer.user_list[i].tech == technology:
            counter1 += 1
        if analyzer.user_list[i].tech == technology2:
            counter2 += 1
    print("The number of",label,':',counter1)
    print("The number of",label2,':',counter2)
        

