def mask_ocean(da):
    """Mask ocean areas"""
    land = regionmask.defined_regions.natural_earth_v5_0_0.land_110
    mask = land.mask(da, lon_name="lon", lat_name="lat")
    da_new = da.where(~np.isnan(mask))
    return da_new
