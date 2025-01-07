# Basic Computer Assembler

This project converts assembly language into machine language for a simple CPU. The CPU architecture supports:

- **7 MRI (Memory Reference Instructions)**  
- **18 Non-MRI Instructions**:  
  - 12 Register Reference Instructions  
  - 6 Input/Output Instructions  
- **4 Pseudo Instructions**:  
  - `ORG` (Set origin)  
  - `END` (End program)  
  - `DEC` (Decimal operand)  
  - `HEX` (Hexadecimal operand)  

### Features:
- **Two-Pass Assembly Process**:  
  - **First Pass**: Builds a symbol table for labels and their memory addresses.  
  - **Second Pass**: Converts instructions into 16-bit binary machine code.  

### Usage:
1. **Input**: Provide the assembly code in `asm.txt`.  
2. **Run**: Execute the assembler to generate the machine code.  
3. **Output**: Machine code is saved to `Machine_Code.txt`.
