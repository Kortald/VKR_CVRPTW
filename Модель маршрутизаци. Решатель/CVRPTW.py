from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


def create_data_model():
    """Содержит всю информацию о решаемой подели"""
    data = {}
    data["time_matrix"] = [
[0, 344, 238, 283, 262, 327, 565, 474, 715, 672, 574, 727, 704, 839, 851, 891, 1061, 1078, 1058, 802, 727, 689, 611, 619, 503],
[300, 0, 207, 219, 427, 638, 687, 649, 1047, 975, 870, 996, 971, 995, 934, 985, 1143, 1169, 1165, 987, 891, 860, 790, 804, 689],
[259, 196, 0, 154, 324, 500, 587, 544, 820, 817, 816, 981, 956, 916, 853, 892, 1046, 1081, 1061, 887, 800, 764, 689, 712, 598],
[302, 187, 137, 0, 355, 537, 602, 580, 856, 837, 811, 984, 977, 933, 876, 915, 1077, 1092, 1080, 862, 783, 747, 665, 694, 533],
[281, 489, 349, 309, 0, 474, 541, 503, 745, 755, 771, 945, 987, 906, 829, 872, 1013, 1082, 1061, 876, 796, 757, 680, 699, 564],
[476, 750, 710, 792, 640, 0, 412, 543, 561, 493, 446, 425, 412, 723, 746, 781, 956, 977, 959, 975, 891, 850, 782, 787, 694],
[340, 615, 413, 505, 360, 101, 0, 271, 498, 412, 375, 542, 575, 654, 577, 628, 792, 839, 817, 632, 546, 510, 432, 455, 312],
[424, 696, 483, 577, 439, 175, 76, 0, 379, 304, 268, 452, 453, 538, 558, 587, 746, 788, 768, 713, 633, 599, 515, 533, 405],
[641, 921, 890, 927, 705, 385, 354, 283, 0, 182, 259, 468, 463, 362, 382, 430, 579, 624, 608, 942, 675, 665, 588, 778, 630],
[601, 882, 845, 892, 780, 357, 418, 347, 197, 0, 112, 276, 267, 426, 457, 496, 640, 687, 676, 1043, 987, 934, 862, 884, 733],
[568, 860, 819, 865, 751, 322, 365, 324, 251, 105, 0, 223, 214, 480, 499, 540, 695, 733, 710, 1001, 929, 882, 807, 835, 685],
[762, 1031, 1019, 1116, 951, 532, 515, 459, 414, 298, 286, 0, 91, 630, 647, 723, 875, 871, 857, 1210, 1127, 1097, 1034, 1045, 920],
[764, 1031, 1019, 1116, 951, 532, 516, 460, 414, 298, 286, 0, 0, 630, 648, 723, 877, 871, 857, 1210, 1127, 1097, 1034, 1045, 920],
[914, 1183, 929, 892, 844, 668, 587, 546, 399, 522, 495, 599, 637, 0, 112, 265, 328, 439, 436, 598, 488, 482, 411, 633, 477],
[908, 1181, 897, 864, 820, 662, 565, 514, 386, 530, 506, 624, 664, 117, 0, 169, 254, 363, 358, 491, 400, 404, 333, 456, 442],
[989, 1260, 974, 957, 905, 724, 640, 583, 445, 568, 548, 781, 744, 225, 153, 0, 178, 215, 201, 486, 350, 361, 288, 420, 466],
[1144, 1415, 1113, 1104, 1057, 898, 805, 737, 639, 751, 723, 827, 869, 279, 204, 160, 0, 384, 366, 627, 516, 520, 428, 567, 698],
[1751, 1569, 1504, 1472, 1475, 1441, 1247, 1152, 1128, 1268, 1258, 1495, 1377, 947, 852, 708, 406, 0, 39, 777, 831, 842, 822, 753, 986],
[1704, 1984, 1517, 1477, 1467, 1388, 1214, 1135, 1113, 1240, 1225, 1449, 1382, 919, 831, 679, 387, 63, 0, 760, 885, 860, 785, 733, 955],
[945, 1022, 914, 872, 827, 1108, 870, 806, 804, 1015, 931, 1209, 1203, 641, 529, 473, 634, 632, 622, 0, 158, 197, 245, 222, 432],
[809, 894, 778, 756, 707, 884, 715, 660, 783, 880, 874, 1052, 1153, 560, 439, 400, 565, 578, 573, 174, 0, 52, 131, 151, 320],
[768, 855, 734, 721, 672, 786, 676, 630, 745, 840, 834, 1018, 1103, 530, 407, 358, 526, 544, 545, 212, 47, 0, 93, 143, 279],
[760, 841, 723, 708, 657, 756, 627, 575, 682, 785, 766, 954, 1084, 483, 354, 312, 447, 487, 472, 198, 111, 63, 0, 149, 265],
[751, 836, 730, 712, 656, 752, 829, 765, 917, 1021, 1083, 1254, 1199, 602, 496, 431, 609, 607, 598, 224, 150, 147, 181, 0, 258],
[869, 964, 841, 811, 753, 691, 609, 556, 664, 745, 735, 921, 1009, 491, 371, 444, 583, 610, 620, 407, 289, 266, 207, 350, 0],
]

    data["demands"] = [0, 14, 24, 34, 10, 14, 18, 54, 34, 20, 11, 14, 65, 13, 11, 16, 32, 42, 6, 24, 24, 11, 37, 13, 14]
    data["vehicle_capacities"] = [100,100,100,100,100,100]
    data["time_windows"] = [
        (0, 500), # Депо 0
        (421, 873), # 1
        (0, 674), # 2
        (302, 854), # 3
        (1021, 1751), # 4
        (256, 421), # 5
        (1230, 1643), # 6
        (340, 654), # 7
        (1263, 1751), # 8
        (0, 1751), # 9
        (321, 892), # 10
        (405, 952), # 11
        (561, 1024), # 12
        (953, 1402), # 13
        (793, 1063), # 14
        (985, 1395), # 15
        (1500, 1751), # 16
        (1154, 1681), # 17
        (1204, 1412), # 18
        (1240, 1751), # 19
        (1023, 1421), # 20
        (954, 1365), # 21
        (600, 1212), # 22
        (1432, 1561), # 23
        (489, 712), # 24
    ]
    data["num_vehicles"] = 6
    data["depot"] = 0
    return data


