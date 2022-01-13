import numpy as np
from map import Map
from agent import Agent


def decide_action(next_state, episode, q_table):
    first = 0.8
    epsilon = first * (1/(episode+1))
    #εグリーディ方策
    if epsilon <= np.random.uniform(0,1):
        next_action = np.argmax(q_table[next_state])
    else:
        next_action = np.random.choice(range(4))
    return next_action


def update(q_table, state, action, reward, next_state):
    next_q_max = np.argmax(q_table[next_state])
    gamma = 0.5
    alpha = 0.5
    q_table[state, action] = (1-alpha)*q_table[state, action] + alpha*(reward + gamma * next_q_max)
    return q_table


def reward(end_or_yet, state, next_state, _map):
    boko = []
    for i in range(_map.shape[0]):
        for j in range(_map.shape[1]):
            if _map[12-j][i] == 3:
                boko.append([12-j,i])

    #座標変換
    state_ = [state//13,state%13]
    next_state_ = [next_state//13,next_state%13]

    for boko_ in boko:
        if state_ == boko_:
            reward = -30
            break
        else:
            reward = 30

    if end_or_yet and next_state_ == [11,11]:
        reward = 150
    elif end_or_yet and next_state_ == [11,2]:
        reward = 70
    elif end_or_yet and next_state_ == [6,11]:
        reward = 40
    elif state == next_state:
        reward = -10
    else:
        reward = -1
    return reward


def main(): 
    map_init = Map()
    agent = Agent()
    max_episode = 100
    num_step = 300
    q_table = np.random.uniform(low=-1, high=1, size=(map_init.size**2, agent.action_space))

    for episode in range(max_episode):
        agent = Agent(map_init.init_pos)
        state = agent.get_state()
        choice_action = np.argmax(q_table[state])
        count = 0

        #step
        for i in range(num_step):
            direction = map_init.check_move(agent.pos)
            agent.action(choice_action, direction)
            end_or_yet = agent.check_done()
            next_state = agent.get_state()
            get_reward = reward(end_or_yet, state, next_state, map_init.map)
            count += get_reward
            q_table = update(q_table, state, choice_action, get_reward, next_state)
            choice_action = decide_action(next_state, episode, q_table)
            state = next_state
            map_init.plot(agent.pos, q_table)
            if end_or_yet:
                break
        print("episode %5d, reward %6d, step %5d" %(episode+1,count,i+1))

if __name__ == '__main__':
    main()
