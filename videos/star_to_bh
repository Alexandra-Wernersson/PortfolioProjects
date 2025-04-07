class StarToBH(ThreeDScene):
    def construct(self):
        # Set Camera Orientation
        frame = self.camera.frame
       
        frame.reorient(45 * DEGREES, -45 * DEGREES)
        frame.set_width(12)  # Zoom out by increasing width

        # Background Image (starry sky)
        background = ImageMobject("textures/starsky.jpeg")
        background.scale(3.5) 
        background.move_to([0, 0, -5])
        self.add(background)
        # Star Shrinking Animation in Black Space
        star = Sphere(radius=3).set_color(YELLOW).move_to([0, 0, 0])
        self.play(FadeIn(star))
        self.wait(1)

        # Star Collapsing into Black Hole
        self.play(star.animate.scale(0.1), run_time=4)
        self.wait(1)
        black_hole = Sphere(radius=0.5).set_color(BLACK).move_to([0, 0, 0])
        self.play(Transform(star, black_hole))
        self.wait(1)

        # Event Horizon Formation
        event_horizon = Circle(radius=0.5, color=WHITE).move_to([0, 0, 0])
        self.play(ShowCreation(event_horizon))
        self.wait(1)

        # Text Overlay
        schwarzschild_text = Text("Schwarzschild (1916)").scale(0.8).to_edge(UP)
        schwarzschild_text.move_to([2, 2, 1])
        schwarzschild_text.rotate(0, axis=RIGHT).set_color("#29ABCA")
        self.play(Write(schwarzschild_text))
        self.wait(3)
