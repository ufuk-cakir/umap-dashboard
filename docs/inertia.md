# Calculate Moment of Inertia Tensor

We calculate the moment of inertia Tensor in order to find the principal axes for the face on rotation of the Galaxy.
First we calculate the radial distance of each star particle to the center of the subhalo:

```
def radial_distance(coords,center):
    d = coords-center
    r_i = d**2
    r= np.sqrt(np.sum(r_i, axis = 1))
    return(r)
```

Then we can calculate the inertia tensor as follows:

```
def momentOfIntertia(rHalf, subhalo_pos,stars, ):
    """ Calculate the moment of inertia tensor (3x3 matrix) for a subhalo-scope particle set."""
    rad = radial_distance(coords = stars["Coordinates"], center = subhalo_pos) 
    wGas = np.where((rad <= 2.0*rHalf))[0] 
    masses = stars["Masses"][wGas] ]
    xyz = stars["Coordinates"][wGas,:]   
    #Shift
    xyz = np.squeeze(xyz)


    if xyz.ndim == 1:
        xyz = np.reshape( xyz, (1,3) )

    for i in range(3):
        xyz[:,i] -= subhalo_pos[i]

    I = np.zeros( (3,3), dtype='float32' )

    I[0,0] = np.sum( masses * (xyz[:,1]*xyz[:,1] + xyz[:,2]*xyz[:,2]) )
    I[1,1] = np.sum( masses * (xyz[:,0]*xyz[:,0] + xyz[:,2]*xyz[:,2]) )
    I[2,2] = np.sum( masses * (xyz[:,0]*xyz[:,0] + xyz[:,1]*xyz[:,1]) )
    I[0,1] = -1 * np.sum( masses * (xyz[:,0]*xyz[:,1]) )
    I[0,2] = -1 * np.sum( masses * (xyz[:,0]*xyz[:,2]) )
    I[1,2] = -1 * np.sum( masses * (xyz[:,1]*xyz[:,2]) )
    I[1,0] = I[0,1]
    I[2,0] = I[0,2]
    I[2,1] = I[1,2]

    return I

```