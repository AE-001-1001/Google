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
        // create a function that clears console
        public static void clear()
        {
            // clear console
            Console.Clear();
        }
        // create a post function for HTTP POST
        static public int Post(string url, string data)
        {
            // Create a new HTTP client
            var client = new HttpClient();
            // Create a new HTTP content
            var content = new StringContent(data);
            // Post the data to the API
            var response = client.PostAsync(url, content).Result;
            // print each line of the data nicely
            foreach (var line in response.Content.ReadAsStringAsync().Result.Split(new[] { Environment.NewLine }, StringSplitOptions.None))
            {
                Console.WriteLine($"{line}");
            }
            // Return the data
            return 0;
        }
        // create a function that reads the DnsEndPoint and prints out the ip address with custom user-agent
        public static void HTTPdecompiler(string website) // suckmydickscript
        {
            // get the website
            // create a new HTTP client
            var client = new HttpClient();
            // create a new HTTP request
            var request = new HttpRequestMessage();
            // set the request method to GET
            request.Method = HttpMethod.Get;
            // set the request url to the given url
            request.RequestUri = new Uri(website);
            // set the request user-agent to the given user-agent
            request.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36");
            // set the request accept to the given accept
            request.Headers.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.3,image/avif,image/webp,image/apng,*/*;q=0.6,application/signed-exchange;v=b3;q=0.9");
            // set the request accept-encoding to the given accept-encoding
            request.Headers.Add("Accept-Encoding", "gzip,deflate,br");
            // set the request accept-language to the given accept-language
            request.Headers.Add("Accept-Language", "en-US,en;q=0.9");
            // set the request cache-control to the given cache-control
            request.Headers.Add("Cache-Control", "max-age=0");
            // set the request sec-ch-ua to the given sec-ch-ua
            request.Headers.Add("Sec-Ch-Ua", "\"Chromium\";v=\"90\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"90\"");
            // set the request sec-ch-ua-mobile to the given sec-ch-ua-mobile
            request.Headers.Add("Sec-Ch-Ua-Mobile", "?0");
            // set the request sec-fetch-dest to the given sec-fetch-dest
            request.Headers.Add("Sec-Fetch-Dest", "document");
            // set the request sec-fetch-mode to the given sec-fetch-mode
            request.Headers.Add("Sec-Fetch-Mode", "navigate");
            // set the request sec-fetch-site to the given sec-fetch-site
            request.Headers.Add("Sec-Fetch-Site", "none");
            // set the request sec-fetch-user to the given sec-fetch-user
            request.Headers.Add("Sec-Fetch-User", "?1");
            // set the request upgrade-insecure-requests to the given upgrade-insecure-requests
            request.Headers.Add("Upgrade-Insecure-Requests", "1");
            // set the request cookie to the given cookie
            request.Headers.Add("Cookie", "__cfduid=d7d9b9b9b9b9b9b9b9b9b9b9b9b9b9b9b1619630000; _ga=GA1.2.1234567890.1619630000; _gid=GA1.2.1234567890.1619630000; _gat_gtag_UA_1234567890_1=1");
            // return the content length
            // get the response from the request
            var response = client.SendAsync(request).Result;
            // print out the response
            Console.WriteLine(response);
            // sleep for 1 seconds
            Thread.Sleep(1000);
            if (response.StatusCode == HttpStatusCode.OK)
            {
                // print out the response content
                // make sure to decode it too
                Console.WriteLine(response.Content.ReadAsStringAsync().Result);
                // Decode the incoming data
            }
            else
            {
                // print out the response status code
                Console.WriteLine(response.StatusCode);
            }
            var data = response.Content.ReadAsStringAsync().Result;
            File.WriteAllLinesAsync("output.csv", new string[] { data });
            // if console appears to be cluttered clear it
            if (Console.CursorTop > 150)
            {
                // clear console
                Console.Clear();
            }
        }

        public static void test()
        {
 
            Console.WriteLine("Hello World!");
            Console.WriteLine(Maths(9, 10));
            // make http ran by task.run
            // create loop
            for (int x = 0; x < 10; x++)
            {
                // create a new task
                Task.Run(() => teste2r());
                // create a new task
                // create a list will different websites to test
                List<string> websites = new List<string>();
                // add websites to the list
                websites.Add("https://www.google.com/");
                websites.Add("https://www.youtube.com/");
                websites.Add("https://www.twitter.com/");
                websites.Add("https://www.facebook.com/");
                websites.Add("https://www.reddit.com/");
                websites.Add("https://www.tumblr.com/");
                websites.Add("https://www.instagram.com/");
                websites.Add("https://www.pinterest.com/");
                websites.Add("https://www.tiktok.com/");
                websites.Add("https://www.twitch.tv/");
                websites.Add("https://www.netflix.com/");
                websites.Add("https://www.amazon.com/");
                websites.Add("https://www.ebay.com/");
                websites.Add("https://www.walmart.com/");
                websites.Add("https://www.apple.com/");
                websites.Add("https://www.microsoft.com/");
                websites.Add("https://www.samsung.com/");
                websites.Add("https://www.adobe.com/");
                websites.Add("https://www.spotify.com/");
                websites.Add("https://www.robinhood.com/");
                websites.Add("https://www.minecraft.net/");
                websites.Add("https://www.roblox.com/");
                websites.Add("https://www.epicgames.com/");
                websites.Add("https://www.ubisoft.com/");
                websites.Add("https://www.playstation.com/");
                websites.Add("https://www.xbox.com/");
                websites.Add("https://www.nvidia.com/");
                websites.Add("https://www.intel.com/");
                websites.Add("https://www.amd.com/");
                websites.Add("https://www.asus.com/");
                websites.Add("https://www.dell.com/");
                websites.Add("https://www.tesla.com/");
                websites.Add("https://github.com/AE-001-1001");
                websites.Add("https://www.reddit.com/r/ProgrammerHumor/");
                // add popular websites to the list
                websites.Add("https://www.pandora.com/");
                websites.Add("https://www.hulu.com/");
                websites.Add("https://www.etsy.com/");
                websites.Add("https://www.bing.com/");
                websites.Add("https://www.yahoo.com/");
                websites.Add("https://www.4chan.org/");
                websites.Add("https://www.9gag.com/");
                websites.Add("https://www.imgur.com/");
                // add .gov websites to the list
                websites.Add("https://www.whitehouse.gov/");
                websites.Add("https://www.usa.gov/");
                websites.Add("https://www.fbi.gov/");
                websites.Add("https://www.cia.gov/");
                websites.Add("https://www.nsa.gov/");
                websites.Add("https://www.dhs.gov/");
                websites.Add("https://www.doe.gov/");
                websites.Add("https://www.dol.gov/");
                websites.Add("https://www.dot.gov/");
                websites.Add("https://www.ed.gov/");
                websites.Add("https://www.epa.gov/");
                websites.Add("https://www.fda.gov/");
                websites.Add("https://www.fema.gov/");
                websites.Add("https://www.hhs.gov/");
                websites.Add("https://www.hud.gov/");
                websites.Add("https://www.usda.gov/");
                websites.Add("https://www.usgs.gov/");
                websites.Add("https://www.va.gov/");
                websites.Add("https://www.nist.gov/");
                websites.Add("https://www.nrc.gov/");
                websites.Add("https://www.nsf.gov/");
                websites.Add("https://www.osha.gov/");
                websites.Add("https://www.sba.gov/");
                websites.Add("https://www.ssa.gov/");
                websites.Add("https://www.usps.gov/");
                // after all websites are added to the list
                // return output to seperate file
                // create a new file
                // Put output into output.txt

                //create a loop that goes through the list, and uses Post function
                foreach (string website in websites)
                {
                    // create a new task
                    HTTPdecompiler(website);
                }
            }
        }
    }
}