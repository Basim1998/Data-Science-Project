import GameEnv
import numpy as np
from ddqn_keras import DDQNAgent
import random, math

TOTAL_GAMETIME = 1000 # Max game time for one episode
N_EPISODES = 10000
REPLACE_TARGET = 50 

game = GameEnv.RacingEnv()

ddqn_agent = DDQNAgent(alpha=0.0005, gamma=0.99, n_actions=5, epsilon=1.00, epsilon_end=0.10, epsilon_dec=0.9995, replace_target= REPLACE_TARGET, batch_size=512, input_dims=19)

# Load the saved model
ddqn_agent.load_model()

ddqn_scores = []
eps_history = []

def run():

    for e in range(N_EPISODES):
        
        game.reset() #reset env 

        done = False
        score = 0
        
        observation_, reward, done = game.step(0)
        observation = np.array(observation_)

        gtime = 0 # set game time back to 0
        
        while not done:
            
            action = ddqn_agent.choose_action(observation)
            observation_, reward, done = game.step(action)
            observation_ = np.array(observation_)

            score += reward
            observation = observation_
            
            gtime += 1

            if gtime >= TOTAL_GAMETIME:
                done = True

        ddqn_scores.append(score)

        if e % REPLACE_TARGET == 0 and e > REPLACE_TARGET:
            ddqn_agent.update_network_parameters()

        if e % 10 == 0 and e > 10:
            ddqn_agent.save_model()
            print("save model")
            
        print('episode: ', e,'score: %.2f' % score,
              ' average score %.2f' % np.mean(ddqn_scores[max(0, e-100):(e+1)]),
              ' epsolon: ', ddqn_agent.epsilon,
              ' memory size', ddqn_agent.memory.mem_cntr % ddqn_agent.memory.mem_size)   

    # Calculate and print the average score
    avg_score = np.mean(ddqn_scores)
    print("Average Score:", avg_score)

run()
