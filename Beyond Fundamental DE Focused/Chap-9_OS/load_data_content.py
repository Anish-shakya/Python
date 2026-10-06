import os

print(os.listdir(os.path.dirname(os.path.abspath(__file__))))
print(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data"))


last_load="2026-01-01"
for i in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),"data")):
    if i.split(".")[0] > last_load:
        print(f"Processing {i} new file")
    
    