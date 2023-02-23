from .functions.config_profile.profile import search_profile
from .functions.config_layer.layer import get_layer
from .functions.plotting.plot import plot_data

# def only_profile():
#     elevation_profile, number_of_elpoints = search_profile()
#     plot_data(elevation_profile, number_of_elpoints)

def profile_layers(datadir):
    elevation_profile, number_of_elpoints = search_profile(datadir)
    layers_points = get_layer(elevation_profile.copy(), datadir)
    plot_data(elevation_profile, number_of_elpoints, layers_points, datadir)
