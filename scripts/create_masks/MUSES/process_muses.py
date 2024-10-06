#! /usr/bin/env python3
import pathlib
from PIL import Image

# Create coarse semantic segmentation mask
# of combined classes
def createMask(colorMap):

    # Initializing and loading pixel data
    row, col = colorMap.size
    px = colorMap.load()
    coarseSegColorMap = Image.new(mode="RGB", size=(row, col))
    cx = coarseSegColorMap.load()

    # Colourmaps for classes
    sky_colour = (61, 184, 255)
    background_objects_colour = (61, 93, 255)
    vulnerable_living_colour = (255, 61, 61)
    small_mobile_vehicle_colour = (255, 190, 61)
    large_mobile_vehicle_colour = (255, 116, 61)
    road_edge_delimiter_colour = (216, 255, 61)
    road_colour = (0, 255, 220)

    # Extracting classes and assigning to colourmap
    for x in range(row):
        for y in range(col):

            # SKY
            if px[x, y] == (70,130,180):
                cx[x,y] = sky_colour

            # BACKGROUND OBJECTS
            # Building    
            elif px[x,y] == (70, 70, 70):
                cx[x,y] = background_objects_colour
            # Pole  
            elif px[x,y] == (153, 153, 153):
                cx[x,y] = background_objects_colour
            # Traffic Light
            elif px[x,y] == (250, 170, 30):
                cx[x,y] = background_objects_colour 
            # Traffic Sign
            elif px[x,y] == (220, 220, 0):
                cx[x,y] = background_objects_colour 
            # Vegetation
            elif px[x,y] == (107, 142, 35):
                cx[x,y] = background_objects_colour
            # Terrain
            elif px[x,y] == (152, 251, 152):
                cx[x,y] = background_objects_colour

            # VULNERABLE LIVING
            # Person
            elif px[x,y] == (220, 20, 60):
                cx[x,y] = vulnerable_living_colour

            # SMALL MOBILE VEHICLE
            # Rider
            elif px[x,y] == (255, 0, 0):
                cx[x,y] = small_mobile_vehicle_colour
            # Motorcylce
            elif px[x,y] == (0, 0, 230):
                cx[x,y] = small_mobile_vehicle_colour
            # Bicycle
            elif px[x,y] == (119, 11, 32):
                cx[x,y] = small_mobile_vehicle_colour

            # LARGE MOBILE VEHICLE
            # Car
            elif px[x,y] == (0, 0, 142):
                cx[x,y] = large_mobile_vehicle_colour
            # Truck
            elif px[x,y] == (0, 0, 70):
                cx[x,y] = large_mobile_vehicle_colour
            # Bus
            elif px[x,y] == (0, 60, 100):
                cx[x,y] = large_mobile_vehicle_colour
            # Train
            elif px[x,y] == (0, 80, 100):
                cx[x,y] = large_mobile_vehicle_colour
            
            # ROAD EDGE DELIMITER
            # Wall
            elif px[x,y] == (102, 102, 156):
                cx[x,y] = road_edge_delimiter_colour
            # Fence
            elif px[x,y] == (190, 153, 153):
                cx[x,y] = road_edge_delimiter_colour

            # ROAD
            elif px[x,y] == (128, 64, 128):
                cx[x,y] = road_colour

    return coarseSegColorMap

# Reading dataset labels and images and sorting returned list in alphabetical order
labels = sorted([f for f in pathlib.Path('/home/zain/Autoware/semantic_segmentation/training_data/MUSES/ground_truth/labels/').glob("*labelColor.png")])
images = sorted([f for f in pathlib.Path('/home/zain/Autoware/semantic_segmentation/training_data/MUSES/images/train/').glob("*.png")])

# Paths to save training data with new coarse segmentation masks
labels_save_path = '/home/zain/Autoware/semantic_segmentation/training_data/Coarse_Seg/MUSES/gt_masks/'
images_save_path = '/home/zain/Autoware/semantic_segmentation/training_data/Coarse_Seg/MUSES/images/'

# Looping through data
for index in range(0, len(labels)):
    
    # Open images and pre-existing masks
    image = Image.open(str(images[index]))
    label = Image.open(str(labels[index]))

    # Create new Coarse Segmentation mask
    coarseSegColorMap = createMask(label)

    # Save images
    image.save(images_save_path + str(index) + ".png","PNG")
    coarseSegColorMap.save(labels_save_path + str(index) + ".png","PNG")

    print(index)

print('--- COMPLETE ---')                