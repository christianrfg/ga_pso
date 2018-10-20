class Particle:
    """
    Description
    ---------
    Class that represents one particle in the PSO.
    
    Attributes
    ---------
    x: numpy array
        Uniformly distributed random vector.
    velocity: float
        Particle's velocity.
    """
    def __init__(self, x, velocity, fx):
        self.x = x
        self.velocity = velocity
        self.fx = fx

    def __repr__(self):
        return "x: {0}\nVelocity: {1}\nF(x): {2}\n".format(
            self.x, self.velocity, self.fx)
    
    def __str__(self):
        return "x: {0}\nVelocity: {1}\nF(x): {2}\n".format(
            self.x, self.velocity, self.fx)
    
    def set_neighbors(self, particulas):
        self.neighbors = particulas
        
    def set_fx(self, fx):
        self.fx = fx