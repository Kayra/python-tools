import mem_profile
import time


def function_one():
    pass


def function_two():
    pass


print('Memory BEFORE: {}Mb'.format(mem_profile.memory_usage_resource()))

timer_start_one = time.clock()
function_one()
timer_end_one = time.clock()

timer_start_two = time.clock()
function_two()
timer_end_two = time.clock()

print('Memory AFTER: {}Mb'.format(mem_profile.memory_usage_resource()))


print('The first function took {} seconds'.format(timer_end_one - timer_start_one))
print('The second function took {} seconds'.format(timer_end_two - timer_start_two))
