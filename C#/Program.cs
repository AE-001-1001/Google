using System.Collections.ObjectModel;
using System.Runtime.InteropServices;
using System.Net;
using System.Security.Principal;

namespace Environment 
{
    // create a class that will be the web server
    class Webserver
    {
        // create a function that will start the web server
        public static void Start()
        {
            // create a web server
            HttpListener listener = new HttpListener();
            // add the prefix to the web server
            listener.Prefixes.Add("http://localhost:8080/");
            // start the web server
            listener.Start();
            // create a loop that will run forever
            while (true)
            {
                // create a context that will be used to get the request
                HttpListenerContext context = listener.GetContext();
                // create a request that will be used to get the request
                HttpListenerRequest request = context.Request;
                // create a response that will be used to get the request
                HttpListenerResponse response = context.Response;
                // change the user-agent to a mac based user-agent
                string mbuser_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36";
                // change the user-agent to a windows based user-agent
                string wbuser_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36";
                // change the user agent to a linux based user-agent
                string Lbuser_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36";
                // check if the OS is windows,mac,or linux
                if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
                {
                    // change the user-agent to a windows based user-agent
                    request.Headers["User-Agent"] = wbuser_agent;
                }
                else if (RuntimeInformation.IsOSPlatform(OSPlatform.Linux))
                {
                    // change the user-agent to a linux based user-agent
                    request.Headers["User-Agent"] = Lbuser_agent;
                }
                else if (RuntimeInformation.IsOSPlatform(OSPlatform.OSX))
                {
                    // change the user-agent to a mac based user-agent
                    request.Headers["User-Agent"] = mbuser_agent;
                }
                // if it is windows get the users elevation
                if (RuntimeInformation.IsOSPlatform(OSPlatform.Windows))
                {
                    // get the users elevation
                    WindowsIdentity identity = WindowsIdentity.GetCurrent();
                    WindowsPrincipal principal = new WindowsPrincipal(identity);
                    // check if the user is an admin
                    if (principal.IsInRole(WindowsBuiltInRole.Administrator))
                    {
                        // print out the users elevation
                        Console.WriteLine("The user is an administrator.");
        
                    }
                    else
                    {
                        // print out the users elevation
                        Console.WriteLine("The user is not an administrator.");
                    }
                }
                WindowsIdentity identityy = WindowsIdentity.GetCurrent();
                WindowsPrincipal principa1l = new WindowsPrincipal(identityy);
                // create a string that will be used to post the request of the OS version of the user and if the user is ADmin or not and the users Internet Service Provider ip, make the text centered and make the background black and the text animated rainbow
                string responseString = "<html><head><style>body {background-color: black; color: white; text-align: center; animation: rainbow 5s infinite;}</style><script>function rainbow() {var letters = '0123456789ABCDEF';var color = '#';for (var i = 0; i < 6; i++) {color += letters[Math.floor(Math.random() * 16)];}document.body.style.color = color;}setInterval(rainbow, 100);</script></head><body><h1>OS: " + RuntimeInformation.OSDescription + "</h1><h1>Admin: " + principa1l.IsInRole(WindowsBuiltInRole.Administrator) + "</h1><h1>ISP: " + new WebClient().DownloadString("http://icanhazip.com") + "</h1></body></html>";
                // create a string that will be used to post the request to make the web server look like a website
                byte[] buffer = System.Text.Encoding.UTF8.GetBytes(responseString);
                // set the content length
                response.ContentLength64 = buffer.Length;
                // set the content length for the time
                System.IO.Stream output = response.OutputStream;
                // write the request to the stream
                output.Write(buffer, 0, buffer.Length);
                // if the user is loaded print out all their data
                    // print out the users ip
                    for (int i = 0; i < request.UserLanguages.Length; i++)
                    {
                        Console.WriteLine("Language: " + request.UserLanguages[i]);
                    }
                    // print out the users host
                    Console.WriteLine("Host: " + request.UserHostName);
                    // print out the users agent
                    Console.WriteLine("Agent: " + request.UserAgent);
                
                // close the stream
                output.Close();
            }
        }
    }

    class Class
    {
        [DllImport("kernel32.dll")]
        static extern Boolean Beep(UInt32 Freq, UInt32 Duration);

        public static void methodRequiringStuffFromKernel32()
        {
            // make Beep work
            Beep(1000, 1000);
        }

        [DllImport("user32.dll")]
        static extern int MessageBox(IntPtr hWnd, String text, String caption, uint type);
        public static void methodRequiringStuffFromUser32()
        {
            // in the message box add cancel and ok buttons
            var result = MessageBox((IntPtr)0, "Hello World", "Hello Dialog", 1);
            if (result == 1)
            {
                // grab all the ip addresses
                for (int i = 0; i < System.Net.Dns.GetHostEntry(Dns.GetHostName()).AddressList.Length; i++)
                {
                    // get the name of the index in System.Net.Dns.GetHostEntry(System.Net.Dns.GetHostName()).AddressList
                    string name = System.Net.Dns.GetHostEntry(Dns.GetHostName()).AddressList[i].ToString();

                }
                // print the users IP
                Console.WriteLine("The user clicked OK.");
            }
            else
            {
                Console.WriteLine("The user clicked Cancel.");
            }
        }
    }
}

