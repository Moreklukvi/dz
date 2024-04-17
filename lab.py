class Player:
    Player = [1,1]
 
    def moveRight(self):
        new_pose = [Player[0]+1,Player[1]]
        if Maze[new_pose[0]][new_pose[1]] == 0:
            Player = new_pose
 
    def moveLeft(self):
        new_pose = [Player[0]-1,Player[1]]
        if Maze[new_pose[0]][new_pose[1]] == 0:
            Player = new_pose
 
    def moveUp(self):
        new_pose = [Player[0],Player[1]+1]
        if Maze[new_pose[0]][new_pose[1]] == 0:
            Player = new_pose
 
    def moveDown(self):
        new_pose = [Player[0],Player[1]-1]
        if Maze[new_pose[0]][new_pose[1]] == 0:
            Player = new_pose
 
class Maze:
    def __init__(self):
       self.maze = [[0,0,0,0,1],
                     [1,1,1,0,1],
                     [1,0,1,0,1],
                     [1,0,0,0,1],
                     [1,0,1,1,1]]
