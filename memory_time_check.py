import mem_profile
import time


def function_one():
    pass


def function_two():
    pass


print('Memory BEFORE: {}Mb'.format(mem_profile.memory_usage_resource()))

timer_start = time.clock()
function_one()
timer_end = time.clock()

# timer_start = time.clock()
# function_two()
# timer_end = time.clock()

print('Memory AFTER: {}Mb'.format(mem_profile.memory_usage_resource()))
print('Took {} seconds'.format(timer_end - timer_start))
