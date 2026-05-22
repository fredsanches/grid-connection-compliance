from pydantic import BaseModel, Field

class TransformerData(BaseModel):
    """Data Transfer Object representing a Distribution Transformer."""

    # Field(...) denote that the argument is required
    equipment_id: str = Field(...,
                              description="Unique equipment identifier (e.g., PAC_1)"
    )
    # Math Constraints: power and voltage must be greater than zero
    # Pydantic will automatically raise ValidationError if they are not
    nom_power_kva: float = Field(..., gt=0, description="Nominal power in kVA")
    primary_voltage_kv: float = Field(..., 
                                      gt=0, 
                                      description="Primary winding voltage in kV")
    secondary_voltage_kv: float = Field(...,
                                        gt=0,
                                        description="Secondary winding voltage in kV")