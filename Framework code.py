class Technology(object):
    
    def __init__(self, label, color = "red"):
        """Each technology should be constructed with
        a text label and a color for display purposes"""
        pass



class User(object):

    def __lt__(self, other):
        """this is a built in comparison function, so that
        user1 < user2 always returns False.  You may not need
        this method at all, but it can sometimes be handy
        for sorting lists that contain users without throwing
        errors"""
        return False
    
    def get_friends(self):
        """returns a list of the user's friends,
        which are also users"""
        pass

    def is_friend(self, other):
        """returns True if this User and other are friends.
            returns False otherwise"""
        pass

    def get_id(self):
        """Returns this User's id"""
        pass

    def get_tech(self):
        """Returns the Technology used by the User, or None if
        the User has no Technlology"""
        pass

    

class Graph(object):

    def __init__(self, population):
        """create a new graph with population users and no connections.
        no users in the new graph should have any technology"""
        pass

    def circle_connect(self, n):
        """connect each user i to the next n users, that is
        users (i+1)%population, (i+2)%population,...,
        (i+n)%population."""
        pass
            
    def random_connections(self, num_connections):
        """add num_connections new connections randomly to the graph"""
        pass

    def is_connected(self):
        """returns True if there is a path from every graph User to
        every other user"""
        pass

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
        pass
        
    def get_users(self):
        """returns a list containing the users in the graph, in
        order of their IDs"""
        pass
    


class GraphAnalyzer(object):
    def __init__(self, graph, my_tech):
        """Contruct a new analyzer to study a provided graph,
        where my_tech represents the given company's technology"""
        pass

    def choose_user(self):
        """returns a user that does not currently have
        a technology, to serve as a first-adopter for 
        this analyzer's technology"""
        pass
