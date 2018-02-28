import pyelastix as px

params = px.get_default_params()

moving_image = '/Users/ian/Programming/hart/mri-images/PQ_forearm_cropped_for_ITK-SNAP_biascorr.nii'
fixed_image = '/Users/ian/Programming/hart/mri-images/sub3_forearm_cropped_for_ITK-SNAP.nii'

px.register(moving_image, fixed_image, params, verbose=2)
