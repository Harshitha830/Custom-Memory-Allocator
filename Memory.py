# Custom Memory Allocator Simulation

class MemoryAllocator:
    def __init__(self, size):
        # Initialize memory with empty blocks
        self.memory = ["_"] * size

    def display_memory(self):
        # Show current memory status
        print("\nCurrent Memory State:")
        print(self.memory)

    def allocate(self, name, size):
        """
        Allocate memory block
        name -> process name
        size -> number of blocks needed
        """

        count = 0
        start = -1

        # First Fit Allocation
        for i in range(len(self.memory)):
            if self.memory[i] == "_":
                if count == 0:
                    start = i
                count += 1

                if count == size:
                    for j in range(start, start + size):
                        self.memory[j] = name
                    print(f"\nAllocated {size} blocks for process '{name}'")
                    return
            else:
                count = 0

        print("\nMemory allocation failed! Not enough space.")

    def free(self, name):
        """
        Free memory occupied by a process
        """
        freed = False

        for i in range(len(self.memory)):
            if self.memory[i] == name:
                self.memory[i] = "_"
                freed = True

        if freed:
            print(f"\nMemory freed for process '{name}'")
        else:
            print("\nProcess not found in memory")


# ----------------------------
# Driver Program
# ----------------------------

size = int(input("Enter total memory blocks: "))
allocator = MemoryAllocator(size)

while True:

    print("\nSelect Operation")
    print("1. Allocate Memory")
    print("2. Free Memory")
    print("3. Display Memory")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter process name: ")
        blocks = int(input("Enter number of blocks needed: "))
        allocator.allocate(name, blocks)

    elif choice == 2:
        name = input("Enter process name to free: ")
        allocator.free(name)

    elif choice == 3:
        allocator.display_memory()

    elif choice == 4:
        print("Exiting program")
        break