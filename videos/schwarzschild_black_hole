from manimlib import *
import numpy as np

#Create spacetime curvature 
class SpaceTimeCurvature(ThreeDScene):
    def construct(self):
        # Set Camera Orientation
        frame = self.camera.frame
        #frame.reorient(45 * DEGREES, -45 * DEGREES)
        frame.set_width(25)

        # Grid Surface with Texture
        grid = TexturedSurface(
            ParametricSurface(
                lambda u, v: [u, v, 0],
                u_range=(-20, 20),
                v_range=(-20, 20),
                resolution=(50, 50)  # Higher resolution for smoother bends
            ),
            image_file="downloads/grid.jpg",
            z_index=-99,
        ).move_to(1.5 * IN)

        grid.set_shading(reflectiveness=0.1, gloss=0.1)
        self.play(ShowCreation(grid), run_time=3)
        self.wait(1)


        # Sun (Gravity Source)
        sun = Sphere(radius=1).set_color(YELLOW).move_to(ORIGIN)
        self.play(FadeIn(sun))
        self.wait(1)

        # Warp Function for Grid Curvature
        def warp_grid(p):
            d = np.linalg.norm(p[:2])
            return p + np.array([0, 0, -2.5 * np.exp(-0.1 * d**2)])

        grid.add_updater(lambda m: m.apply_function(warp_grid))
        self.wait(3)

        # Einstein Equation
        equation = Tex(r"""G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}""")
        equation.scale(1.5).move_to([4, 4, 1])
        equation.rotate(PI / 2, axis=RIGHT).set_color("#29ABCA")
        self.play(Write(equation))
        self.wait(2)
        
        challenge = Text("How do you measure distance on a curved spacetime?")
        challenge.scale(1.5).move_to([4, 4, 1.5])
        challenge.rotate(PI / 2, axis=RIGHT).set_color("#29ABCA")
        self.play(FadeOut(equation),Write(challenge))
        self.wait(2)
        # Orbit Animation

        earth = Dot(radius=0.2, color=BLUE).move_to([8, 0, 0])
        orbit = Circle(radius=8, color=WHITE).rotate(PI / 2)
        self.play(ShowCreation(orbit), FadeIn(earth))
        self.play(MoveAlongPath(earth, orbit), run_time=6, rate_func=linear)
