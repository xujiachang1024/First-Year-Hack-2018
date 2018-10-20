import cities
import csv

def load_demo_cities(file_name):
    road_map = []
    for l in csv.reader(open(file_name, 'r'), quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
        if l[0].lower() == "city":
            continue
        road_map.append((None, l[0], float(l[1]), float(l[2]), None, None))
    return road_map

def print_menu(road_map):
    for i in range(len(road_map)):
        print(str(i) + ": " + road_map[i][1])

def main():
    road_map = load_demo_cities("city_list.csv")
    selected_road_map = []
    while True:
        print_menu(road_map)
        option = raw_input("Type the number of the city > ")
        if option.lower() == "no" or option.lower() == "n":
            break
        try:
            option = int(option.strip())
            if option >= 0 and option < len(road_map):
                if road_map[option] not in selected_road_map:
                    selected_road_map.append(road_map[option])
                    continue
            print("Invalid inputs!")
        except:
            print("Invalid inputs!")

    print(selected_road_map)
    optimal = cities.find_best_cycle(selected_road_map)
    # cities.print_map(optimal)
    file_name = "demo_route.csv"
    cities.output_road_map(optimal[0], file_name)

if __name__ == "__main__":

    main()
