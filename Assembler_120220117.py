#Defining the opcodes for the instructions
#there are 3 types of instructions: MRI, Non-MRI, and pseudo instructions

MRI = {"AND": "0",
    "ADD": "1",
    "LDA": "2",
    "STA": "3",
    "BUN": "4",
    "BSA": "5",
    "ISZ": "6"
}

Register_instruction = {"CLA": "7800",
                        "CLE": "7400", 
                        "CMA": "7200",
            "CME": "7100",
            "CIR": "7080",
           "CIL": "7040",
            "INC": "7020",
            "SPA": "7010",
            "SNA": "7008",
            "SZA": "7004",
            "SZE": "7002",
            "HLT": "7001"
}



in_out_instructions = {
    "INP": "F800",
    "OUT": "F400",
    "SKI": "F200",
    "SKO": "F100",
    "ION": "F080",
    "IOF": "F040"
}

pseudoinstructions = ["ORG", "END", "DEC", "HEX"]

symbol_table = {}
lines = []
output = []


def first_pass():
    LC = 0
    for line in lines:
        if line[0].endswith(","):  # line has a label? has a comma?
            label = line[0][:-1]
            symbol_table[label] = LC  # store the label in the symbol table to its corresponding LC excluding the comma
            line = line[1:]  # remove the label from the line

        if line[0] == "ORG":
            LC = int(line[1], 16)   # LC =  ORG value
        elif line[0] == "END":
            break  #stop  the first pass
        elif line[0] in ["DEC", "HEX"]:
            LC += 1  # increment LC for each instruction
        else:
            LC += 1  


def second_pass():
    LC = 0
    for line in lines:
        instruction = ""

        if line[0].endswith(","):  # skip label in second pass
            line = line[1:]
        #pseudo instructions
        if line[0] == "ORG":
            LC = int(line[1], 16)  # LC =  ORG value
            continue
        elif line[0] == "END":
            break  #stop the second pass

        elif line[0] == "DEC":
            value = int(line[1])  # convert decimal to binary
            instruction =  bin(value & 0xFFFF)[2:].zfill(16) 

        elif line[0] == "HEX":
            value = int(line[1], 16)  # convert hexadecimal to binary
            instruction = bin(value)[2:].zfill(16) 

#MRI instructions
        if line[0] in MRI:
            opcode = MRI[line[0]]  # get the opcode for MRI instruction
            address = symbol_table.get(line[1], 0)  # get the address from the symbol table
            indirect = "1" if len(line) > 2 and line[2] == "I" else "0"  # check for indirect addressing
            instruction = f"{indirect}{bin(int(opcode))[2:].zfill(3)}{bin(address)[2:].zfill(12)}"
#non-MRI instructions
        elif line[0] in Register_instruction:
            instruction = bin(int(Register_instruction[line[0]], 16))[2:].zfill(16)   # convert register instruction to binary

        elif line[0] in in_out_instructions:
            instruction = bin(int(in_out_instructions[line[0]], 16))[2:].zfill(16)  # convert input/output instruction to binary

        output.append((LC, instruction))  # store the LC and instruction
        LC += 1


def main():
    global lines
    # opening the source file
    with open("asm.txt", "r") as f:
        for line in f:
            if "/" in line:
                line = line.split("/")[0]  # Remove comments
            if line.strip():
                lines.append(line.strip().split())  # split the line into components

    first_pass()
    second_pass()

    # writing the machine code to the output file
    with open("Machine_Code.txt", "w") as f:
        for lc, instr in output:
            f.write(f"{bin(lc)[2:].zfill(12)}  {instr}\n")


if __name__ == "__main__":
    main()
