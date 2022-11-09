


using System.Drawing;
namespace BackEnd
{
    internal class Back
    {
        // create loading screen with cool animation
        // create main menu
        public static string Animation(string text)
        {
            string result = " ";
            for (int i = 0; i < text.Length; i++)
            {
                result += text[i];
                Console.Write(result);
                Thread.Sleep(100);
                Console.Clear();
            }
            return result;
        }
        public static void Reader(string args)
        {
            Console.WriteLine(args);
        }
        public static string Readinput(string prompt, int number)
        {
            return $"{prompt + " " + number}";
        }
        }
    }



namespace Program
{
    class Program
    {        
        public static string Stringify(string message,int number){
                        // create a variable that stores the input
            string input = BackEnd.Back.Readinput(message, number);
            //
            string[] array = new string[1];
            // assign id to array
            array[0] = input.Replace(" " , " | ");
            
            // print the input
            foreach (string item in array)
            {
                BackEnd.Back.Reader(item + " " + ((uint)number + 1) + " " + ((uint)number + 2) + " " + ((uint)number + 3) + " " + ((uint)number + 4) + " " + ((uint)number + 5) + " " + ((uint)number + 6) + " | ");
                foreach (char c in item)
                {
                    // create a loop for the console colors
                    foreach ( ConsoleColor color in Enum.GetValues(typeof(ConsoleColor)))
                    {
                        Console.Title = "Console Color: " + color;
                    if (c == '|')
                    {
                        Console.WriteLine(c);
                    }
                    else
                    {
                        // reassign the arrays value
                        Console.WriteLine(((byte)color + " " + item + " "));
                    }
                        Console.ForegroundColor = color;
                        Console.Write(c);
                        Thread.Sleep(10);
                    }
                    Thread.Sleep(25);
                    Console.Clear();
                }
            }
        return $"Done";
        }

        public static void Main()
        {
        // Main function that runs everything
        Console.Clear();
        BackEnd.Back.Animation("<Loading...>");
        Stringify("!", 0);
        Stringify("@", 1);
        Stringify("#", 2);
        Stringify("%", 3);
        Stringify("^", 4);
        Stringify("&", 5);
        Stringify("*", 6);
        Stringify("(", 7);
        Stringify(")", 8);
        Stringify("-", 9);
        Stringify("_", 10);
        Stringify("=", 11);
        Stringify("+", 12);
        Stringify("{", 13);
        Stringify("}", 14);
        Stringify("[", 15);
        Stringify("]", 16);
        Stringify(":", 17);
        Stringify(";", 18);
        Stringify("'", 19);
        Stringify("\"", 20);
        Stringify("|", 21);
        Stringify("\\", 22);
        Stringify(",", 23);
        Stringify(".", 24);
        Stringify("<", 25);
        Stringify(">", 26);
        Stringify("?", 27);
        Stringify("/", 28);
        Stringify("a", 29);
        Stringify("b", 30);
        Stringify("c", 31);
        Stringify("d", 32);
        Stringify("e", 33);
        Stringify("f", 34);
        Stringify("g", 35);
        Stringify("h", 36);
        Stringify("i", 37);
        Stringify("j", 38);
        Stringify("k", 39);
        Stringify("l", 40);
        Stringify("m", 41);
        Stringify("n", 42);
        Stringify("o", 43);
        Stringify("p", 44);
        Stringify("q", 45);
        Stringify("r", 46);
        Stringify("s", 47);
        Stringify("t", 48);
        Stringify("u", 49);
        Stringify("v", 50);
        Stringify("w", 51);
        Stringify("x", 52);
        Stringify("y", 53);
        Stringify("z", 54);
        }
        }
    }
