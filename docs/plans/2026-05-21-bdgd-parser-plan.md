# BDGD Parser Implementation Plan

> **For Antigravity:** REQUIRED WORKFLOW: Use `.agent/workflows/execute-plan.md` to execute this plan in single-flow mode.

**Goal:** Create a robust, high-performance parser for ANEEL BDGD File Geodatabases (.gdb) using GeoPandas + pyogrio, outputting strictly validated Pydantic models.

**Architecture:** A `GDBParser` class that encapsulates `geopandas` and `pyogrio` to read layers, transforming the spatial data into Pydantic models (DTOs) for the OpenDSS engine. This isolates the simulation core from any GIS/GDAL dependencies.

**Tech Stack:** `geopandas`, `pyogrio`, `pytest`, `pydantic`

## Target Layers
Based on the requirements for power flow calculations, we will target the following elements first:
- **Transformers:** (Nominal power, voltages, taps, losses, impedance).
- **Conductors/Wires:** (Ampacity, impedance matrices).
- **Reclosers:** (Status, settings).

---

### Task 1: Package Scaffolding & Pytest Setup

**Files:**
- Create: `pyproject.toml` (if not exists)
- Create: `src/bdgd_tools/__init__.py`
- Create: `tests/conftest.py`

**Step 1: Create initial structure**
Create the `src` and `tests` directories to establish the standard Python package layout.

**Step 2: Setup tests**
Verify `pytest` can run and discover tests.

**Step 3: Commit**
```bash
git add pyproject.toml src/ tests/
git commit -m "chore: scaffold project structure and pytest"
```

---

### Task 2: Pydantic Data Models (DTOs)

**Files:**
- Create: `src/bdgd_tools/core/models.py`
- Create: `tests/core/test_models.py`

**Step 1: Write the failing test**
```python
# tests/core/test_models.py
from bdgd_tools.core.models import BusData

def test_bus_data_creation():
    bus = BusData(bus_id="BUS_01", base_kv=13.8)
    assert bus.bus_id == "BUS_01"
    assert bus.base_kv == 13.8
```

**Step 2: Run test to verify it fails**
Run: `pytest tests/core/test_models.py -v`
Expected: FAIL with "ModuleNotFoundError" or "ImportError".

**Step 3: Write minimal implementation**
```python
# src/bdgd_tools/core/models.py
from pydantic import BaseModel, Field

class BusData(BaseModel):
    bus_id: str = Field(..., description="Unique bus identifier")
    base_kv: float = Field(..., gt=0, description="Base voltage in kV")
```

**Step 4: Run test to verify it passes**
Run: `pytest tests/core/test_models.py -v`
Expected: PASS

**Step 5: Commit**
```bash
git add src/bdgd_tools/core/models.py tests/core/test_models.py
git commit -m "feat: add Pydantic models for grid assets"
```

---

### Task 3: The GDB Parser Core

**Files:**
- Create: `src/bdgd_tools/core/gdb_parser.py`
- Create: `tests/core/test_gdb_parser.py`

**Step 1: Write the failing test**
```python
# tests/core/test_gdb_parser.py
import pytest
from unittest.mock import patch
import geopandas as gpd
from shapely.geometry import Point
from bdgd_tools.core.gdb_parser import GDBParser

@patch("geopandas.read_file")
@patch("pyogrio.list_layers")
def test_gdb_parser_list_layers(mock_list_layers, mock_read_file):
    mock_list_layers.return_value = [["UN_TRF_D", "Point"]]
    
    parser = GDBParser("dummy.gdb")
    layers = parser.list_layers()
    
    assert "UN_TRF_D" in layers
```

**Step 2: Run test to verify it fails**
Run: `pytest tests/core/test_gdb_parser.py -v`
Expected: FAIL with "ImportError".

**Step 3: Write minimal implementation**
```python
# src/bdgd_tools/core/gdb_parser.py
import geopandas as gpd
import pyogrio

class GDBParser:
    def __init__(self, gdb_path: str):
        self.gdb_path = gdb_path
        
    def list_layers(self) -> list[str]:
        """Lists all layers available in the Geodatabase."""
        layers_info = pyogrio.list_layers(self.gdb_path)
        return [layer[0] for layer in layers_info]
```

**Step 4: Run test to verify it passes**
Run: `pytest tests/core/test_gdb_parser.py -v`
Expected: PASS

**Step 5: Commit**
```bash
git add src/bdgd_tools/core/gdb_parser.py tests/core/test_gdb_parser.py
git commit -m "feat: add base GDBParser using pyogrio"
```

---

### Task 4: Parsing Layers into DTOs

**Files:**
- Modify: `src/bdgd_tools/core/gdb_parser.py`
- Modify: `tests/core/test_gdb_parser.py`

**Step 1: Write the failing test**
Add a test that uses `parser.extract_buses()` which should return a list of `BusData` objects, mocking the GeoDataFrame returned by `geopandas.read_file`.

**Step 2: Run test to verify it fails**
Run: `pytest tests/core/test_gdb_parser.py -v`
Expected: FAIL (Method not implemented)

**Step 3: Write minimal implementation**
Implement `extract_buses()` in `GDBParser` which internally calls `geopandas.read_file(..., engine="pyogrio")`, iterates over the rows (or uses apply), and instantiates `BusData` objects.

**Step 4: Run test to verify it passes**
Run: `pytest tests/core/test_gdb_parser.py -v`
Expected: PASS

**Step 5: Commit**
```bash
git add src/bdgd_tools/core/gdb_parser.py tests/core/test_gdb_parser.py
git commit -m "feat: parse layer data into Pydantic models"
```
