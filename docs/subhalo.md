# Load Subhalo data

```
    def get_subhalo(self, halo_id):
        
        self.subhalo = il.groupcat.loadSingle(self.basePath, self.snapshot_number,subhaloID =halo_id)
        
        
        self.center = self.subhalo["SubhaloPos"]
        self.mass = self.subhalo["SubhaloMassType"][self.PartTypeDict[self.particle_type]]*1e10
        self.halfmassrad = self.subhalo["SubhaloHalfmassRadType"][self.PartTypeDict[self.particle_type]]
```