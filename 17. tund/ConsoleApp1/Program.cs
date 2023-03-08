using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int esimenearv;
            int teinearv;
            string märk;

            Console.Write("Sisesta esimene arv: "); //ei pane reavahetust lõppu, saad vastata samal real
            esimenearv = int.Parse(Console.ReadLine()); //sama mis pythony int(input())
            Console.Write("Sisesta tehtemärk: ");
            märk = Console.ReadLine();
            Console.Write("Sisesta teine arv: ");
            teinearv = int.Parse(Console.ReadLine());

            int vastus = 0;

            switch(märk)
            {
                case "+":
                    vastus = esimenearv + teinearv;
                    break;
                case "-":
                    vastus = esimenearv - teinearv;
                    break;
                case "*":
                    vastus = esimenearv * teinearv;
                    break;
                case "/":
                    vastus = esimenearv / teinearv;
                    break;
            }

            Console.WriteLine(vastus.ToString());
            Console.ReadLine(); //et programm ei väljuks
        }
    }
}
