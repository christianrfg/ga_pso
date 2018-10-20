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
    best_position: float
        Particle's best known position.
    neighbors_particles: list of Particle
        Neighbors of that Particle.
    """

    def __init__(self, position, velocity, best_position):
        self.position = position
        self.velocity = velocity
        self.best_position = best_position
        self.neighbors_particles = None

    def __repr__(self):
        position_neighbors = [x.position for x in self.neighbors_particles]
        return "Particle position: {0}\nVelocity: {1}\nBest position: {2}\nPositions of neighboring particles:\n{3}".format(
            self.position, self.velocity, self.best_position, position_neighbors)

    def __str__(self):
        position_neighbors = [x.position for x in self.neighbors_particles]
        return "Particle position: {0}\nVelocity: {1}\nBest position: {2}\nPositions of neighboring particles:\n{3}".format(
            self.position, self.velocity, self.best_position, position_neighbors)
