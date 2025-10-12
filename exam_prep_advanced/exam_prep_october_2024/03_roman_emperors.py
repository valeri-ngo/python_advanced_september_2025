def list_roman_emperors(*args, **kwargs):
    success_emperors = {}
    failed_emperors = {}
    result = ""


    for emp_name, success_status in args:
        if success_status:
            success_emperors[emp_name] = kwargs[emp_name]
        else:
            failed_emperors[emp_name] = kwargs[emp_name]

    sorted_success_emperors = sorted(success_emperors.items(), key= lambda kvp: (-kvp[1], kvp[0]))
    sorted_failed_emperors = sorted(failed_emperors.items(), key= lambda kvp: (kvp[1], kvp[0]))

    result = f"Total number of emperors: {len(args)}"
    if success_emperors:
        # If any successful emperor:
        result += "\nSuccessful emperors:"
        for emp_name, year in sorted_success_emperors:
            result += f"\n****{emp_name}: {year}"
    if failed_emperors:
        # If any unsuccessful emperor
        result += "\nUnsuccessful emperors:"
        for emp_name, year in sorted_failed_emperors:
            result += f"\n****{emp_name}: {year}"

    return result


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print()
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print()
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))
