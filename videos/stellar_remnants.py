from manimlib import *
import numpy as np

class StellarRemnants(ThreeDScene):
    def construct(self):
        # Set Camera Orientation
        frame = self.camera.frame
        frame.reorient(45 * DEGREES, -45 * DEGREES)
        frame.set_width(12)  # Zoom out to view full animation

        # Background Image (starry sky)
        background = ImageMobject("textures/starsky.jpeg")
        background.scale(3.5)
        background.move_to([0, 0, -5])
        self.add(background)

        # Neutron Star Formation with Color
        neutron_star = Sphere(radius=1).set_color(BLUE)
        neutron_text = Text("Neutron Star (1.4–3 M☉)").scale(0.7).move_to([0, 2, 0]).set_color(BLUE)

        # Display the neutron star and text
        self.play(FadeIn(neutron_star))
        self.play(Write(neutron_text))
        self.wait(2)
        self.play(FadeOut(neutron_text))

        # Transition to White Dwarf (using color)
        white_dwarf = Sphere(radius=0.7).set_color(GREY)
        dwarf_text = Text("White Dwarf (≤ 1.4 M☉)").scale(0.7).move_to([0, 3, 0]).set_color(WHITE)

        # Remove neutron star and create the white dwarf
        self.play(FadeOut(neutron_star))

        # Show white dwarf
        self.play(FadeIn(white_dwarf))
        self.play(Write(dwarf_text))
        self.wait(2)
        self.play(FadeOut(dwarf_text))

        # Transition to Black Hole (using color)
        black_hole = Sphere(radius=0.5).set_color(BLACK)
        bh_text = Text("Black Hole (≥ 3 M☉)").scale(0.7).move_to([0, 3, 0]).set_color(WHITE)

        # Transition sphere from white dwarf to black hole (using scaling effect here)
        self.play(white_dwarf.animate.scale(0.1), run_time=3)
        self.play(Transform(white_dwarf, black_hole))
        self.play(Write(bh_text))
        self.wait(2)

        # Labels for Thresholds
        chandrasekhar_text = Text("Chandrasekhar Limit (1.4 M☉)").scale(0.6).to_edge(UP).set_color(WHITE)
        tov_text = Text("Tolman–Oppenheimer–Volkoff Limit (3 M☉)").scale(0.6).to_edge(DOWN).set_color(WHITE)
        self.play(Write(chandrasekhar_text), Write(tov_text))
        self.wait(3)

        # Fade Out
        self.play(FadeOut(white_dwarf), FadeOut(black_hole), FadeOut(chandrasekhar_text), FadeOut(tov_text), FadeOut(background))
        self.wait(2)


class NeutronStarCollapse(ThreeDScene):
    def construct(self):
        # Set Camera Orientation
        frame = self.camera.frame
        frame.reorient(45 * DEGREES, -45 * DEGREES)
        frame.set_width(12)  # Zoom out to view full animation

        # Background Image (starry sky)
        background = ImageMobject("textures/starsky.jpeg")
        background.scale(3.5)
        background.move_to([0, 0, -5])
        self.add(background)

        # Neutron Star Formation
        neutron_star = Sphere(radius=1.2).set_color(BLUE)
        neutron_text = Text("Neutron Star").scale(0.9).move_to([0, 3, 0]).set_color(BLUE)
        self.play(FadeIn(neutron_star))
        self.play(Write(neutron_text))
        self.wait(2)

        # Mass Increase Effect
        self.play(neutron_star.animate.scale(1.2), run_time=3)
        self.wait(2)


        # TOV Limit Display
        tov_text = Text("TOV Limit (~2-3 M☉)").scale(0.9).move_to([0,2,0]).set_color(BLUE)
        self.play(Write(tov_text))
        self.wait(2)
        
        # Collapse to Black Hole
        self.play(neutron_star.animate.scale(0.1), run_time=3)
        black_hole = Sphere(radius=0.5).set_color(BLACK)
        bh_text = Text("Black Hole").scale(0.9).move_to([0, 1.8, 0]).set_color(BLUE)
        self.play(FadeOut(neutron_text))
        self.play(FadeOut(tov_text))
        self.play(Transform(neutron_star, black_hole))
        self.play(Write(bh_text))
        self.wait(4)

        # Fade Out
        self.play(FadeOut(bh_text), FadeOut(tov_text), FadeOut(background))
        self.wait(2)

