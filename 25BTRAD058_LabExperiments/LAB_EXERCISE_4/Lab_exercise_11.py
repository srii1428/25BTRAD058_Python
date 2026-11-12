# Log file reader program.
#* Log File Reader Program: Develop a Python program to read a log file, identify specific keywords such as
#ERROR, WARNING, and INFO, and summarize the number of occurrences of each category.
#* Analyze log contents, design suitable search and counting logic, handle missing or empty files, and verify
#the accuracy of results. (CT)
#* Apply the program to a sample application log and explain how it helps identify errors and monitor system
#activity. (RWE)

try:
    file = open(r"C:\Users\M SRIHARIPRIYAA\Downloads\log.txt", "r")
    error = warning = info = 0
    for line in file:
        if "ERROR" in line:
            error += 1
        elif "WARNING" in line:
            warning += 1
        elif "INFO" in line:
            info += 1
            file.close()
            print("ERROR:", error)
            print("WARNING:", warning)
            print("INFO:", info)
except FileNotFoundError:
    print("File not found")

# Sample log.txt:
# INFO: Program started
#  ERROR: File not foundWARNING: Low memory
# INFO: User logged in
# ERROR: Connection failed