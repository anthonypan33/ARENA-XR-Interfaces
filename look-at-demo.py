from arena import * 
from yarl import URL

scene = Scene(host="mqtt.arenaxr.org", scene='examplev2', debug=True)

BUTTON_MODELS = {
    # "fertilizer": "store/users/azp/Models/Plant_ui/final_buttons/fert_button_finalv2.glb",
    "fertilizer": "store/users/azp/Models/unchecked_yup/fert_button_unchecked.glb",
    "water": "store/users/azp/Models/unchecked_yup/water_button_unchecked.glb", 
    "light": "store/users/azp/Models/unchecked_yup/light_button_unchecked.glb",
    "plant_info": "store/users/azp/Models/unchecked_yup/info_button_unchecked.glb"
}


POPUP_MODELS = {
    "orchid": {
        "fertilizer": "store/users/azp/Models/unchecked_yup/fert_pop_unchecked.glb",
        "water": "store/users/azp/Models/unchecked_yup/waterorchid_pop_unchecked.glb",
        "light": "store/users/azp/Models/unchecked_yup/lightorchid_pop_unchecked.glb", 
        "plant_info":"store/users/azp/Models/unchecked_yup/infoorchid_pop_unchecked.glb"
    }, 
    "jade": {
        "fertilizer": "store/users/azp/Models/unchecked_yup/fertjade_pop_unchecked.glb",
        "water": "store/users/azp/Models/unchecked_yup/waterjade_pop_unchecked.glb",
        "light": "store/users/azp/Models/unchecked_yup/lightjade_pop_unchecked.glb", 
        "plant_info": "store/users/azp/Models/unchecked_yup/infojade_pop_unchecked.glb"
    },
    "katy": {
        "fertilizer": "store/users/azp/Models/unchecked_yup/fertkaty_pop_unchecked.glb",
        "water": "store/users/azp/Models/unchecked_yup/waterkaty_pop_unchecked.glb",
        "light": "store/users/azp/Models/unchecked_yup/lightkaty_pop_unchecked.glb", 
        "plant_info":"store/users/azp/Models/unchecked_yup/infokaty_pop_unchecked.glb"
    },
    "cactus": {
        "fertilizer": "store/users/azp/Models/unchecked_yup/fertcactus_pop_unchecked.glb",
        "water": "store/users/azp/Models/unchecked_yup/watercactus_pop_unchecked.glb",
        "light": "store/users/azp/Models/unchecked_yup/lightcactus_pop_unchecked.glb", 
        "plant_info":"store/users/azp/Models/unchecked_yup/infocactus_pop_unchecked.glb"
    }
}


