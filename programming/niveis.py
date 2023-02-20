MODELAGEM MATEMÁTICA

entrada:

definições:
sejam
 w: velocidade angular da esteira
 s: passos do atleta na esteira
 b: quantidade de kilocalorias queimadas no exercício

atribuição de valores:
s = 4
w = 5

b = 0

if (s + w) >= 50:
    b = 60

resutado da função:
    0 ou 60

saida:
    quantidade de kilocalorias queimadas no exercício
    é suficiente para manter a saúde fisíca em dia!


MODELAGEM COMPUTACIONAL
"""
Comentário do arquivo
"""


"""
[summary]

Returns:
    [type]: [description]
"""

4

4 # steps

# run: steps in speficic weeks
4+5
4+9
4+32

runner_steps_in_iteration_in_ergonomic_checks = 4

# Runner steps in iteration in ergonomic checks
steps = 4

steps+5
steps+9
steps+32


def run(weeks):
    steps = 4
    run_in_week = steps + weeks

    return run_in_week


def run(week, steps=4):
    """
    Contagem de passos andados na week.

    Args:
        week ([type]): [description]
        steps (int, optional): [description]. Defaults to 4.

    Returns:
        [type]: [description]
    """
    run_in_week = steps + week

    return run_in_week


def test_run_in_week_5():
    week = 5
    run(week)
    assert

def test_run_in_week_9():
    week = 9
    run(week)
    assert

def test_run_in_week_32():
    week = 32
    run(week)
    assert

def test_run_in_week_steps()
    week = 32
    steps = 8
    run(week)
    assert

def test_run_in_week_burn_50kcal():
    """
    from 0 to 5: 10kcal
    from 5 to 50: 60kcal
    from 50 to 155: 120kcal
    from 155 to 250: 300kcal
    """
    ...