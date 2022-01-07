import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox 

class Map(object):
    def __init__(self):
        # 0:壁
        # 1:通路
        # 2:スタート
        # 3:でこぼこ道
        # 4:ながれていないトイレ
        # 5:和式
        # 6:洋式
        #13*13
        self.map = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,],
                             [0,3,1,1,1,0,4,1,1,1,0,6,0,],
                             [0,1,1,0,1,0,0,0,1,0,1,1,0,],
                             [0,1,0,0,1,1,0,1,1,1,1,1,0,],
                             [0,1,1,0,1,1,1,1,3,3,1,1,0,],
                             [0,1,1,1,1,0,1,1,1,0,1,0,0,],
                             [0,3,1,0,0,0,3,1,0,1,1,1,0,],
                             [0,3,1,0,1,1,3,1,1,1,3,1,0,],
                             [0,3,1,1,1,1,1,1,0,0,1,1,0,],
                             [0,1,1,0,1,0,0,1,3,3,3,3,0,],
                             [0,1,1,1,1,0,1,1,1,0,1,5,0,],
                             [0,2,1,1,0,0,0,1,1,1,1,1,0,],
                             [0,0,0,0,0,0,0,0,0,0,0,0,0,]])
        self.size = self.map.shape[0]
        self.init_pos = [1,1]
        self.goal_pos = [11,11]#(行,列)
        self.normal_goal_pos = [11,2]
        self.bad_goal_pos = [6,11]
        plt.figure(figsize=(7,7))

    def chack_movable(self,pos):
        up    = bool(self.map[12-pos[1]-1][pos[0]])
        down  = bool(self.map[12-pos[1]+1][pos[0]])
        right = bool(self.map[12-pos[1]][pos[0]+1])
        left  = bool(self.map[12-pos[1]][pos[0]-1])

        return([up,down,right,left])

    def plot(self,pos=[1,1],q_table=[]):
        gpoint = np.arange(0, self.size, 1)
        plt.vlines(gpoint, 0, self.size, linewidth=0.3, colors="k")
        plt.hlines(gpoint, 0, self.size, linewidth=0.3, colors="k")
        plt.xlim(0, self.size)
        plt.ylim(0, self.size)
        for i in range (self.size):
            for j in range (self.size):
                if self.map[12-j][i] == 0:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "k", alpha=0.9)
                elif self.map[12-j][i] == 1:
                    if q_table[i*13+j][np.argmax(q_table[i*13+j])] > 1.0:
                        plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "y", \
                                alpha=np.clip(q_table[i*13+j][np.argmax(q_table[i*13+j])]/100,0,0.9))
                        if np.argmax(q_table[i*13+j]) == 0: 
                            plt.text(i, j, "↑", size=20, alpha=np.clip(q_table[i*13+j][np.argmax(q_table[i*13+j])]/100,0,0.9))
                        elif np.argmax(q_table[i*13+j]) == 1: 
                            plt.text(i, j, "↓", size=20, alpha=np.clip(q_table[i*13+j][np.argmax(q_table[i*13+j])]/100,0,0.9))
                        elif np.argmax(q_table[i*13+j]) == 2: 
                            plt.text(i, j, "→", size=20, alpha=np.clip(q_table[i*13+j][np.argmax(q_table[i*13+j])]/100,0,0.9))
                        elif np.argmax(q_table[i*13+j]) == 3: 
                            plt.text(i, j, "←", size=20, alpha=np.clip(q_table[i*13+j][np.argmax(q_table[i*13+j])]/100,0,0.9))
                        else:pass
                    else:
                        pass
                elif self.map[12-j][i] == 2:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "g", alpha=0.5)
                elif self.map[12-j][i] == 3:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "k", alpha=0.5)
                    plt.text(i, j, "^", size=20)
                elif self.map[12-j][i] == 4:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "c", alpha=0.5)
                    plt.text(i, j, "✕", size=10)
                elif self.map[12-j][i] == 5:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "m", alpha=0.5)
                    plt.text(i, j, "△", size=15)
                elif self.map[12-j][i] == 6:
                    plt.axvspan(xmin=i, xmax=i+1, ymin=j/self.size, ymax=(j+1)/self.size, color = "b", alpha=0.5)
                    plt.text(i, j, "○", size=15)
                else:
                    pass
        plt.axvspan(xmin=pos[0], xmax=pos[0]+1, ymin=pos[1]/self.size, ymax=(pos[1]+1)/self.size,\
                    color = "r", alpha=0.5)
        plt.plot()
        plt.pause(0.001)
        plt.cla()
 

if __name__ == "__main__":
    Map().plot()
