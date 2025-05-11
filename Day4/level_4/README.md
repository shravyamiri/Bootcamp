Stream Processing Pipeline (Level 4)
This project upgrades a simple str -> str processing pipeline into a more powerful stream-based architecture. It supports:

Fan-out: Split one line into many

Fan-in: Combine multiple lines into one

Stateful Processing: Maintain counters, buffers, or accumulators

Stateless Processing: Like converting text to uppercase

Processor Initialization with Configuration

Project Structure

stream_pipeline/

├── processors.py         
├── main.py              
└── test_processors.py    

Example Input

hello world

foo bar

python|java|c++

stream processing

Processor Chain

processors = [
    LineCounter(),                  
    to_upper,                       
    SplitByDelimiter("|"),         
    JoinEveryNLines(2)             
]

output
1: HELLO WORLD | 2: FOO BAR

3: PYTHON | JAVA

C++ | 4: STREAM PROCESSING

How to Run

Clone or download the files

Ensure you have Python 3.x installed.

Run the main pipeline

python main.py

run the test

python test_processors.py

you should see

All tests passed.

Challenge Questions Answered

Reused str -> str functions using a decorator (str_to_stream_processor)

Parameterized processors using class constructors

Split and joined lines using fan-in/fan-out processors

Clear separation of stateful vs stateless processors

All processors are testable independently
