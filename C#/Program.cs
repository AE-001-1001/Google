using System.Runtime.InteropServices;

// Create a function using the InteropServices
// attribute and the DllImport attribute.
[DllImport("kernel32", CharSet = CharSet.Ansi, ExactSpelling = true, SetLastError = true)]
static extern IntPtr LoadLibraryA(
    string lpFileName
    );
[DllImport("user32", CharSet = CharSet.Ansi, ExactSpelling = true, SetLastError = true)]
static extern int MessageBoxA(
    IntPtr hWnd,
    string lpText,
    string lpCaption,
    uint uType
    );
// use the IntPtr
IntPtr hModule = LoadLibraryA("kernel32.dll");

Console.WriteLine("hModule = {0}", hModule);

// create a new function that will attach to given process id
static void AttachToProcess(int pid)
{
    // get the handle to the process
    IntPtr hProcess = OpenProcess(PROCESS_ALL_ACCESS, false, pid);
    // check if the handle is valid
    if (hProcess == IntPtr.Zero)
    {
        // if not, throw an exception
        throw new Exception("OpenProcess failed");
    }
    // if the handle is valid, print out the handle
    Console.WriteLine("hProcess = {0}", hProcess);
    // close the handle
    CloseHandle(hProcess);
}

nint OpenProcess(object pROCESS_ALL_ACCESS, bool v, int pid)
{
    // create a variable that stores the handle
    var hProcess = IntPtr.Zero;
    // check if the handle is valid
    if (hProcess == IntPtr.Zero)
    {
        // if not, throw an exception
        throw new Exception("OpenProcess failed");
    }
    // if the handle is valid, print out the handle
    Console.WriteLine("hProcess = {0}", hProcess);
}