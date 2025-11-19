from manim import *
class StockAnimation(Scene):
    def construct(self):

        # ------------------------------------------------------------
        # 1) TITLE
        # ------------------------------------------------------------
        title = Text("Best Time to Buy and Sell Stock II", font_size=52, weight=BOLD)
        subtitle = Text("Complete Explanation + Visualization + Code", font_size=28)
        header = VGroup(title, subtitle).arrange(DOWN, buff=0.4)

        self.play(FadeIn(header, shift=UP))
        self.wait(2)
        self.play(FadeOut(header))

        # ------------------------------------------------------------
        # 2) PROBLEM STATEMENT
        # ------------------------------------------------------------
        problem = Paragraph(
            "You are given an array prices where prices[i] is the price of a stock on day i.",
            "",
            "You may buy and sell multiple times, but you can hold at most one share at a time.",
            "",
            "Goal: Return the maximum profit possible.",
            alignment="left",
            font_size=30,
            line_spacing=1.2
        )

        self.play(FadeIn(problem))
        self.wait(4)
        self.play(FadeOut(problem))

        # ------------------------------------------------------------
        # 3) EXAMPLES
        # ------------------------------------------------------------
        ex_title = Text("Examples", font_size=40, weight=BOLD)
        ex_list = Paragraph(
            "1) prices = [7, 1, 5, 3, 6, 4] → Output: 7",
            "2) prices = [1, 2, 3, 4, 5] → Output: 4",
            "3) prices = [7, 6, 4, 3, 1] → Output: 0",
            alignment="left",
            font_size=28,
            line_spacing=1.3
        )

        example_block = VGroup(ex_title, ex_list).arrange(DOWN, buff=0.4)

        self.play(FadeIn(example_block))
        self.wait(4)
        self.play(FadeOut(example_block))

        # ------------------------------------------------------------
        # 4) GRAPH VISUALIZATION
        # ------------------------------------------------------------
        graph_title = Text("Visualizing Example 1", font_size=40)
        self.play(FadeIn(graph_title))
        self.wait(1)
        self.play(graph_title.animate.to_edge(UP))

        prices = [7, 1, 5, 3, 6, 4]
        x_start = -3.5
        y_start = -2
        x_scale = 1.3
        y_scale = 0.25

        dots, labels = [], []

        for i, p in enumerate(prices):
            dot = Dot([x_start + i * x_scale, y_start + p * y_scale, 0])
            label = Text(str(p), font_size=26).next_to(dot, UP, buff=0.15)
            dots.append(dot)
            labels.append(label)

        self.play(*[FadeIn(d) for d in dots])
        self.play(*[FadeIn(lbl) for lbl in labels])

        lines = []
        for i in range(len(dots) - 1):
            line = Line(dots[i].get_center(), dots[i + 1].get_center())
            lines.append(line)
            self.play(Create(line), run_time=0.4)

        self.wait(2)
        self.play(
            FadeOut(graph_title),
            *[FadeOut(d) for d in dots],
            *[FadeOut(lbl) for lbl in labels],
            *[FadeOut(ln) for ln in lines]
        )

        # ------------------------------------------------------------
        # 5) PROFIT CALCULATION (STEP-BY-STEP)
        # ------------------------------------------------------------
        calc_title = Text("Step-by-Step Profit Calculation", font_size=40)
        self.play(FadeIn(calc_title))
        self.wait(1)
        self.play(calc_title.animate.to_edge(UP))

        steps = []
        total_profit = 0

        for i in range(len(prices) - 1):
            today = prices[i]
            tomorrow = prices[i + 1]

            if tomorrow > today:
                profit = tomorrow - today
                total_profit += profit

                step_text = Text(
                    f"Buy at {today}, Sell at {tomorrow} → +{profit}",
                    font_size=30
                )
                steps.append(step_text)

                group = VGroup(*steps).arrange(DOWN, buff=0.5).move_to(ORIGIN)

                if len(steps) == 1:
                    self.play(FadeIn(group))
                else:
                    self.play(Transform(prev_group, group))

                prev_group = group
                self.wait(0.7)

        self.wait(2)

        # 100% GUARANTEED FIX: Clear all leftover objects
        self.clear()

        # ------------------------------------------------------------
        # 6) IMPLEMENTATION CONCEPT EXPLANATION
        # ------------------------------------------------------------
        concept_title = Text("How We Implement the Solution", font_size=40)
        concept_lines = Paragraph(
            "We loop through the price array.",
            "If today's price < tomorrow's price → we buy today and sell tomorrow.",
            "We keep adding all positive differences.",
            "This is a Greedy Strategy.",
            alignment="left",
            font_size=28,
            line_spacing=1.2,
        )

        concept_group = VGroup(concept_title, concept_lines).arrange(DOWN, buff=0.5)

        self.play(FadeIn(concept_group))
        self.wait(4)
        self.play(FadeOut(concept_group))

        # ------------------------------------------------------------
        # 7) SHOW C++ CODE
        # ------------------------------------------------------------
        code_title = Text("C++ Solution", font_size=40)

        cpp_code_text = Paragraph(
            "class Solution {",
            "public:",
            "    int maxProfit(vector<int>& prices) {",
            "        int profit = 0;",
            "",
            "        for (int i = 1; i < prices.size(); i++) {",
            "            if (prices[i] > prices[i - 1]) {",
            "                profit += prices[i] - prices[i - 1];",
            "            }",
            "        }",
            "",
            "        return profit;",
            "    }",
            "};",
            alignment="left",
            font_size=24,
            line_spacing=0.6
        )

        code_group = VGroup(code_title, cpp_code_text).arrange(DOWN, buff=0.5)

        self.play(FadeIn(code_group))
        self.wait(5)
        self.play(FadeOut(code_group))

        # ------------------------------------------------------------
        # 8) EXPLAIN CODE LOGIC
        # ------------------------------------------------------------
        explain_title = Text("Explanation of Code", font_size=40)
        explain_lines = Paragraph(
            "• Initialize profit = 0",
            "• Loop from i = 1 to n-1",
            "• If price[i] > price[i-1], add the difference to profit",
            "• Return total profit",
            alignment="left",
            font_size=28,
            line_spacing=1.2
        )

        explain_group = VGroup(explain_title, explain_lines).arrange(DOWN, buff=0.5)

        self.play(FadeIn(explain_group))
        self.wait(4)
        self.play(FadeOut(explain_group))

        # CLEAR EVERYTHING BEFORE FINAL ANSWER (100% FIX)
        self.clear()

        # ------------------------------------------------------------
        # 9) FINAL ANSWER
        # ------------------------------------------------------------
        final_box = RoundedRectangle(width=8, height=1.5, color=GREEN)
        final_text = Text("Maximum Profit = 7", font_size=38, color=GREEN)
        final_text.move_to(final_box.get_center())

        final_group = VGroup(final_box, final_text)

        self.play(Create(final_box), FadeIn(final_text))
        self.wait(2)
        self.play(FadeOut(final_group))

        # ------------------------------------------------------------
        # END
        # ------------------------------------------------------------
        thank = Text("Thank You!", font_size=40)
        self.play(FadeIn(thank))
        self.wait(2)
