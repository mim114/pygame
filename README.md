1. For bubble_hunter.py, paddleball.py install python3-tk.

2. For casino.py if you use windows add in file -->
   from ctypes import \*

   windll.kernel32.GetStdHandle.restype = c_ulong
   h = windll.kernel32.GetStdHandle(c_ulong(0xfffffff5))

   instead -->
   def color(c):
   return f"\033[0;{c}m"
