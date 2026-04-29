def place_stations(houses, radius=4):
    houses = sorted(houses)
    stations = []
    i = 0
    
    while i < len(houses):
        station = houses[i] + radius
        stations.append(station)
        while i < len(houses) and houses[i] <= station + radius:
            i += 1
    return stations


houses = [1, 5, 10, 15, 22, 23, 30]
stations = place_stations(houses)
print("Станции:", stations)
print("Количество:", len(stations))

for h in houses:
    assert any(abs(h - s) <= 4 for s in stations), f"Дом {h} не покрыт!"
print("Все дома покрыты")
