# Calculate the Rotation Matrix for Face On Rotation

This function takes the moment of inertia tensor as an input calculates its eigenvectors in the first step.

(BILDER EINFÜGEN, WIE WIR DIE GALAXIEN ROTIEREN WOLLEN)


```
def rotationMatrix(inertiaTenor, return_value = "face-on"):
    """ Calculate 3x3 rotation matrix by a diagonalization of the moment of inertia tensor.
    Note the resultant rotation matrices are hard-coded for projection with axes=[0,1] e.g. along z. """

    # get eigen values and normalized right eigenvectors
    eigen_values, rotation_matrix = np.linalg.eig(inertiaTenor)

    # sort ascending the eigen values
    sort_inds = np.argsort(eigen_values)
    eigen_values = eigen_values[sort_inds]

    # permute the eigenvectors into this order, which is the rotation matrix which orients the
    # principal axes to the cartesian x,y,z axes, such that if axes=[0,1] we have face-on
    new_matrix = np.matrix( (rotation_matrix[:,sort_inds[0]],
                             rotation_matrix[:,sort_inds[1]],
                             rotation_matrix[:,sort_inds[2]]) )

    # make a random edge on view   ---> rotation entlang x achse
    #new_matrix auf eigenvektor, winkel berechnen, rotation matrix bauen
    phi = np.random.uniform(0, 2*np.pi)
    theta = np.pi / 2
    psi = 0

    A_00 =  np.cos(psi)*np.cos(phi) - np.cos(theta)*np.sin(phi)*np.sin(psi)
    A_01 =  np.cos(psi)*np.sin(phi) + np.cos(theta)*np.cos(phi)*np.sin(psi)
    A_02 =  np.sin(psi)*np.sin(theta)
    A_10 = -np.sin(psi)*np.cos(phi) - np.cos(theta)*np.sin(phi)*np.cos(psi)
    A_11 = -np.sin(psi)*np.sin(phi) + np.cos(theta)*np.cos(phi)*np.cos(psi)
    A_12 =  np.cos(psi)*np.sin(theta)
    A_20 =  np.sin(theta)*np.sin(phi)
    A_21 = -np.sin(theta)*np.cos(phi)
    A_22 =  np.cos(theta)

    random_edgeon_matrix = np.matrix( ((A_00, A_01, A_02), (A_10, A_11, A_12), (A_20, A_21, A_22)) )

    # prepare return with a few other useful versions of this rotation matrix
    r = {}
    r['face-on'] = new_matrix
    r['edge-on'] = np.matrix( ((1,0,0),(0,0,1),(0,-1,0)) ) * r['face-on'] # disk along x-hat
    r['edge-on-smallest'] = np.matrix( ((0,1,0),(0,0,1),(1,0,0)) ) * r['face-on']
    r['edge-on-y'] = np.matrix( ((0,0,1),(1,0,0),(0,-1,0)) ) * r['face-on'] # disk along y-hat
    r['edge-on-random'] = random_edgeon_matrix * r['face-on']
    r['phi'] = phi
    

    return r[return_value]

```