from sales_engine import AISalesAutomationEngine


def test_roi_calculation():
    engine = AISalesAutomationEngine("SaaS")

    result = engine.calculate_predictive_roi(100, 40)

    assert result["hours_recovered"] == 1092
    assert result["capital_saved_usd"] == 43680


def test_industry_filter():
    engine = AISalesAutomationEngine("Healthcare")

    results = engine.process_pipeline()

    assert len(results) == 1
    assert results[0]["industry"] == "healthcare"
