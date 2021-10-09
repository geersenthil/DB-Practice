class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0;
        int y = 0;
        int dir = 0;
        instructions = instructions + instructions + instructions + instructions;
        char path[] = instructions.toCharArray();
        for (int i=0; i < path.length; i++)  {
             char move = path[i];
            if (move == 'R')
                dir = (dir + 1)%4;
            else if (move == 'L')
                dir = (4 + dir - 1) % 4;
      else 
      {
                 if (dir == 0)
                    y++;
                 else if (dir == 1)
                    x++;
                 else if (dir == 2)
                    y--;
                 else 
                    x--;
              }
          }

        return (x == 0 && y == 0);
    }
}