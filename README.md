# Blender-Auto-Renderer
Automatically renders your collections one by one, in proper side views. 

### Important: 
***Back up*** your file before running this scripts: it **applies all the transformation** of your objects. 
This is due to the use of bound box in determining camera position. Theoretically you can undo right after, but since your operation will involve changing the scripts (editing the collection names), sometimes the undo history will be messed up. So backup is still recommended. 

### Getting Started: 
1. Go to your blender file, move objects into collections. Say you want to render objects in "collection1" and "collection2" separately, then move anything else to some other collection. 

2. Modify the "main function" of the auto_renderer_II.py file: 

  a) update the collections: 
  
    collections = ["collection1", "collection2"]
    
  b) other changes: output paths and names etc. It outputs to the blender file's directory by default. (Only PNG format is tested, other formats should work also if supported by blender)
    
3. Go to Blender, open the Scripting tab, open the script, run it (hotkey by default should be Alt + P). 

You now have one or multiple side views of your collections in intended directory: 
  ![auto_render_c1](https://user-images.githubusercontent.com/54278583/211163132-35e0dee4-e5dd-43bd-b435-c682acf7655a.png)
![auto_render_c2](https://user-images.githubusercontent.com/54278583/211163135-c9374e4c-e7c3-4fa7-afca-feba03bc6128.png)
![auto_render_c3](https://user-images.githubusercontent.com/54278583/211163137-c028f4f9-1058-410f-96b8-8567002a3456.png)
![auto_render_c4](https://user-images.githubusercontent.com/54278583/211163139-e1498d32-09d8-4cd0-87a0-f0419e2afb2b.png)