class MainCharacterTimeline(InteractiveScene):
    def construct(self):
        # Add the timeline
        frame = self.frame

        timeline = NumberLine(
            (1925, 1945, 10),
            tick_size=0.1,
            longer_tick_multiple=2,
            big_tick_spacing=10,
            unit_size=0.5 
        )
        numbers =timeline.add_numbers(
            range(1925, 1945, 20),
            group_with_commas=False,
            font_size=20,
            buff=0.15
        )
       # for number in numbers[:5]:
       #     number.remove(number[0])
       #     bce = Text("BCE")
        #    bce.set_height(0.75 * number.get_height())
         #   bce.next_to(number, RIGHT, buff=0.05, aligned_edge=DOWN)
         #   number.add(bce)
         #   number.shift(0.15 * LEFT)

        self.add(timeline)
        frame.move_to(timeline.n2p(1939))

        # Characters
        characters = [
            ("Tolman–Oppenheimer–Volkoff limit", 1939, 1940, 0.2, BLUE_D),
            ("Chandrasekhar limit", 1930, 1931, 0.2, RED_C),
        #    ("Copernicus", 1473, 1543, 0.2, RED_A),
         #   ("Brahe", 1546, 1601, 0.5, RED_E),
        ]
        character_labels = VGroup()
        for name, start, end, offset, color in characters:
            line = Line(timeline.n2p(start), timeline.n2p(end))
            line.set_stroke(color, 2)
            line.shift(offset * UP)
            # name_mob = Text(name, font_size=24)
            name_mob = Text(name, font_size=18)
            name_mob.set_color(color)
            name_mob.next_to(line, UP, buff=0.05)
            dashes = VGroup(
                DashedLine(line.get_start(), timeline.n2p(start), dash_length=0.01),
                DashedLine(line.get_end(), timeline.n2p(end), dash_length=0.01),
            )
            dashes.set_stroke(color, 1.5)
            line_group = VGroup(line, name_mob, dashes)
            character_labels.add(line_group)

        images = Group(
            ImageMobject("images/TOV_trio.gif"),
            ImageMobject("images/Chandrasekhar.gif"),
        )
        for image, character_label in zip(images, character_labels):
            image.set_height(2.0)
            image.next_to(character_label, UP)

        # Add greeks
        frame.set_height(5).move_to(timeline.n2p(1939))
        frame.set_y(0.5)

        # Add vertical dashed lines beneath 1930 and 1939
        dashed_1930 = DashedLine(
            timeline.n2p(1930), timeline.n2p(1930) + 0.5 * DOWN, dash_length=0.05
        ).set_stroke(WHITE, 1.5)

        dashed_1939 = DashedLine(
            timeline.n2p(1939), timeline.n2p(1939) + 0.5 * DOWN, dash_length=0.05
        ).set_stroke(WHITE, 1.5)

        # Add year labels
        year_1930 = Text("1930", font_size=24).set_color(WHITE)
        year_1939 = Text("1939", font_size=24).set_color(WHITE)

        # Positioning below the timeline
        year_1930.next_to(dashed_1930, DOWN, buff=0.1)
        year_1939.next_to(dashed_1939, DOWN, buff=0.1)

        # Add them to the scene
        self.play(FadeIn(year_1930), FadeIn(year_1939))

        self.play(
            FadeIn(character_labels[0], lag_ratio=0.1),
        )
        self.wait()
        self.play(
            FadeIn(character_labels[1], lag_ratio=0.1),
            FadeIn(images[1], 0.5 * UP),
            frame.animate.set_height(6).match_x(timeline.n2p(1930)).set_anim_args(run_time=3),
        )
        self.wait(7)



