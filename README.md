# Blender-Auto-Renderer
Automatically renders your collections one by one, in proper side views. 

### Getting Started: 
1. Go to your blender file, move objects into collections. Say you want to render objects in "collection1" and "collection2" separately, then move anything else to some other collection. 

2. Modify the "main function" of the auto_renderer_II.py file: 

  a) update the collections: 
  
    collections = ["collection1", "collection2"]
    
  b) other changes: output paths and names etc. It outputs to the blender file's directory by default. (Only PNG format is tested, other formats should work also if supported by blender)
    
3. Go to Blender, open the Scripting tab, open the script, run it (hotkey by default should be Alt + P). 

You now have one or multiple side views of your collections in intended directory: 
  ![图片](https://user-images.githubusercontent.com/54278583/211157150-55760fdd-ec4e-4f53-bd7f-718091bdc776.png)
 
 
### Important: 
If your camera ends up in strange positions, check if you haven't applied scales to your objects! 
