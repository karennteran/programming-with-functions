import math
from subprocess import list2cmdline

def main():

    name = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z Short", "#10", "#211", "#211", "#300", "#303"]
    radius = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    cost = [0.28, 0.43, 0.45, 0.61, 0.86, 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]
    
    max_cost_efficiency = 0
    max_name = ""
    
    for x in range(len(cost)):
        
        volume = compute_volume(radius[x], height[x])
        surface_area = compute_surface_area(radius[x], height[x])
        storage_efficiency = compute_storage_efficiency(volume, surface_area)
        cost_efficiency = compute_cost_efficiency(volume, cost[x])
        print(f"{name[x]} {storage_efficiency:.1f} ${cost_efficiency:.2f}")   

        if cost_efficiency > max_cost_efficiency:
            max_cost_efficiency = cost_efficiency
            max_name = name[x]

    print(f"The can with the highest cost effieciency is {max_name} with a cost efficiency of ${max_cost_efficiency:.2f}") 


    # name = "#1 Picnic"
    # radius = 6.83 list[0]
    # height = 10.16 list[0]
    # cost = 0.28
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#1 Tall"
    # radius = 7.78
    # height = 11.91
    # cost = 0.43
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#2"
    # radius = 8.73
    # height = 11.59
    # cost = 0.45
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#2.5"
    # radius = 10.32
    # height = 11.91
    # cost = 0.61
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#3 Cylinder"
    # radius = 10.79
    # height = 17.78
    # cost = 0.86
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#5"
    # radius = 13.02
    # height = 14.29
    # cost = 0.83
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#6Z"
    # radius = 5.40
    # height = 8.89
    # cost = 0.22
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#8Z short"
    # radius = 6.83
    # height = 7.62
    # cost = 0.26
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#10"
    # radius = 15.72
    # height = 17.78
    # cost = 1.53
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#211"
    # radius = 6.83
    # height = 12.38
    # cost = 0.34
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#300"
    # radius = 7.62
    # height = 11.27
    # cost = 0.38
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

    # name = "#303"
    # radius = 8.10
    # height = 11.11
    # cost = 0.42
    # volume = compute_volume(radius, height)
    # surface_area = compute_surface_area(radius, height)
    # storage_efficiency = compute_storage_efficiency(volume, surface_area)
    # cost_efficiency = compute_cost_efficiency(volume, cost)
    # print(f"{name} {storage_efficiency:.1f} ${cost_efficiency:.2f}")

def compute_volume(radius, height):
    """Computes the volume of a cylinder
        parameters = 
            radius of base
            height of cylinder
        returns = 
            volume of cylinder"""
    
    volume = math.pi * radius ** 2 * height
    return volume

def compute_surface_area(radius, height):
    """"Computes surface area of cylinder
        Parameters = 
            radius of base
            height of cylinder
        returns =
            surface area of cylinder"""
    
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(volume, surface_area):
    """Compute storage efficiency of cans
        Parameters =
            volume of can
            surface area of can
        returns =
            storage efficiency of can"""
    
    storage_efficiency = volume / surface_area
    return storage_efficiency

def compute_cost_efficiency(volume, cost):
    """Computes the cost effienciency of the can
        parameter =
            volume of can
            cost of can
        returns = 
            cost effienciency of can"""
    
    cost_efficiency = volume / cost
    return cost_efficiency

main()
