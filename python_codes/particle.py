class Particle:
    """
    Description
    ---------
    Class that represents one particle in the PSO.
    
    Attributes
    ---------
    position: numpy array
        Uniformly distributed random vector.
    velocity: float
        Particle's velocity.
    p_i: float
        Particle's best known position.
    """
    def __init__(self, position, velocity, p_i):
        self.position = position
        self.velocity = velocity
        self.p_i = p_i

    def __repr__(self):
        return "x: {0}\nVelocity: {1}\np_i: {2}\n".format(
            self.x, self.velocity, self.p_i)
    
    def __str__(self):
        return "x: {0}\nVelocity: {1}\np_i: {2}\n".format(
            self.x, self.velocity, self.p_i)

    def set_x(self, x):
        self.x = x

    def set_velocity(self, velocity):
        self.velocity = velocity
        
    def set_p_i(self, p_i):
        self.p_i = p_i