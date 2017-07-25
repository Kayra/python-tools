import mem_profile
import time


def function_one():
    pass


def function_two():
    pass


memory_start_one = mem_profile.memory_usage_resource()
timer_start_one = time.clock()
function_one()
timer_end_one = time.clock()
memory_end_one = mem_profile.memory_usage_resource()


memory_start_two = mem_profile.memory_usage_resource()
timer_start_two = time.clock()
function_two()
timer_end_two = time.clock()
memory_end_two = mem_profile.memory_usage_resource()


print('The first function took {} seconds'.format(timer_end_one - timer_start_one))
print('The second function took {} seconds'.format(timer_end_two - timer_start_two))


print('The first function used {}mb'.format(memory_end_one - memory_start_one))
print('The second function used {}mb'.format(memory_end_two - memory_start_two))


def memory_profile(function_one, function_two):

    memory_start_one = mem_profile.memory_usage_resource()
    function_one()
    memory_end_one = mem_profile.memory_usage_resource()

    memory_start_two = mem_profile.memory_usage_resource()
    function_two()
    memory_end_two = mem_profile.memory_usage_resource()

    print('The first function used {}mb'.format(memory_end_one - memory_start_one))
    print('The second function used {}mb'.format(memory_end_two - memory_start_two))