class PlantButtonSet:
    def __init__(self, parent_name):
        self.parent_name = parent_name
        self.active_object = None
        # POPUP_["venus_flytrap"].get("popup_model") # Will return Nnone if popup model not defined in dict, SAFE
        self.ui_container = GLTF(object_id=parent_name + "_panel_container", position=Position(0,0.05,0),scale=Scale(0.1,0.1,0.1), rotation=Rotation(0,0,0), url="store/users/azp/Models/Plant_UI_Panel_yunchecked.glb", parent=parent_name, **{"look-at": "#my-camera"})
        self.button_fertilize = GLTF(object_id=parent_name + "_fertilize_button", position=Position(-1.15,0,0.15), scale=Scale(1,1,1), rotation=Rotation(0,0,0), url=BUTTON_MODELS["fertilizer"], parent=self.ui_container.object_id)
        self.button_water = GLTF(object_id=parent_name + "_water_button", position=Position(-0.38,0,0.5), scale=Scale(1,1,1), rotation=Rotation(0,0,0), url=BUTTON_MODELS["water"], parent=self.ui_container.object_id)
        self.button_light = GLTF(object_id=parent_name + "_light_button", position=Position(0.38,0,0.15), scale=Scale(1,1,1), rotation=Rotation(0,0,0), url=BUTTON_MODELS["light"], parent=self.ui_container.object_id)
        self.button_plant_info = GLTF(object_id=parent_name + "_plant_info_button", position=Position(1.15,0,0.15), scale=Scale(1,1,1), rotation=Rotation(0,0,0), url=BUTTON_MODELS["plant_info"], parent=self.ui_container.object_id)

        scene.add_object(self.ui_container)
        scene.update_object(self.ui_container)
        
        scene.add_object(self.button_fertilize)
        scene.update_object(self.button_fertilize, click_listener=True, evt_handler=self.mouse_handler)
    
        scene.add_object(self.button_water)
        scene.update_object(self.button_water, click_listener=True, evt_handler=self.mouse_handler)
    
        scene.add_object(self.button_light)
        scene.update_object(self.button_light, click_listener=True, evt_handler=self.mouse_handler)

        scene.add_object(self.button_plant_info)
        scene.update_object(self.button_plant_info , click_listener=True, evt_handler=self.mouse_handler)

        if POPUP_MODELS.get(self.parent_name):
            self.button_fertilize.pop = self.fert_pop_func
            self.button_water.pop = self.water_pop_func
            self.button_light.pop = self.light_pop_func
            self.button_plant_info.pop = self.plant_pop_func
        

    def fert_pop_func(self):
        fert_pop = GLTF(object_id=self.parent_name + "_fertilizer_popup", position=Position(0,1.5,0), scale=Scale(1,1,1), rotation=Rotation(0,0,0), url=POPUP_MODELS[self.parent_name]["fertilizer"], parent=self.ui_container)

        scene.add_object(fert_pop)
        scene.update_object(fert_pop)

        return fert_pop

    def water_pop_func(self):
        water_pop = GLTF(object_id=self.parent_name + "_water_popup", position=Position(0,1.5,0), scale=Scale(1,1,1), rotation=Rotation(0,0,0), url=POPUP_MODELS[self.parent_name]["water"], parent=self.ui_container)

        scene.add_object(water_pop)
        scene.update_object(water_pop)

        return water_pop

    def light_pop_func(self):
        light_pop = GLTF(object_id=self.parent_name + "_light_popup", position=Position(0,1.5,0), scale=Scale(1,1,1), rotation=Rotation(0,0,0), url=POPUP_MODELS[self.parent_name]["light"], parent=self.ui_container)

        scene.add_object(light_pop)
        scene.update_object(light_pop)

        return light_pop

    def plant_pop_func(self):
        plant_pop = GLTF(object_id=self.parent_name + "_plant_info_popup", position=Position(0,1.5,0), scale=Scale(1,1,1), rotation=Rotation(0,0,0), url=POPUP_MODELS[self.parent_name]["plant_info"], parent=self.ui_container)

        scene.add_object(plant_pop)
        scene.update_object(plant_pop)

        return plant_pop

    def mouse_handler(self, scene, evt, msg):
        if (evt.type == 'mouseenter' or evt.type == 'mouseleave'):
            return

        if self.active_object is not None and evt.type == 'mouseup':
            # active_object.delete()
            print("object deleted")
            scene.delete_object(self.active_object)

        button_obj = scene.all_objects.get(evt.object_id)
        
        if not hasattr(button_obj, "pop"):
            print("no click function for this object")
            return

        if evt.type =="mousedown":
            print("mousedown")
            button_obj.dispatch_animation(
                AnimationMixer(clip="Button_down", loop="once")
                # Animation(property="position", easing="linear", dur=1000)
            )
            scene.run_animations(button_obj)
            

        if evt.type =="mouseup":
            print("mouseup")
            button_obj.dispatch_animation(
                AnimationMixer(clip="Button_up", loop="once")
            )
            scene.run_animations(button_obj)
            self.active_object=button_obj.pop()
    


@scene.run_once
def main():

    orchid_buttonset = PlantButtonSet("orchid")
    jade_buttonset = PlantButtonSet("jade")
    katy_buttonset = PlantButtonSet("katy")
    cactus_buttonset = PlantButtonSet("cactus")
    plant1_buttonset = PlantButtonSet("plant1")
    plant2_buttonset = PlantButtonSet("plant2")
    plant3_buttonset = PlantButtonSet("plant3")
    plant4_buttonset = PlantButtonSet("plant4")
    plant5_buttonset = PlantButtonSet("plant5")
    plant6_buttonset = PlantButtonSet("plant6")
    plant7_buttonset = PlantButtonSet("plant7")
    plant8_buttonset = PlantButtonSet("plant8")


scene.run_tasks()

#create function for each pop up menu
#add each function a new my_popups dictionary using same keys as my_buttons dictionary
#

