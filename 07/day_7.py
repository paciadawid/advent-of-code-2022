with open("input.txt", "r", encoding="utf-8") as f:
    commands = [line.strip().split() for line in f.readlines()]

current_path: list = []
file_system: dict[str, dict] = {}
full_name = ""
for command in commands:
    match command:
        case ["$", "cd", ".."]:
            current_path.pop()
        case ["$", "cd", child_folder]:
            current_path.append(child_folder)
            full_name = "/".join(current_path)
            if full_name not in file_system:
                file_system[full_name] = {}
            if "dirs" not in file_system[full_name]:
                file_system[full_name]["dirs"] = []
            if "files" not in file_system[full_name]:
                file_system[full_name]["files"] = []
            file_system[full_name]["size"] = None
        case ["$", _]:
            pass
        case ["dir", directory]:
            file_system[full_name]["dirs"].append(f"{full_name}/{directory}")
        case [size, name]:
            file_system[full_name]["files"].append(int(size))


def calculate_size(target_directory, file_map=None):
    sum_size = 0
    if not file_map:
        file_map = file_system
    for subdir in file_map[target_directory]["dirs"]:
        sum_size += calculate_size(subdir, file_map)
    return sum(file_map[target_directory]["files"]) + sum_size


# part 1
total_size = 0
for name, folder in file_system.items():
    dir_size = calculate_size(name)
    if dir_size <= 100000:
        total_size += dir_size
    folder["size"] = dir_size
print(total_size)

# part 2
disk_space, space_needed = 70000000, 30000000
current_free_space = disk_space - file_system["/"]["size"]
free_space_needed = space_needed - current_free_space

smallest_to_remove = disk_space
for folder in file_system.values():
    if free_space_needed <= folder["size"] < smallest_to_remove:
        smallest_to_remove = folder["size"]
print(smallest_to_remove)
