using System.Net;
using System.Threading;

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
        // create a function and thread in that function to get the IP address of the given website
        static public void GetIP(string url)
        {
            // Create a new HTTP client
            var client = new HttpClient();
            // Get the data from the API
            var response = client.GetStringAsync(url).Result;
            // print each line of the data nicely
            foreach (var line in response.Split(new[] { Environment.NewLine }, StringSplitOptions.None))
            {
                Console.WriteLine($"{line}");
            }
        }

        // create a function that clears console
        public static void clear()
        {
            // clear console
            Console.Clear();
        }
        // create a function that renames the console to the website running along with the time with cool loading bar
        public static void rename(string name)
        {
            // rename console
            Console.Title = name + " " + DateTime.Now;
            // create loading bar 
            for (int i = 0; i < 100; i++)
            {
                // print out cool loading bar
                Console.WriteLine("Loading: " + i + "%");
                // sleep for 1 second
                Thread.Sleep(1);
            }

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
            request.Headers.Add("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36");
            // set the request accept to the given accept
            request.Headers.Add("Accept", "text/html,application/xhtml+xml,application/xml;q=0.6,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9");
            // set the request accept-encoding to the given accept-encoding
            request.Headers.Add("Accept-Encoding", "gzip,deflate,br");
            // set the request accept-language to the given accept-language
            request.Headers.Add("Accept-Language", "en-US,en;q=0.9");
            // set the request cache-control to the given cache-control
            request.Headers.Add("Cache-Control", "max-age=0");
            // set the request sec-ch-ua to the given sec-ch-ua
            request.Headers.Add("Sec-Ch-Ua", "\"Chromium\";v=\"108\", \"Google Chrome\";v=\"108\", \";Not A Brand\";v=\"99\"");
            // set the request sec-ch-ua-mobile to the given sec-ch-ua-mobile
            request.Headers.Add("Sec-Ch-Ua-Mobile", "?0");
            // set the request sec-fetch-dest to the given sec-fetch-dest
            request.Headers.Add("Sec-Fetch-Dest", "document");
            // set the request sec-fetch-mode to the given sec-fetch-mode
            request.Headers.Add("Sec-Fetch-Mode", "no-cors");
            // set the request sec-fetch-site to the given sec-fetch-site
            request.Headers.Add("Sec-Fetch-Site", "cross-site");
            // set the request sec-fetch-user to the given sec-fetch-user
            request.Headers.Add("Sec-Fetch-User", "?1");
            // set the request upgrade-insecure-requests to the given upgrade-insecure-requests
            request.Headers.Add("Upgrade-Insecure-Requests", "1");
            // set the request cookie to the given cookie across all websites
            request.Headers.Add("Cookie", "PHPSESSID=1; _ga=GA1.2.1; _gid=GA1.2.1; _gat_gtag_UA_1=1");
            // return the content length
            // get the response from the request
            var response = client.SendAsync(request).Result;
            // print out the response
            Console.WriteLine(response);
            // sleep for 1 seconds
            Thread.Sleep(1000);
            File.WriteAllText("output.csv", response.Content.ReadAsStringAsync().Result);
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
            // if nosniff is in the response 
            // try to decode the data
            if (data.Contains("nosniff"))
            {
                // decode the data
                Console.WriteLine(data);
            }
            // try to incur TCP_HIT
            // if the response contains the word "cache"
            if (data.Contains("cache"))
            {
                // print out the response
                Console.WriteLine(data);
            }
            // if console appears to be cluttered clear it
            if (Console.CursorTop > 256)
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
                    // create malicious post data
                    // create a new task
                    rename(website);
                    HTTPdecompiler(website);
                }
            }
        }
    }
}