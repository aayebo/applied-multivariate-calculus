def great_circle_distance(lat1, lon1, lat2, lon2, R=6371.0):
    p1, l1, p2, l2 = np.deg2rad([lat1, lon1, lat2, lon2])
    a = np.sin((p2-p1)/2)**2 + (
        np.cos(p1)*np.cos(p2)*np.sin((l2-l1)/2)**2)
    angle = 2*np.arctan2(np.sqrt(a), np.sqrt(max(0, 1-a)))
    return R*angle

print(great_circle_distance(0, 0, 0, 90, R=1))
assert np.isclose(great_circle_distance(0,0,0,90,R=1), np.pi/2)
