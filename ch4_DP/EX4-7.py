'''
Autor: Zel
Email: 2995441811@qq.com
Date: 2022-04-14 21:21:01
LastEditors: Zel
LastEditTime: 2022-04-15 19:10:58
'''
import numpy as np
import matplotlib.pyplot as plt

"""
    Jack's car rental problem
"""
iterate_num = 0
max_iterate_num = 100
poisson_lam1 = (3, 3)
poisson_lam2 = (4, 2)

class PoissonGenerator(object):
    
    def __init__(self, lambd) -> None:
        self.set = np.random.poisson(lam=lambd, size=max_iterate_num)
        self.index = 0
        
    def new(self):
        if self.index == max_iterate_num:
            return None
        return self.set[self.index]

class Agent(object):
    def __init__(self) -> None:
        self.policy = np.zeros((21, 21)) # 策略
        self.V = np.zeros((21, 21)) # 价值函数
        self.gamma = 0.9 # 衰减因数
        
        
class Problem(object):
    
    def __init__(self) -> None:
        self.state_domain = []
        
        for i in range(21):
            for j in range(21):
                self.state_domain.append((i, j))
        self.rental_num1_gnrt = PoissonGenerator(poisson_lam1[0])
        self.rental_num2_gnrt = PoissonGenerator(poisson_lam1[1])
        self.return_num1_gnrt = PoissonGenerator(poisson_lam2[0])
        self.return_num2_gnrt = PoissonGenerator(poisson_lam2[1])      
        
    def response(state, action)->list[tuple(3)]:
        reward = []

def main():
    A = Agent()
    P = Problem()
    policy_iteration(A, P)

def policy_iteration(a:Agent, pb:Problem):
    pass
    

def policy_evaluation(a:Agent, pb:Problem):
    Delta = 0
    theta = 0.1
    
    for i, j in pb.state_domain:
        v = a.V[i, j]
        a.V[i, j] = 1


def policy_improvement(a:Agent, pb:Problem):
    pass

if __name__ == '__main__':
    main()