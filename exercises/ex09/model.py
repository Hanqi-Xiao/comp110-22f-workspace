"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random, randint
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt

__author__ = "730295059"


def bound(value: int, min_n: int, max_n: int) -> int:
    """Bounds number by two constants."""
    return max(min_n, min(max_n, value))


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def distance(self, other_point: Point) -> float:
        """Ecludian distance between two points."""
        x_dist = other_point.x - self.x 
        y_dist = other_point.y - self.y 
        return sqrt(x_dist**2 + y_dist**2)

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
        

class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Update its location based on direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell, unfinished, map color to sickness."""
        if self.is_infected():
            return "red"
        elif self.is_vulnerable():
            return "gray"
        elif self.is_immune():
            return "green"

    def contract_disease(self) -> None:
        """Adjust disease state."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Check if is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        return False
    
    def is_infected(self) -> bool:
        """Check if infected."""
        if self.sickness >= constants.INFECTED:
            return True
        return False

    def contact_with(self, other_cell: Cell) -> None:
        """Contact, what happens to both the cells?"""
        if self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()
        elif self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()

    def immunize(self) -> None:
        """Immune the cell."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> None:
        """Check if immune."""
        if self.sickness == constants.IMMUNE:
            return True
        return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, initial_infected: int, initial_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        if (initial_infected >= cells) or (initial_infected <= 0):
            raise ValueError("Hey goi, you value error, the initial infected input given makes no sense. At least some number of starting cells must start infected.")
        if initial_immune > cells or initial_immune < 0:
            raise ValueError("There are too many or too few already immune cells.")
        if (initial_immune + initial_infected) > cells:
            raise ValueError("Total amount of non-vulnerable cells is too much.")

        self.population = []
        for _ in range(cells):
            new_cell: Cell = Cell(self.random_location(), self.random_direction(speed))
            if initial_infected > 0:
                new_cell.contract_disease()
                initial_infected -= 1
            elif initial_immune > 0:
                new_cell.immunize()
                initial_immune -= 1
            self.population.append(new_cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        count: int = 0
        self.check_contacts()
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
            # if count == 0:
            #     print(cell.location.x, constants.MIN_X, constants.MIN_X > (cell.direction.x + cell.location.x))
            count += 1
        self.time += 1

    def random_location(self) -> Point:
        """Generate a random location."""
        x: int = randint(constants.MIN_X, constants.MAX_X)
        y: int = randint(constants.MIN_Y, constants.MAX_Y)
        return Point(x, y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        angle: float = random() * pi * 2
        x: float = cos(angle) * speed
        y: float = sin(angle) * speed
        return Point(x, y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if not (constants.MIN_X) < (cell.direction.x + cell.location.x) < (constants.MAX_X):
            cell.location.x = bound(cell.direction.x + cell.location.x, constants.MIN_X, constants.MAX_X)
            cell.direction.x = cell.direction.x * -1
            # print("correctin")
        if not (constants.MIN_Y) < (cell.direction.y + cell.location.y) < (constants.MAX_Y):
            cell.location.y = bound(cell.direction.y + cell.location.y, constants.MIN_Y, constants.MAX_Y)
            cell.direction.y = cell.direction.y * -1
            # print("correctin")

    def check_contacts(self) -> None:
        """Method to check contacts."""
        for i in range(len(self.population) - 1, -1, -1):
            first_cell = self.population[i]
            for j in range(i):
                second_cell = self.population[j]
                if first_cell.location.distance(second_cell.location) < constants.CELL_RADIUS:
                    first_cell.contact_with(second_cell)

    def is_complete(self) -> bool:
        """Checks if the model is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        return True