def print_solution(data, manager, routing, solution):
    print(f"Целевое значение: {solution.ObjectiveValue()/60}")
    time_dimension = routing.GetDimensionOrDie("Time")
    total_time = 0
    total_load = 0
    for vehicle_id in range(data["num_vehicles"]):
        index = routing.Start(vehicle_id)
        plan_output = f"Маршрут для ТС {vehicle_id}:\n"
        route_time = 0
        route_load = 0
        while not routing.IsEnd(index):
            node_index = manager.IndexToNode(index)
            route_load += data["demands"][node_index]
            time_var = time_dimension.CumulVar(index)
            plan_output += f" Пункт ({node_index}), Загрузка({route_load}), Время ({str(solution.Min(time_var)/60)[0:5]},{str(solution.Max(time_var)/60)[0:5]}) --> \n"
            index = solution.Value(routing.NextVar(index))
        time_var = time_dimension.CumulVar(index)
        plan_output += f" Пункт ({manager.IndexToNode(index)}), Загрузка({route_load})\n"
        plan_output += f"Время, затраченное на маршрут: {str(solution.Min(time_var)/60)[0:5]} мин\n"
        plan_output += f"Загрузка на маршруте: {route_load}\n"
        print(plan_output)
        total_time += solution.Min(time_var)
        total_load += route_load
    print(f"Суммарное время маршрутов: {str(total_time/60)[0:5]} ")
    print(f"Суммарный вес перемещённого груза: {total_load} кг")

def main():
    """решение CVRPTW задачи."""
    # Создаем датасет модели на основе заполненной выше информации
    data = create_data_model()

    # Создается диспетчер индексации маршрутизации.
    manager = pywrapcp.RoutingIndexManager(
        len(data["time_matrix"]), data["num_vehicles"], data["depot"]
    )

    # Создаем модель маршрутизации
    routing = pywrapcp.RoutingModel(manager)

    # Создаем и транзитный коллбэк
    def time_callback(from_index, to_index):
        # Возвращает время, необходимое на проезд от from_node до to_node
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data["time_matrix"][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(time_callback)

    # Определяет стоимость каждой дуги (дороги). В нашем случае - время на проезд по дуге
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Добавляем ограничения вместимости
    def demand_callback(from_index):
        # Возвращает значение "потребности" каждого пункта выдачи
        from_node = manager.IndexToNode(from_index)
        return data["demands"][from_node]

    demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    routing.AddDimensionWithVehicleCapacity(
        demand_callback_index,
        0,  # резервная грузоподъемность - нулевая
        data["vehicle_capacities"],  # Максимальная грузоподъемность
        True,  # Накопительная переменная загрузки устанавливается в ноль при начале маршрута каждого ТС
        "Capacity",
    )
    time = "Time"
    routing.AddDimension(
        transit_callback_index,
        3000,#максимально возможное время ожидания в пункте
        3000, #максимальное время для ТС
        False, #Накопительная переменная времени не устанавливается в ноль при начале маршрута каждого ТС
        time
    )
    time_dimension = routing.GetDimensionOrDie(time)
    for location_index, time_window in enumerate(data["time_windows"]):
        if location_index == data["depot"]:
            continue
        index = manager.NodeToIndex(location_index)
        time_dimension.CumulVar(index).SetRange(time_window[0], time_window[1])
    depot_index = data["depot"]
    for vehicle_index in range(data["num_vehicles"]):
        index = routing.Start(vehicle_index)
        time_dimension.CumulVar(index,).SetRange(data["time_windows"][depot_index][0],data["time_windows"][depot_index][1])

    for i in range(data["num_vehicles"]):
        routing.AddVariableMinimizedByFinalizer(time_dimension.CumulVar(routing.Start(i)))
        routing.AddVariableMinimizedByFinalizer(time_dimension.CumulVar(routing.End(i)))


    # Устанавливаем эвристику первого решения
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )
    search_parameters.local_search_metaheuristic = (
        routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
    )
    search_parameters.time_limit.FromSeconds(1)

    # Вызываем решатель собранной задачи
    solution = routing.SolveWithParameters(search_parameters)

    # Выводим решение в консоль Пайтон
    if solution:
        print_solution(data, manager, routing, solution)
    else:
        print("ERROR")

if __name__ == "__main__":
    main()


