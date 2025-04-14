from py4j.java_gateway import JavaGateway

gateway = JavaGateway()

ArrayList = gateway.jvm.java.util.ArrayList
HashSet = gateway.jvm.java.util.HashSet

java_list = ArrayList()
java_set = HashSet()


def call_sevensFlipped(allocations, spaces, shortfall, backup_size, used):
    java_util = gateway.jvm.java.util

    java_allocations = java_util.ArrayList()
    for allocation in allocations:
        java_array = gateway.new_array(gateway.jvm.int, len(allocation))
        for i, val in enumerate(allocation):
            java_array[i] = val
        java_allocations.add(java_array)

    java_spaces = java_util.ArrayList()
    for space in spaces:
        java_spaces.add(space)

    java_shortfall = gateway.new_array(gateway.jvm.int, 2)
    java_shortfall[0] = shortfall[0]
    java_shortfall[1] = shortfall[1]

    java_used = java_util.HashSet()
    if used:
        for index in used:
            java_used.add(index)

    backup_size = int(backup_size)

    combine = gateway.entry_point
    java_result = combine.sevensFlipped(java_allocations, java_spaces, java_shortfall, backup_size, java_used)

    def java_list_to_python(java_list):
        return [list(item) if hasattr(item, '__iter__') and not isinstance(item, str) else item for item in java_list]

    python_result = [java_list_to_python(sublist) for sublist in java_result]

    return python_result


def call_optimize(sorted_allocations, allocations, backup_size, out_combos, spaces):
    java_util = gateway.jvm.java.util

    java_sorted_allocations = java_util.ArrayList()
    for allocation in sorted_allocations:
        java_list = java_util.ArrayList()
        for val in allocation:
            java_list.add(val)
        java_sorted_allocations.add(java_list)

    java_allocations = java_util.ArrayList()
    for allocation in allocations:
        java_array = gateway.new_array(gateway.jvm.int, len(allocation))
        for i, val in enumerate(allocation):
            java_array[i] = val
        java_allocations.add(java_array)

    java_out_combos = java_util.ArrayList()
    for combo in out_combos:
        java_list = java_util.ArrayList()
        for val in combo:
            java_list.add(val)
        java_out_combos.add(java_list)

    java_spaces = java_util.ArrayList()
    for space in spaces:
        java_spaces.add(space)

    backup_size = int(backup_size)

    combine = gateway.entry_point
    java_result = combine.optimize(java_sorted_allocations, java_allocations, backup_size, java_out_combos, java_spaces)

    def java_list_to_python(java_list):
        return [list(item) if hasattr(item, '__iter__') and not isinstance(item, str) else item for item in java_list]

    python_result = [java_list_to_python(sublist) for sublist in java_result]

    return python_result