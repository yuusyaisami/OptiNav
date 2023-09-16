class OptiNav:
    def __init__(self) -> None:
        pass

    def OptimalNavigation(self, array, player_position, goal_position, movableBlockType, obstacleBlockType):
        self.map = array
        self.player_position = player_position
        self.movableBlockType = movableBlockType
        self.obstacleBlockType = obstacleBlockType
        self.player_position
        self.Optimal_Routes = []
        for r in range(len(self.map)): # 進めるブロックと進めないブロックをマップに代入
            for c in range(len(self.map[r])):
                for movable in movableBlockType:
                    if movable == self.map[r][c]:
                        self.map[r][c] = 0
                for obstacle in obstacleBlockType:
                    if obstacle == self.map[r][c]:
                        self.map[r][c] = 999
        self.map[player_position[1]][player_position[0]] = 1 # プレイヤーの位置
        # self.map[goal_position[1]][goal_position[0]] = 998 # goalの位置
        self.goal_position = goal_position
        self.ValueAssigner()
        self.OptimalRoute()
        return self.Optimal_Routes

    def ValueAssigner(self):
        i = 1
        while True:
            isDoValueAssign = False
            isEscape = False
            for r in range(len(self.map)):
                for c in range(len(self.map[r])):
                    if self.map[r][c] == i: # 上下または左右に、次の数値が入れられるか確認する
                        if r != 0: # 上
                            if self.map[r - 1][c] == 0: # 何もあてはめられていない、進めるブロック
                                if r - 1 == self.goal_position[1] and c == self.goal_position[0]: # 次の地点がgoal
                                    isEscape = True
                                    break
                                self.map[r - 1][c] = i + 1
                                isDoValueAssign = True
                        if r != len(self.map) - 1: # 下 (len()はインデックスより +1 されているから)
                            if self.map[r + 1][c] == 0:
                                if r + 1 == self.goal_position[1] and c == self.goal_position[0]: # 次の地点がgoal
                                    isEscape = True
                                    break
                                self.map[r + 1][c] = i + 1
                                isDoValueAssign = True
                        if c != 0: # 左
                            if self.map[r][c - 1] == 0:
                                if r == self.goal_position[1] and c - 1 == self.goal_position[0]: # 次の地点がgoal
                                    isEscape = True
                                    break
                                self.map[r][c - 1] = i + 1
                                isDoValueAssign = True
                        if c != len(self.map[r]) - 1: # 右
                            if self.map[r][c + 1] == 0:
                                if r == self.goal_position[1] and c + 1 == self.goal_position[0]: # 次の地点がgoal
                                    isEscape = True
                                    break
                                self.map[r][c + 1] = i + 1
                                isDoValueAssign = True
            i += 1
            if not isDoValueAssign or isEscape: # 一度も
                self.map[self.goal_position[1]][self.goal_position[0]] = 998 # goalの位置
                return

    def OptimalRoute(self):
        self.Optimal_Routes.insert(0, (self.goal_position[0], self.goal_position[1])) # goalのインデックスを挿入
        r = self.goal_position[1] # 現在の地点
        c = self.goal_position[0]

        index = 999 # 現在の数値
        move_index = (0,0) # 候補先
        while True:
            if r != 0: # 上 もしインデックスよりマップ数値のほうが小さかったら
                if index > self.map[r - 1][c] and self.map[r - 1][c] != 0:
                    move_index = c, r - 1
            if r != len(self.map) - 1: # 下
                if index > self.map[r + 1][c] and self.map[r + 1][c] != 0:
                    move_index = c, r + 1
            if c != 0: # 右
                if index > self.map[r][c - 1] and self.map[r][c - 1] != 0:
                    move_index = c - 1, r
            if c != len(self.map[r]) - 1: # 右
                if index > self.map[r][c + 1] and self.map[r][c + 1] != 0:
                    move_index = c + 1, r
            x, y = move_index
            if r == x and c == y: # 一度も数値のあてはめが行われなかったら
                return
            self.Optimal_Routes.insert(0, (x, y)) # 数値をOptimal_Routesにインサートする
            r = y # 候補先の位置を現在の位置にする
            c = x
            index = self.map[r][c] # 候補先の数値を現在の数値にする
def main():
    opti_nav = OptiNav()
    map = [[1,1,1,1,1,1,1],
           [1,0,0,0,1,0,1],
           [1,0,1,0,0,0,1],
           [1,0,0,0,1,0,1],
           [1,1,1,0,1,0,1],]
    optinav_array = opti_nav.OptimalNavigation(map,[1,1],[5,1],[0],[1])
    print(optinav_array)
    
if __name__ == '__main__':
    main()
