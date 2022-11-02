using System.Net;


namespace helloWorld
{
    class tester
    {
        private static float Maths(int a, int b)
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
        // create a function that prints out the system type, the users name, the time, and ip address, and current website device is on given field
        public static void teste2r()
        {
            
            // print out the system type
            Console.WriteLine("System Type: " + Environment.OSVersion);
            
            // print out the users name
            Console.WriteLine("User Name: " + Environment.UserName);
            
            // print out the time
            Console.WriteLine("Time: " + DateTime.Now);
            
            // print out the ip address
            Console.WriteLine("IP Address: " + Dns.GetHostAddressesAsync("www.tcusd3.org").Result[0]);
            
            // print out the current website device is on
            foreach(var x in System.Net.Dns.GetHostEntryAsync("www.twitter.com").Result.AddressList)
            {
            // print out each ip associated with the website
            foreach(var y in System.Net.Dns.GetHostAddressesAsync("www.google.com").Result)
            {
                Console.WriteLine($"IP of (website): " + y);
                Console.WriteLine($"IP of (website): " + x);
            }
            }
        }
        // create a function that reads the DnsEndPoint and prints out the ip address
        public async static void HTTP()
        {
            // ask for website to get ip address of
            Console.WriteLine("Enter a website to get the ip address of: ");
            // read the website
            string? website = Console.ReadLine();
            // create a DnsEndPoint
            DnsEndPoint dns = new DnsEndPoint(website, 80);
            // loop through DnsEndPoint
            foreach(var x in System.Net.Dns.GetHostEntryAsync(website).Result.AddressList)
            {
                // print out the ip address
                Console.WriteLine($"IP of ({website}): " + x);
            }
        }

        public static void test()
        {
 
            Console.WriteLine("Hello World!");
            Console.WriteLine(Maths(9, 10));
            // make http ran by task.run
            HTTP();
            teste2r();
        }
    }
}