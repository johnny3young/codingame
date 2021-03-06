// Power of Thor - Episode 1
using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;

class Player
{
    static void Main(string[] args)
    {
        string[] inputs = Console.ReadLine().Split(' ');
        int lightX = int.Parse(inputs[0]); // the X position of the light of power
        int lightY = int.Parse(inputs[1]); // the Y position of the light of power
        int x = int.Parse(inputs[2]); // Thor's starting X position
        int y = int.Parse(inputs[3]); // Thor's starting Y position

        // game loop
        while (true)
        {
            int remainingTurns = int.Parse(Console.ReadLine()); // The remaining amount of turns Thor can move. Do not remove this line.
            var move = new StringBuilder();

            if (y < lightY)
            {
              move.Append('S');
              y++;
            }
            else if (y > lightY)
            {
              move.Append('N');
              y--;
            }

            if (x < lightX)
            {
              move.Append('E');
              x++;
            }
            else if (x > lightX)
            {
              move.Append('W');
              x--;
            }

            // A single line providing the move to be made: N NE E SE S SW W or NW
            Console.WriteLine(move.ToString());
        }
    }
}
