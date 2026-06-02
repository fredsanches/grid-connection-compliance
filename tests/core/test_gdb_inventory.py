from pathlib import Path
from unittest.mock import patch

from bdgd_tools.core.gdb_inventory import (
  LayerInventory,
  build_inventory,
  render_inventory_markdown,
)

@patch("bdgd_tools.core.gdb_inventory.pyogrio.read_info")
@patch("bdgd_tools.core.gdb_inventory.pyogrio.list_layers")
def test_build_inventory_classifies_topology_candidates(
    mock_list_layers,
    mock_read_info,
    tmp_path,
):
  # fake path -> pytest fixture
  gdb_path = tmp_path / "coelba.gdb"
  gdb_path.mkdir()

  mock_list_layers.return_value = [
    ["SSDMT", "LineString"],
    ["UNTRMT", "Point"],
  ]
  mock_read_info.side_effect = [
    {
      "geometry_type": "LineString",
      "features": 10,
      "fields": ["COD_ID", "CTMT", "PAC_1", "PAC_2", "TIP_CND"],
    },
    {
      "geometry_type": "Point",
      "features": 3,
      "fields": ["COD_ID", "CTMT", "PAC_1", "TEN_PRI", "POT_NOM"],
    },
  ]

  layers = build_inventory(gdb_path)
  layers_by_name = {layer.name: layer for layer in layers}

  assert "SSDMT" in layers_by_name
  assert "UNTRMT" in layers_by_name
  assert "medium_voltage_segment" in layers_by_name["SSDMT"].candidate_concepts
  assert "conductor" in layers_by_name["SSDMT"].candidate_concepts
  assert "transformer" in layers_by_name["UNTRMT"].candidate_concepts


def test_render_inventory_markdown_contains_layer_metadata():
  layers = (
    LayerInventory(
      name="SSDMT",
      geometry_type="LineString",
      row_count=10,
      columns=("COD_ID", "CTMT", "PAC_1", "PAC_2", "TIP_CND"),
      candidate_concepts=("medium_voltage_segment", "conductor")
    ),
  )
  markdown = render_inventory_markdown(
    gdb_path=Path("data/raw/bdgd/coelba/coelba.gdb"),
    layers=layers,
    source="ANEEL BDGD open data portal",
    download_date="2026-06-01",
  )
  assert "# BDGD Inventory" in markdown
  assert "SSDMT" in markdown
  assert "medium_voltage_segment" in markdown
  assert "TIP_CND" in markdown