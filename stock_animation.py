from manim import *

class StockAnimation(Scene):
    def construct(self):

        # =====================================================================
        # 1) TITLE SECTION
        # =====================================================================
        title = Text("Best Time to Buy and Sell Stock II", font_size=52, weight=BOLD)
        subtitle = Text("Complete Visual Explanation + Buy/Sell Animation", font_size=28)
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.3)

        self.play(FadeIn(header, shift=UP))
        self.wait(2)
        self.play(FadeOut(header))

        # =====================================================================
        # 2) EXAMPLE INTRO
        # =====================================================================
        intro = Text("Example: prices = [7, 1, 5, 3, 6, 4]", font_size=34)
        self.play(FadeIn(intro))
        self.wait(2)
        self.play(FadeOut(intro))

        # =====================================================================
        # 3) DRAW PRICE GRAPH
        # =====================================================================
        graph_title = Text("Price Graph", font_size=40)
        self.play(FadeIn(graph_title))
        self.wait(1)
        self.play(graph_title.animate.to_edge(UP))

        prices = [7, 1, 5, 3, 6, 4]

        x_start = -5
        y_base = -2
        x_step = 1.5
        y_scale = 0.25

        dots = []
        labels = []

        # Draw dot for each price
        for i, p in enumerate(prices):
            dot = Dot([x_start + i*x_step, y_base + p*y_scale, 0], color=WHITE)
            label = Text(str(p), font_size=26).next_to(dot, UP, buff=0.15)
            dots.append(dot)
            labels.append(label)

        self.play(*[FadeIn(d) for d in dots], *[FadeIn(l) for l in labels])
        self.wait(1)

        # Connect with lines
        lines = []
        for i in range(len(prices)-1):
            line = Line(dots[i].get_center(), dots[i+1].get_center(), color=GRAY)
            lines.append(line)
            self.play(Create(line), run_time=0.4)

        self.wait(1)

        # =====================================================================
        # 4) DATA-STRUCTURE STYLE BUY/SELL ANIMATION
        # =====================================================================
        pointer = Triangle(color=YELLOW, fill_opacity=1).scale(0.2)
        pointer.next_to(dots[0], DOWN, buff=0.2)
        self.play(FadeIn(pointer))

        profit_val = 0
        profit_text = Text(f"Profit: {profit_val}", font_size=34, color=GREEN).to_edge(UP)
        self.play(FadeIn(profit_text))

        buy_sell_objects = []

        # Loop through days
        for i in range(len(prices)-1):

            # Move pointer to current day
            self.play(pointer.animate.move_to(dots[i].get_center() + DOWN*0.4), run_time=0.4)

            today = prices[i]
            tomorrow = prices[i+1]

            if tomorrow > today:

                # BUY marker
                buy_arrow = Arrow(
                    dots[i].get_center() + DOWN*0.5,
                    dots[i].get_center(),
                    buff=0.1, color=GREEN
                )
                buy_label = Text("BUY", font_size=24, color=GREEN).next_to(dots[i], DOWN)
                buy_sell_objects += [buy_arrow, buy_label]

                self.play(FadeIn(buy_arrow), FadeIn(buy_label))

                # SELL marker
                sell_arrow = Arrow(
                    dots[i+1].get_center() + UP*0.5,
                    dots[i+1].get_center(),
                    buff=0.1, color=RED
                )
                sell_label = Text("SELL", font_size=24, color=RED).next_to(dots[i+1], UP)
                buy_sell_objects += [sell_arrow, sell_label]

                # Highlight line
                highlight = Line(
                    dots[i].get_center(),
                    dots[i+1].get_center(),
                    color=GREEN,
                    stroke_width=6
                )
                buy_sell_objects.append(highlight)

                # Animate segment
                self.play(
                    Create(highlight),
                    FadeIn(sell_arrow), FadeIn(sell_label),
                    pointer.animate.move_to(dots[i+1].get_center() + DOWN*0.4),
                    run_time=0.7
                )

                # Update profit
                diff = tomorrow - today
                profit_val += diff

                new_profit_text = Text(f"Profit: {profit_val}", font_size=34, color=GREEN).to_edge(UP)
                self.play(Transform(profit_text, new_profit_text))

                self.wait(0.4)

            else:
                self.play(pointer.animate.move_to(dots[i+1].get_center() + DOWN*0.4), run_time=0.4)
                self.wait(0.2)

        self.wait(1)

        # Fade out graph visuals
        self.play(*[FadeOut(m) for m in buy_sell_objects],
                  FadeOut(pointer),
                  FadeOut(graph_title),
                  *[FadeOut(d) for d in dots],
                  *[FadeOut(l) for l in labels],
                  *[FadeOut(ln) for ln in lines],
                  FadeOut(profit_text))

        # =====================================================================
        # 5) IMPROVED EXPLANATION SECTION (NEAT + CLEAN)
        # =====================================================================
        self.clear()

        explain_title = Text("How the Final Profit is Calculated", font_size=42, weight=BOLD)
        self.play(FadeIn(explain_title, shift=UP))
        self.wait(2)
        self.play(FadeOut(explain_title))

        explanation_steps = [
            "We compare each day's price with the next day's price.",
            "If the next day's price is higher → we make a transaction.",
            "We 'buy' today and 'sell' tomorrow.",
            "We add the difference (sell - buy) to our profit.",
            "This captures all rising segments of the graph.",
            "This greedy method guarantees the maximum profit possible."
        ]

        for step in explanation_steps:
            t = Text(step, font_size=32)
            self.play(FadeIn(t))
            self.wait(2)
            self.play(FadeOut(t))

        # =====================================================================
        # 6) BREAKDOWN OF THIS EXAMPLE'S ACTUAL TRANSACTIONS
        # =====================================================================
        breakdown_title = Text("Breakdown of Transactions", font_size=40, weight=BOLD)
        self.play(FadeIn(breakdown_title))
        self.wait(1.5)
        self.play(breakdown_title.animate.to_edge(UP))

        transactions = [
            "Buy at 1, Sell at 5 → Profit +4",
            "Buy at 3, Sell at 6 → Profit +3"
        ]

        y_offset = 1
        for tstep in transactions:
            tx = Text(tstep, font_size=32)
            tx.move_to([0, y_offset, 0])
            y_offset -= 1.2
            self.play(FadeIn(tx, shift=DOWN))
            self.wait(2)
            self.play(FadeOut(tx))

        # =====================================================================
        # 7) TOTAL PROFIT SUMMARY
        # =====================================================================
        summary_title = Text("Total Calculation", font_size=40)
        self.play(FadeIn(summary_title))
        self.wait(1)
        self.play(summary_title.animate.to_edge(UP))

        l1 = Text("Profit from first rise: 5 - 1 = 4", font_size=32)
        l2 = Text("Profit from second rise: 6 - 3 = 3", font_size=32)
        l3 = Text("Total Profit = 4 + 3 = 7", font_size=38, color=GREEN)

        summary_group = VGroup(l1, l2, l3).arrange(DOWN, buff=0.4)
        self.play(FadeIn(summary_group))
        self.wait(3)
        self.play(FadeOut(summary_group), FadeOut(summary_title))

        self.clear()

        # =====================================================================
        # 8) FINAL ANSWER
        # =====================================================================
        final_box = RoundedRectangle(width=7, height=1.5, color=GREEN)
        final_text = Text("Maximum Profit = 7", font_size=40, color=GREEN)
        final_text.move_to(final_box.get_center())

        self.play(Create(final_box), FadeIn(final_text))
        self.wait(2)
        self.play(FadeOut(final_box), FadeOut(final_text))

        thank = Text("Thank You!", font_size=40)
        self.play(FadeIn(thank))
        self.wait(2)
