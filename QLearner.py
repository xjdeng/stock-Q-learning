import random

class QLearner(object):
    def __init__(self, q0, actions, learning = 0.5, discount = 0.5):
        self.actions = actions
        self.learning = learning
        self.discount = discount
        self.Q = q0
        self.A = None
        self.newQ = -9999999999999
        self.state0 = None
        self.action0 = None
        self.reward0 = None
    
    def reset(self):
        if (self.state0, self.action0, self.reward0) != (None, None, None):
            oldQ = self.Q[(self.state0,self.action0)]
            self.Q[(self.state0,self.action0)] = oldQ + self.learning*(self.reward0 - oldQ)
        (self.state0, self.action0, self.reward0) = (None, None, None)
    
    def pickAction(self, state):
        self.newQ = -9999999999999999999
        (j,k) = (0,0)
        self.A = None
        while (k < len(self.actions)) & (j == 0):
            if self.Q[(state,self.actions[0])] == self.Q[(state,self.actions[k])]:
                j = 1
            k += 1
        if j == 0:
            self.A = random.choice(self.actions)
        else:
            for i2 in self.actions:
                if self.Q[(state,i2)] >= self.newQ:
                    self.newQ = self.Q[(state,i2)]
                    self.A = i2
        return self.A
    
    def updateState(self, state, reward, newAction = None):
        if newAction is not None:
            self.A = newAction
        if (self.state0, self.action0, self.reward0) != (None, None, None):
            oldQ = self.Q[(self.state0,self.action0)]
            self.Q[(self.state0, self.action0)] = (1-self.learning)*oldQ + self.learning*(self.reward0 + self.discount*self.newQ)
        (self.state0, self.action0, self.reward0) = (state, self.A, reward)
        