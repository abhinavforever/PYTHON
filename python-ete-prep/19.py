class string:
    def get_String(self,string):
        self.string=string

    def print_String(self):
        print(self.string.upper())
s=string()
st=input()
s.get_String(st)
s.print_String()