namespace MyWorld
{
    class Program
    {
        static void PreRunner(string[] args)
        {
            // use System.Collections.Generic;
            // to use Dictionary
            Dictionary<string, string> dict = new Dictionary<string, string>();
            dict.Add("Hello", "World");
            // Loop for each item in the list
            foreach (KeyValuePair<string, string> kvp in dict)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("{0},{1}", kvp.Key, kvp.Value);
            }
            // use System.Collections.ObjectModel;
            // to use ObservableCollection
            ObservableCollection<string> collection = new ObservableCollection<string>();
            collection.Add("Hello");
            // create a id for Hello
            int id = collection.IndexOf("Hello");
            // remove Hello
            collection.RemoveAt(id);
            // add World
            collection.Add("World");
            // Loop for each item in the list
            foreach (string item in collection)
            {
                Console.ForegroundColor = ConsoleColor.Blue;
                Console.WriteLine(item);
            }
        }
        // create a function that will draw an X
        static int DrawX(int x, int y)
        {
            // set the cursor position
            Console.SetCursorPosition(x, y);
            
            // Creates the A
            foreach (int r in new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 })
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.SetCursorPosition(x - r, y + r);
                // this loop creates the /\ part of the A
                foreach (int gh in new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10 })
                    {
                        Console.WriteLine("X");
                        Console.SetCursorPosition(x + gh, y + gh);
                    }
                    // make the cursor line up with the X's on the outside and then draw
                Console.SetCursorPosition(x-4, y + 5); // quick mafs to make it line up seeeeeeeee touch this and it doesn't line up anymore :(
                Console.WriteLine("---------");
            }

            // Create the N
            for (int i = 0; i < 10; i++)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.SetCursorPosition(x + 10, y + i);
                Console.WriteLine("X");
                for (int j = 0; j < 10; j++)
                {
                    Console.SetCursorPosition(x + 10 + j, y + j);
                    Console.WriteLine("X");
                }
                Console.SetCursorPosition(x + 20, y + i);
                Console.WriteLine("X");
            }

            // Create the D 
            for (int i = 0; i < 10; i++)
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.SetCursorPosition(x + 24, y + i);
                Console.WriteLine("X");
                for (int j = 0; j < 5; j++)
                {
                    Console.SetCursorPosition(x + 30 + j, y + j);
                    Console.WriteLine("X");
                }
                for (int j = 0; j < 5; j++)
                {
                    Console.SetCursorPosition(x + 30 + j, y + 9 - j);
                    Console.WriteLine("X");
                    if (j == 0)
                    {
                        // {Top of the D}make the lines at the top for the D
                        for (int k = 0; k < 5; k++)
                        {
                            Console.SetCursorPosition(x + 26 + k, y);
                            Console.WriteLine("X");
                        }
                    }
                    if (j == 4)
                    {
                        // {Bottom of the D}make the lines at the bottom for the D
                        for (int k = 0; k < 5; k++)
                        {
                            Console.SetCursorPosition(x + 26 + k, y + 9);
                            Console.WriteLine("X");
                        }
                    }
                }
            }
            // Create the R
            for (int i = 0; i < 10; i++)
            {
                // create the top of the R
                Console.ForegroundColor = ConsoleColor.Green;
                Console.SetCursorPosition(x + 36, y + i);
                Console.WriteLine("X");
                for (int j = 0; j < 5; j++)
                {
                    Console.SetCursorPosition(x + 42 + j, y + j);
                    Console.WriteLine("X");
                }
                // the line that goes down the middle of the R
                for (int j = 0; j < 5; j++)
                {
                    Console.SetCursorPosition(x + 42, y + 5 + j);
                    Console.WriteLine("X");
                    for (int k = 0; k < 5; k++)
                    {
                        Console.SetCursorPosition(x + 42 + k, y + 3 + k);
                        Console.WriteLine("X");
                    }
                }
            }
            int List = x, List2 = y;
            // return the value of x
            return List+List2;
        }
        // create a function that will clear the screen
        static void ClearScreen()
        {
            // clear the screen
            Console.Clear();
        }

        static void Main(string[] args)
        {   
            ClearScreen();
            Console.WriteLine(DrawX(10, 10));
            Console.ResetColor();
            PreRunner(args);
            Environment.Class.methodRequiringStuffFromKernel32();
            Environment.Class.methodRequiringStuffFromUser32();
            // try giving the text emotions and colors to express those emotions
            Console.ForegroundColor = ConsoleColor.White;
            // run the webserver
            Console.WriteLine("Running Webserver @ http://localhost:8080/");
            Environment.Webserver.Start();
        }
    }
}