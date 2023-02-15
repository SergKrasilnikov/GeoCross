from functions.config_profile.profile import search_profile
from functions.config_layer.layer import get_layer
# from functions.config_layer.layer import search_layers
from functions.plotting.plot import plot_data

# def only_profile():
#     elevation_profile, number_of_elpoints = search_profile()
#     plot_data(elevation_profile, number_of_elpoints)

def profile_layers():
    elevation_profile, number_of_elpoints = search_profile()
    layers_points = get_layer(elevation_profile.copy())
    print(elevation_profile)
    #for layer in layers_points:
        #print(layer)
    plot_data(elevation_profile, number_of_elpoints, layers_points)
