def solve_map_coloring(countries, neighbors, colors):
    assignment = {}

    def is_consistent(country, color):
        for nb in neighbors.get(country, []):
            if assignment.get(nb) == color:
                return False
        return True

    def mrv_select_unassigned():
        unassigned = [c for c in countries if c not in assignment]

        def remaining_domain_size(c):
            return sum(is_consistent(c, col) for col in colors)

        return min(unassigned, key=remaining_domain_size)

    def backtrack():
        if len(assignment) == len(countries):
            return assignment.copy()

        country = mrv_select_unassigned()
        for color in colors:
            if is_consistent(country, color):
                assignment[country] = color
                result = backtrack()
                if result:
                    return result
                assignment.pop(country)
        return None

    return backtrack()


def demo_6_countries():
    countries = ["Aland", "Boreal", "Cyrene", "Dorne", "Eldia", "Fjord"]
    neighbors = {
        "Aland":  ["Boreal", "Cyrene"],
        "Boreal": ["Aland", "Cyrene", "Dorne"],
        "Cyrene": ["Aland", "Boreal", "Dorne", "Eldia"],
        "Dorne":  ["Boreal", "Cyrene", "Eldia", "Fjord"],
        "Eldia":  ["Cyrene", "Dorne", "Fjord"],
        "Fjord":  ["Dorne", "Eldia"],
    }
    return countries, neighbors
