import logic.sim


def test_min_pool_cost_enforced():
    min_cost = 0.01
    model = logic.sim.Simulation(n=10, min_pool_cost=min_cost)
    for agent in model.get_agents_list():
        assert agent.cost >= min_cost
