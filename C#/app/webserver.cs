using System.Diagnostics;

namespace BrainOfNeuralNetwork
{
    class BasketToCatch
    {
        public static void Runner()
        {
            // attach to any google.exe process
            Process[] processes = Process.GetProcessesByName("chrome");
            // read out data from the process
            foreach (Process process in processes)
            {
                Console.WriteLine("  ID: {0}", process.Id);
                if (process.Id == 7300)
                {
                    // print found given process id
                    Console.WriteLine($"Found process id" + " " + process.Id);
                    // attach to the process
                    Process processToAttach = Process.GetProcessById(process.Id);
                    // read out data from the attached process
                    foreach (Process Data in Process.GetProcesses())
                    {
                        // print out the data
                        Console.WriteLine("  Count: {0}", Data.Threads.Count);
                        // print out data in the process
                        foreach (ProcessThread thread in Data.Threads)
                        {
                            Console.WriteLine("    Thread ID: {0}", thread.Id);
                        }
                    }
                }
            }
        }
        public static void BackRead()
        {
            var bytes = new byte[1024];
            foreach (var b in bytes)
            {
                Console.WriteLine(b);
            }
        }
    }
}

