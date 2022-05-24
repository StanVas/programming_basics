# Обем на басейна в литри
volume = int(input())
# дебит на първата тръба за час
first_pipe = int(input())
# дебит на втората тръба за час
second_pipe = int(input())
# часовете които работникът отсъства
hours = float(input())
first_pipe_total = first_pipe * hours
second_pipe_total = second_pipe * hours
both_pipes_total = first_pipe_total + second_pipe_total
percent_first_pipe = 0
percent_second_pipe = 0
percent_pipes = 0
diff = abs(volume - both_pipes_total)
each_pipe = first_pipe + second_pipe

if volume >= both_pipes_total:
    percent_pipes = (both_pipes_total / volume) * 100
    first_pipe_percent = (first_pipe / each_pipe) * 100
    second_pipe_percent = (second_pipe / each_pipe) * 100
    print(f"The pool is {percent_pipes}% full. Pipe 1: {first_pipe_percent:.2f}%. Pipe 2: {second_pipe_percent:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {diff} liters.")
