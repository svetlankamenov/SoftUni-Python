from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    def calculate_revenue_after_race(self, race_pos:int):
        petronas_money = 0
        team_viewer_money = 0

        if race_pos <= 1:
            petronas_money += 1000000
            team_viewer_money += 100000
        elif race_pos <= 3:
            petronas_money += 500000
            team_viewer_money += 100000
        elif race_pos <= 5:
            team_viewer_money += 100000
        elif race_pos <= 7:
            team_viewer_money += 50000

        earned_money = petronas_money + team_viewer_money - 200000
        self.budget += earned_money
        return f"The revenue after the race is {earned_money}$. Current budget {self.budget}$"