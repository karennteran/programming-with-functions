import math
# the storage efficiency of a steel can is computed by dividing by the volume of a can by its surface area.

# volume is equal to pi times radius elevated to the two power times height

# surface area is equal to two times pi (radius plus height)




def main():
   can_size = "#1 Picnic"
   radius = 6.83
   height = 10.16
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "#1 Tall"
   radius = 7.78
   height = 11.91
   volume = compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "#2"
   radius = 8.73
   height = 11.59
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "#2.5"
   radius = 10.32
   height = 11.91
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "3 cylinder"
   radius = 10.79
   height = 17.78
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")
   


   can_size = "#5"
   radius = 13.02
   height = 14.29
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   stor_effi = compute_storage_efficiency(radius, height)
   print(f"{can_size} {storage_efficiency:.1f} {stor_effi}")


   can_size ="#6z"
   radius = 5.4
   height = 8.89
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "#8z short"
   radius = 6.83
   height = 7.62
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "#10"
   radius = 15.72
   height = 17.78
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "#211"
   radius = 6.83
   height = 12.38
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "#300"
   radius = 7.62
   height = 11.27
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


   can_size = "#303"
   radius = 8.1
   height = 11.11
   volume =  compute_volume(radius, height)
   surface_area = compute_surface_area(radius, height)
   storage_efficiency = volume / surface_area
   print(f"{can_size} {storage_efficiency:.1f}")


# volume is equal to pi times radius elevated to the two power times height
def compute_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume


# surface area is equal to two times pi (radius plus height)
def compute_surface_area(radius, height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    efficiency = volume / surface_area
    return efficiency



# calling main function
main()