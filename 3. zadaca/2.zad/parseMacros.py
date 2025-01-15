def _parse_macros(self):
    self._iter_lines(self._parse_macro)

def _mv(self, A, B):
    return [f"@{A}", "D=M", f"@{B}", "M=D"]

def _swp(self, A, B):
    return [
        "@TEMP", "M=0",
        f"@{A}", "D=M", "@TEMP", "M=D",
        f"@{B}", "D=M", f"@{A}", "M=D",
        "@TEMP", "D=M", f"@{B}", "M=D"
    ]

def _add(self, A, B, D):
    return [f"@{A}", "D=M", f"@{B}", "D=D+M", f"@{D}", "M=D"]

def _while(self, A):
    self._nest += 1
    return [
        f"(WHILE{self._nest})",
        f"@{A}", "D=M",
        f"@END{self._nest}", "D;JEQ"
    ]

def _parse_macro(self, line, o, p):
    if line.startswith("$"):
        cmd = line[1:].split("(")
        macro = cmd[0]
        
        if len(cmd) > 1:
            args = cmd[1]
            args_list = args.replace(")", "").split(",")
            
            if macro == "MV":
                return self._mv(args_list[0], args_list[1])
            elif macro == "SWP":
                return self._swp(args_list[0], args_list[1])
            elif macro == "ADD":
                return self._add(args_list[0], args_list[1], args_list[2])
            elif macro == "WHILE":
                return self._while(args_list[0])
            else:
                self._flag = False
                self._line = o
                self._errm = f"Unknown command '{macro}'"
                return ""
        if macro == "END":
            return [
                f"@WHILE{self._nest}",
                "0;JMP",
                f"(END{self._nest})"
            ]
    return line
