class Agent(object):
    def __init__(self, init_pos = [1,1], goal_pos = [11,11], normal_pos = [11,2], bad_pos = [6,11]):
        self.pos = [init_pos[0], init_pos[1]]
        self.goal_pos = goal_pos
        self.normal_goal_pos = normal_pos
        self.bad_goal_pos = bad_pos
        self.action_space = 4
        self.done = False

    def action(self,a,d):
        if a == 0 and d[0]:
            self.pos[1] += 1
        elif a == 1 and d[1]:
            self.pos[1] -= 1
        elif a == 2 and d[2]:
            self.pos[0] += 1
        elif a == 3 and d[3]:
            self.pos[0] -= 1
        else:
            pass
    
    def get_state(self):
        state = self.pos[0]*13 + self.pos[1]
        return state 

    def check_done(self):
        if self.pos[0] == self.goal_pos[0] and self.pos[1] == self.goal_pos[1]:
            done = True
        elif self.pos[0] == self.normal_goal_pos[0] and self.pos[1] == self.normal_goal_pos[1]:
            done = True
        elif self.pos[0] == self.bad_goal_pos[0] and self.pos[1] == self.bad_goal_pos[1]:
            done = True
        else:
            done = False
        return done

"""
class Agent():
    def __init__(self, start=[1,1], goal=[11,11], normal_goal=[11,2], bad_goal=[6,11]):
        self.start = start
        self.goal_pos = goal_pos
        self.normal_goal_pos = normal_pos
        self.bad_goal_pos = bad_pos
        self.action_space = 4
        
    def action(self):
        s

"""
