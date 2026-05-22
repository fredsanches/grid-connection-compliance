import pytest
from pydantic import ValidationError
from bdgd_tools.core.models import TransformerData

def test_transformer_data_valid_creation():
    """Test that a valid Transformer can be instantiated."""
    t = TransformerData(
            equipment_id = "TRF_01",
            nom_power_kva = 112.5,
            primary_voltage_kv = 13.8,
            secondary_voltage_kv = .38
    )
    assert t.equipment_id == "TRF_01"
    assert t.nom_power_kva == 112.5

def test_transformer_data_invalid_power():
    """Test that negative power raises a validation error."""
    with pytest.raises(ValidationError):
        TransformerData(
            equipment_id="TRF_02",
            nom_power_kva=-50.0,    # invalid: power must be > 0
            primary_voltage_kv=13.8,
            secondary_voltage_kv=.38
        )