class MassScale(InteractiveScene):
    def construct(self):
        # Set up mass axis (1 to 4 Solar Masses)
        # Set up mass axis (1 to 4 Solar Masses)
        mass_axis = NumberLine(
            x_range=(1, 4, 0.5),  # (start, end, step)
            unit_size=3, 
            tick_size=0.1
        )
        mass_axis_label = Text("Mass (M☉)", font_size=24).next_to(mass_axis, DOWN)

        # Add mass axis
        self.play(ShowCreation(mass_axis), Write(mass_axis_label))
        title = Text("Cosmic Hierarchy", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(2)

        # Important mass points
        important_masses = [1.4, 2.2, 3]
        labels = ["White Dwarf (≤ 1.4 M☉)", "Neutron Star (1.4 – 3 M☉)", "TOV Limit (~3 M☉)"]
        colors = [WHITE, BLUE_D, RED_C]

        for mass, label, color in zip(important_masses, labels, colors):
            # Dashed line
            dash = DashedLine(
                mass_axis.number_to_point(mass), 
                mass_axis.number_to_point(mass) + 0.1 * DOWN, 
                stroke_width=2
            )
            # Label
            mass_label = Text(label, font_size=20).set_color(color)
            mass_label.next_to(dash, UP, buff=0.2)

            self.play(ShowCreation(dash), Write(mass_label))
        # White Dwarf (1.4 M☉)
        wd_mass = 1.4
        wd_label = Text("White Dwarf (≤ 1.4 M☉)", font_size=20).set_color(WHITE)
        wd_label.next_to(mass_axis.number_to_point(wd_mass), UP, buff=0.1)
        wd_dash = DashedLine(mass_axis.number_to_point(wd_mass), stroke_width=2)

        # Neutron Star (2-3 M☉)
        ns_mass = 2  # Mark neutron star at 2.0 M☉
        ns_label = Text("Neutron Star (1.4 – 3 M☉)", font_size=20).set_color(BLUE_D)
        ns_label.next_to(mass_axis.number_to_point(ns_mass), UP, buff=0.1)
        ns_dash = DashedLine(mass_axis.number_to_point(ns_mass), ns_label.get_bottom(), stroke_width=2)

        # TOV Limit (3 M☉)
        tov_mass = 3.0
        tov_label = Text("TOV Limit (~3 M☉)", font_size=20).set_color(RED_C)
        tov_label.next_to(mass_axis.number_to_point(tov_mass), UP, buff=0.1)
        tov_dash = DashedLine(mass_axis.number_to_point(tov_mass), tov_label.get_bottom(), stroke_width=2)

        # Add Labels and Dashes
        self.play(ShowCreation(wd_dash))
        self.play(ShowCreation(ns_dash))
        self.play(ShowCreation(tov_dash))


        # Add Images (Optional)
        wd_image = ImageMobject("images/WhiteDwarf.png").scale(0.45).next_to(wd_label, UP)
        ns_image = ImageMobject("images/NeutronStar.jpg").scale(0.45).next_to(ns_label, UP)
        tov_image = ImageMobject("images/BlackHole.jpg").scale(0.5).next_to(tov_label, UP)

        self.play(FadeIn(wd_image), FadeIn(ns_image), FadeIn(tov_image))

        # Wait and fade out
        self.wait(3)
        ns_text = Text("Stars 1.4 – ~3 M☉ collapse into neutron stars supported by neutron degeneracy pressure", font_size=25)
        ns_text.to_edge(DOWN).shift(UP*1.2)
        self.play(Write(ns_text))
        self.wait(2)

        tov_text = Text("Stars above 3M☉ must collapse into a black hole", font_size=25)
        tov_text.to_edge(DOWN).shift(UP*0.8)
        self.play(Write(tov_text))
        self.wait(2)
        self.play(FadeOut(wd_label), FadeOut(ns_label), FadeOut(tov_label),
                  FadeOut(wd_dash), FadeOut(ns_dash), FadeOut(tov_dash),
                  FadeOut(wd_image), FadeOut(ns_image), FadeOut(tov_image),
                  FadeOut(mass_axis), FadeOut(mass_axis_label))

from manimlib import *

class ChandrasekharLimit(ThreeDScene):
    def construct(self):
        # Set Camera Orientation
        frame = self.camera.frame
        frame.reorient(45 * DEGREES, -45 * DEGREES)
        frame.set_width(12)  # Zoom out to view full animation
        frame.set_color(BLACK)


        # Create White Dwarf
        white_dwarf = Sphere(radius=1, color=BLUE).move_to(ORIGIN)
        wd_label = Text("White Dwarf (≤ 1.4 M☉)", font_size=24).next_to(white_dwarf, UP)
        
        # Electron Degeneracy Pressure Arrows
        arrows = VGroup(*[Arrow(ORIGIN, UP * 0.5, buff=0.1, color=BLUE) for _ in range(8)])
       # arrows.arrange_in_grid(rows=2, cols=4).move_to(white_dwarf)
        arrows.arrange_in_grid(2, 4).move_to(white_dwarf)

        # Add initial scene
        self.play(FadeIn(white_dwarf), Write(wd_label), LaggedStart(*[GrowArrow(a) for a in arrows], lag_ratio=0.1))
        self.wait(3)

        # Increase mass past 1.4 M☉
        self.play(white_dwarf.animate.scale(1.2), wd_label.animate.set_opacity(0.6))
        wd_label_1_4 = Text("> 1.4 M☉", font_size=24, color=RED).next_to(white_dwarf, UP)
        self.play(Transform(wd_label, wd_label_1_4), FadeOut(arrows))
        self.wait(2)

        # Explanation Text
        explanation0 = Text("TOV Limit: General Relativity", font_size=25, color=YELLOW)
        explanation0.to_edge(DOWN).shift(UP * 1.2)
        self.play(Write(explanation0))
        self.wait(3)
        # Explanation Text
        explanation = Text("Chandrasekhar's Limit: Quantum Mechanics & Special Relativity", font_size=25, color=YELLOW)
        explanation.to_edge(DOWN).shift(UP * 0.8)
        self.play(Write(explanation))
        self.wait(3)

        # Collapse into a Neutron Star
        neutron_star = Sphere(radius=0.5, color=PURPLE).move_to(ORIGIN)
        ns_label = Text("Neutron Star (1.4 - 3 M☉)", font_size=24).next_to(neutron_star, UP)
        collapse_arrows = VGroup(*[Arrow(UP * 0.5, ORIGIN, buff=0.1, color=RED) for _ in range(8)])
        collapse_arrows.arrange_in_grid(2, 4).move_to(white_dwarf)

        self.play(FadeOut(white_dwarf), FadeIn(neutron_star), FadeIn(collapse_arrows), Write(ns_label))
        self.wait(2)
        
        # Fade out
        self.play(FadeOut(neutron_star), FadeOut(ns_label), FadeOut(collapse_arrows), FadeOut(explanation))
        self.wait()
