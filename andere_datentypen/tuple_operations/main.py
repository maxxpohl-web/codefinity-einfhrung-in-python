# Initial items on shelf #1 (provided as a tuple)
shelf1 = ("celery", "spinach", "cucumbers")

# Items being added to the shelf #1 (provided as a list)
shelf1_update = ["tomatoes", "celery", "cilantro"]
shelf1_update_tuple = tuple(shelf1_update)                 # aus der List wird ein Tuple

shelf1_concat = shelf1 + shelf1_update_tuple              # aus den beiden Tuple wird eine Verkettung      
celery_count = shelf1_concat.count("celery")  
                                                    # Zähle wie oft celery in dem tuple vorkommt und speichere den         
                                                   # Wert in der neue Variable                         
celery_index = shelf1_concat.index("celery")

print("Updated Shelf #1: ", shelf1_concat)
print("Number of Celery: ", celery_count)
print("Celery Index: " , celery_index)



