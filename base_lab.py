align_value = 0
cohesion_value = 0
separation_value = 1


def process_sprite_group(sprite_group, canvas):
    """Function to draw sprites on canvas, update them and delete those who became old"""
    remove_sprites = set([])
    copy_sprite_group = sprite_group.copy()

    for sprite in copy_sprite_group:
        sprite.draw(canvas)
        sprite.edges()
        sprite.perform_flocking(copy_sprite_group)

        if sprite.update(): # update returns True if the sprite became old, else False
            remove_sprites.add(sprite)

    if len(remove_sprites): # if something needs to be deleted..
        sprite_group.difference_update(remove_sprites)


class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0], vel[1]]
        self.acceleration = [0.0, 0.0]
        self.max_speed = 2
        self.max_force = 5
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def update(self):
        for i in range(DIMENSIONS):
            self.pos[i] += self.vel[i]
            self.vel[i] += self.acceleration[i]
            if self.vel[i] > self.max_speed:
                self.vel[i] = self.max_speed
            self.acceleration[i] *= 0

        self.angle += self.angle_vel
        self.age   += 1

        # return True if the sprite is old and needs to be destroyed
        if self.age < self.lifespan:
            return False
        else:
            return True

    def edges(self):
        if self.pos[0] > CANVAS_RES_LIST[0]:
            self.pos[0] = 0
        elif self.pos[0] < 0:
            self.pos[0] = CANVAS_RES_LIST[0]

        if self.pos[1] > CANVAS_RES_LIST[1]:
            self.pos[1] = 0
        elif self.pos[1] < 0:
            self.pos[1] = CANVAS_RES_LIST[1]

    def collide(self, other_object):
        """
        Method that takes as imput a sprite and another object (e.g. the ship, a sprite)
        and returns True if they collide, else False
        """
        distance = dist(self.pos, other_object.get_pos())
        sum_radii = self.radius + other_object.get_radius()

        if distance < sum_radii:
            return True
        else:
            return False

    def perform_flocking(self, boids):
        alignment = self.align(boids)
        cohesion = self.cohesion(boids)
        separation = self.separation(boids)

        for i in range(DIMENSIONS):
            alignment[i] *= align_value
            cohesion[i] *= cohesion_value
            separation[i] *= separation_value

            self.acceleration[i] += alignment[i]
            self.acceleration[i] += cohesion[i]
            self.acceleration[i] += separation[i]

    # Moving Tactics
    def align(self, boids):
        perceptionRadius = 100
        steering = [0.0, 0.0]
        total = 0

        for boid in boids:
            distance = math.dist(self.pos, boid.pos)
            if (boid != self and distance < perceptionRadius):
                for i in range(DIMENSIONS):
                    steering[i] += boid.vel[i]
                total += 1

        if total > 0:
            for i in range(DIMENSIONS):
                steering[i] = steering[i] / total
                steering[i] -= self.vel[i]
                if steering[i] > self.max_force:
                    steering[i] = self.max_force


        return steering

    def separation(self, boids):
        perceptionRadius = 50
        steering = [0.0, 0.0]
        diff = [0.0, 0.0]
        total = 0

        for boid in boids:
            distance = math.dist(self.pos, boid.pos)
            if (boid != self and distance < perceptionRadius and distance > 0):
                diff = numpy.subtract(self.pos, boid.pos).tolist()
                diff = numpy.divide(diff, distance * distance).tolist()
                steering = numpy.add(steering, diff).tolist()
                total += 1

        if total > 0:
            steering = numpy.divide(steering, total).tolist()
            steering = numpy.subtract(steering, self.vel).tolist()
            for i in range(DIMENSIONS):
                if steering[i] > self.max_force:
                    steering[i] *= self.max_force


        return steering

    def cohesion(self, boids):
        perceptionRadius = 20
        steering = [0.0, 0.0]
        total = 0

        for boid in boids:
            distance = math.dist(self.pos, boid.pos)
            if (boid != self and distance < perceptionRadius):
                for i in range(DIMENSIONS):
                    steering[i] += boid.pos[i]
                total += 1

        if total > 0:
            for i in range(DIMENSIONS):
                steering[i] = steering[i] / total
                steering[i] -= self.pos[i]
                steering[i] -= self.vel[i]
                if steering[i] > self.max_force:
                    steering[i] = self.max_force

        return steering
