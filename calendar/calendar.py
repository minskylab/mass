import copy
from dataclasses import dataclass
from typing import List, Dict, Tuple
from enum import Enum
import random
import math
import tableformatter
from colorama import Back
from tabulate import tabulate

# block 1h
# kinds: 10
#

# inputs: []
# output: []

# Task kind enum


class BlockState(Enum):
    Assigned = "As"
    Blocked = "Bl"
    Available = "Av"


@dataclass
class Block:
    kind: BlockState
    name: str = ""
    weight: float = 1.0


class Days(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6


@dataclass
class Calendar:
    data: Dict[Days, List[Block]]


def new_calendar() -> Calendar:
    data: Dict[Days, List[Block]] = {}
    for d in Days:
        data[d] = [Block(BlockState.Available) for i in range(24)]
    return Calendar(data)


def constraint_calendar(calendar: Calendar, hows: int = 10) -> Calendar:
    data: Dict[Days, List[Block]] = dict.copy(calendar.data)

    for i in range(hows):
        day: Days = random.choice([d for d in Days])
        index = math.floor(random.random()*24)
        data[day][index] = Block(BlockState.Blocked)

    return Calendar(data)


def new_population(size: int) -> List[Calendar]:
    pass


def eval_individual(cal: Calendar) -> float:
    data: Dict[Days, List[Block]] = dict.copy(cal.data)
    out: float = 0

    # Based on blanks
    score = 0

    for d in Days:
        score += sum([1 for b in data[d] if b.kind == BlockState.Available])

    data_size = len(data[Days.Monday]) if len(data) > 0 else -1
    out = score/(data_size * len(Days))

    # Based on continuity

    # Based on lunch time 12hrs to 15hrs, peak 13hrs

    # score = 0

    # for d in Days:
    #     for b in data[d]:
    #         # A = 0 if cond else
    #         if b.kind == BlockKind.Available:
    #             score = score+2 if b == 12 else score = score + 0
    #             score = score+3 if b == 13 else score = score + 0
    #             score = score+2 if b == 14 else score = score + 0
    #             score = score+1 if b == 15 else score = score + 0

    # out = num/(len(data[d]) * len(Days))

    return out


def sort_by_adaptation(population: List[Calendar]) -> List[Calendar]:
    return sorted(population, lambda cal: eval_individual(cal))


def crossover_individuals(cal1: Calendar, cal2: Calendar) -> Tuple[Calendar, Calendar]:
    pass


def mutation_individual(cal: Calendar) -> Calendar:
    pass


def show_calendar(calendar: Calendar):
    data: Dict[Days, List[Block]] = dict.copy(calendar.data)
    header: List = []
    table_rows: List = []
    """
    colors: Dict[BlockKind, str] = {BlockKind.Available: tableformatter.TableColors.TEXT_COLOR_GREEN,
                                   BlockKind.Constraint: tableformatter.TableColors.TEXT_COLOR_RED,
                                   BlockKind.Task: tableformatter.TableColors.TEXT_COLOR_BLUE}
    """
    colors: Dict[BlockState, str] = {BlockState.Available: Back.GREEN,
                                     BlockState.Blocked: Back.RED,
                                     BlockState.Assigned: Back.BLUE}

    for day in Days:
        header.append(day.name)
        row = [colors[block.kind] + block.kind.value for block in data[day]]
        # row = [tableformatter.Row(block.kind.value) for block in data[day]]
        table_rows.append(row)
        # , text_color=colors[b.kind]
    table_rows = list(map(list, zip(*table_rows)))

    # print(Back.GREEN + 'hola'1
    print("".join([Back.WHITE + "{:>11}".format(h)
                   for h in header]) + "{:>11}".format(Back.RESET))

    for row in table_rows:
        print("".join(["{:>15}".format(col)
                       for col in row]) + "{:>15}".format(Back.RESET))
    # print(tableformatter.generate_table(table_rows, header))


if __name__ == "__main__":
    print("c")
Days
# print(c.data[Days.Monday])
# print(len(c.data[Days.Monday]))
c1 = new_calendar()
c2 = new_calendar()

c1 = constraint_calendar(c1, hows=20)
c2 = constraint_calendar(c2, hows=20)

show_calendar(c1)
print(eval_individual(c1))

show_calendar(c2)
print(eval_individual(c2))


# row_format ="{:>15}" * (len(teams_list) + 1)
# https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data
# https://docs.python.org/3.8/library/string.html#formatspec
