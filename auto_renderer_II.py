import bpy
import math


"""
Automatically render the intended collections with the specified camera and specs, one collection at a time. 
Important: Backup your blender file before running this script: it applies all the transformations of your objects! 
"""
class AutoRenderer():
    def __init__(self, collections: list, camera_name="Camera", camera_type="ORTHO", 
                    output_path="./", output_name="auto_render", output_format="PNG") -> None:
        """
        collections: a list of strings, each the name of a collection
        camera_type: for now only "ORTHO" is supported. 
        """
        self.collections = collections
        self.cam = bpy.data.objects[camera_name]
        if camera_type != "ORTHO":
            raise NotImplementedError("Only orthographic camera is supported for now.")
        self.cam.data.type = camera_type
        
        self.output_path = output_path
        self.output_name = output_name
        self.output_format = output_format

        self.intended_collection = None
        
        self.reset_bbox_info()

    def activate_all_collections(self):
        """
        Mark all collections as active. 
        """
        for layer_collection in bpy.context.view_layer.layer_collection.children:
            layer_collection.exclude = False

    def deactivate_all_other_collection(self, collection_name: str):
        """
        Leave only the intended collection active.
        """
        for layer_collection in bpy.context.view_layer.layer_collection.children:
            if layer_collection.name != collection_name:
                layer_collection.exclude = True
            else:
                layer_collection.exclude = False
    
    def calculate_bounding_box(self):
        """
        Calculate the bounding box size of the intended collection. 
        The reference to the collection must have been updated. 

        Important: It applies all the transformations of your objects! Either undo afterwards, or backup your file.
        """
        bpy.ops.object.select_all(action='DESELECT')
        for obj in self.intended_collection.objects:
            if "Light" in obj.name: # skips lights for now
                continue
            # Make the object the only active one to apply transformation -> to calculate bbox correctly
            obj.select_set(True)
            bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
            for coord in obj.bound_box:
                # coord = obj.matrix_world * coord
                self.min_x = min(self.min_x, coord[0])
                self.min_y = min(self.min_y, coord[1])
                self.min_z = min(self.min_z, coord[2])
                self.max_x = max(self.max_x, coord[0])
                self.max_y = max(self.max_y, coord[1])
                self.max_z = max(self.max_z, coord[2])
            obj.select_set(False)
        self.objects_width = self.max_x - self.min_x
        self.objects_height = self.max_y - self.min_y
        self.objects_depth = self.max_z - self.min_z

    def reset_bbox_info(self):
        """
        Resets the bounding box info to default values for next collection.
        """
        self.min_x = float("inf")
        self.min_y = float("inf")
        self.min_z = float("inf")
        self.max_x = float("-inf")
        self.max_y = float("-inf")
        self.max_z = float("-inf")

        self.objects_width = 0
        self.objects_height = 0
        self.objects_depth = 0

    def set_up_camera(self):
        """
        Set up camera to fit the bounding box of the intended collection.
        Only orthogonal camera is supported for now.
        """
        self.cam.location = [(self.max_x + self.min_x) / 2, self.min_y - self.objects_height, (self.max_z + self.min_z) / 2]
        self.cam.rotation_euler = (math.pi / 2, 0, 0)
        self.cam.data.ortho_scale = max(self.objects_width, self.objects_depth) * 2
        focal_length = (self.objects_width / 2) / math.tan(math.radians(30))
        self.cam.data.lens = focal_length
    
    def render_collection(self, collection_name: str):
        """
        Render the intended collection.
        """
        # update intended colletion reference
        self.intended_collection = bpy.data.collections[collection_name]
        # deactivate all other collections
        self.deactivate_all_other_collection(collection_name)
        # calculate bounding box
        self.calculate_bounding_box()
        # set up camera
        self.set_up_camera()
        # render
        bpy.ops.render.render()
        filepath = self.output_path + self.output_name + "_" + collection_name + "." + self.output_format.lower()
        bpy.data.images["Render Result"].save_render(filepath=filepath)
        # reactivate all collections for next render
        self.activate_all_collections()
        # forget about last calculation
        self.reset_bbox_info()
    
    def auto_render(self):
        """
        Render all collections in the supplied list at instantiation.
        """
        for collection_name in self.collections:
            self.render_collection(collection_name)


if __name__ == "__main__":
    collections = ["c1", "c2", "c3", "c4"]
    output_path = "./"
    output_name = "auto_render"
    output_format = "PNG"
    auto_renderer = AutoRenderer(collections, output_path=output_path, output_name=output_name, output_format=output_format)
    auto_renderer.auto_render()

