# Load Particle Data
```
 def get_particle_data(self,halo_id):
        print("loading data.")
        self.stars = il.snapshot.loadSubhalo(self.basePath, self.snapshot_number, self.halo_id, "stars")
        
        #self.gas = il.snapshot.loadSubhalo(self.basePath, self.snapshot_number, self.halo_id, "gas") SOME GALAXIES HAVE TO MUCH GAS PARTICLES, PROCESS GETS KILLED
   
        print("finished.")
```	