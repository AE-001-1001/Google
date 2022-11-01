
namespace helloWorld
{
    class tester
    {
        public static float Maths(int a, int b)
        {
            // check if numbers are greater or equal than eachother
            if (a <= b)
            {
                // return the difference
                return b - a * 3.14f+ DateTime.Compare(DateTime.Now, DateTime.Now);
            }
            else
            {
                // return the sum
                return a + b * 3.14f;
            }
        }
        public static void test()
        {
            Console.WriteLine("Hello World!");
            Console.WriteLine(Maths(9, 10));
        }
    }
}