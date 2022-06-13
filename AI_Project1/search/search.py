# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import searchAgents #imported for Q5

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    "*** YOUR CODE HERE ***"
    stack = util.Stack()
    closed = []
    stack_element = (problem.getStartState(), '', 0)
    stack.push(stack_element)
    while True:      
        if stack.isEmpty():
            raise Exception("Stack empty")

        stack_element = stack.pop()
            
        if problem.isGoalState(stack_element[0]):
            path = stack_element[1].split(" ")[1:]
            print(path)
            return path
        if stack_element[0] not in closed:
            closed.append(stack_element[0])
            for child in problem.getSuccessors(stack_element[0]):
                stack.push((child[0], stack_element[1] + " " + child[1], stack_element[2] +  child[2]))

    '''print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))'''

    
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    closed = []
    queue_element = (problem.getStartState(), '', 0)
    queue.push(queue_element)
    while True:      
        if queue.isEmpty():
            raise Exception("Queue empty")          #Works both with Q2 and Q5

        queue_element = queue.pop()

        if problem.isGoalState(queue_element[0]):
            path = queue_element[1].split(" ")[1:]
            return path
        if queue_element[0] not in closed:
            closed.append(queue_element[0])
            for child in problem.getSuccessors(queue_element[0]):
                queue.push((child[0], queue_element[1] + " " + child[1], queue_element[2] +  child[2]))
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    pqueue = util.PriorityQueue()

    closed = []
    pqueue_element = (problem.getStartState(), '', 0)
    pqueue.push(pqueue_element, 0)
    while True:      
        if pqueue.isEmpty():
            raise Exception("Queue empty")

        pqueue_element = pqueue.pop()
            
        if problem.isGoalState(pqueue_element[0]):
            path = pqueue_element[1].split(" ")[1:]
            return path
        if pqueue_element[0] not in closed:
            closed.append(pqueue_element[0])
            for child in problem.getSuccessors(pqueue_element[0]):
                pqueue.push((child[0], pqueue_element[1] + " " + child[1], pqueue_element[2] +  child[2]), pqueue_element[2] +  child[2])

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pqueue = util.PriorityQueue()

    closed = []
    pqueue_element = (problem.getStartState(), '', heuristic(problem.getStartState(), problem))
    pqueue.push(pqueue_element, heuristic(problem.getStartState(), problem))
    while True:      
        if pqueue.isEmpty():
            raise Exception("Queue empty")
        
        pqueue_element = pqueue.pop()       #works with both Q4, Q6

        if problem.isGoalState(pqueue_element[0]):
            path = pqueue_element[1].split(" ")[1:]
            return path
        if pqueue_element[0] not in closed:
            closed.append(pqueue_element[0])
            for child in problem.getSuccessors(pqueue_element[0]):
                total_cost = pqueue_element[2] +  child[2] + heuristic(child[0], problem) - heuristic(pqueue_element[0], problem)
                pqueue.push((child[0], pqueue_element[1] + " " + child[1], total_cost), total_cost)
                #print(f'State {pqueue_element[0][0]} {pqueue_element[0][1].asList()} childState {child[0][0]} {child[0][1].asList()} heu of state+1 {heuristic(pqueue_element[0], problem) + 1} heu of child {heuristic(child[0], problem)}')
            
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
