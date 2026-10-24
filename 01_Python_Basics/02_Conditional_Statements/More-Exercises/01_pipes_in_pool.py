volume = int(input())
pipe_one = int(input())
pipe_two = int(input())
hours = float(input())

water = (pipe_one * hours) + (pipe_two * hours)

if water <= volume:
    print(f"The pool is {(water/volume*100):.2f}% full. Pipe 1: {(pipe_one*hours/water*100):.2f}%. Pipe 2: {(pipe_two*hours/water*100):.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {abs(volume-water):.2f} liters.")