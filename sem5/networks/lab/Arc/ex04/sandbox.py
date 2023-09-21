import wmi

conn = wmi.WMI()
conn.Win32_Process.Create(CommandLine="notepad")