from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos: int):
        oracle_money = 0
        honda_money = 0

        if race_pos <= 1:
            oracle_money += 1500000
            honda_money += 20000
        elif race_pos <= 2:
            oracle_money += 800000
            honda_money += 20000
        elif race_pos <= 8:
            honda_money += 20000
        elif race_pos <= 10:
            honda_money += 10000

        earned_money = oracle_money + honda_money - 250000

        self.budget += earned_money
        return f"The revenue after the race is { earned_money }$. Current budget { self.budget }$"