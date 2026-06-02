from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence

import pyogrio


@dataclass(frozen=True, slots=True)
class LayerInventory:
  """Metadata for one BDGD layer.

  Parameters:
    name: Layer name inside the File Geodatabase.
    geometry_type: Geometry type reported by GDAL/pyogrio.
    row_count: Number of features when reported by pyogrio.
    columns: Attribute column names.
    candidate_concepts: Electrical concepts this layer may represent.

  Raises:
    No exception is raised by this data container.
  """

  name: str
  geometry_type: str
  row_count: int | None
  columns: tuple[str, ...]
  candidate_concepts: tuple[str, ...]


def build_inventory(gdb_path: Path) -> tuple[LayerInventory, ...]:
  """Build metadata inventory for every layer in a File Geodatabase.

  Args:
      gdb_path (Path): Path to an extracted `.gdb` directory.

  Raises:
    FileNotFoundError: If the GDB path does not exist.

  Returns:
      tuple[LayerInventory, ...]: layer inventory records.
  """

  if not gdb_path.exists():
    raise FileNotFoundError(f"GDB path not found: {gdb_path}")
  
  layers: list[LayerInventory] = []
  for layer_data in pyogrio.list_layers(gdb_path):
    layer_name  = str(layer_data[0])
    info        = pyogrio.read_info(gdb_path, layer=layer_name)
    columns     = tuple(str(field) for field in info.get("fields", ()))

    layers.append(
      LayerInventory(
        name=layer_name,
        geometry_type=str(info.get("geometry_type", "Unknown")),
        row_count=_read_feature_count(info),
        columns=columns,
        candidate_concepts=_classify_layer(layer_name, columns)
      )
    )

  return tuple(layers)


def render_inventory_markdown(
    gdb_path: Path,
    layers: Sequence[LayerInventory],
    source: str,
    download_date: str,
) -> str:
  """Render inventory metadata as markdown
  
  Parameters:
    gdb_path: local path to the inspected GDB.
    layers: layer inventory records.
    source: data source description.
    download_date: date when raw BDGD file was downloaded.
  Returns:
    str: Markdown report content."""
  
  lines = [
    "# BDGD Inventory",
    "",
    f"- **Source:** {source}",
    f"- **Download date:** {download_date}",
    f"- **GDB path:** `{gdb_path}`",
    "",
    "## Layers",
    "",
  ]

  for layer in layers:
    lines.extend(
      [
        f"### {layer.name}",
        "",
        f"- Geometry type: `{layer.geometry_type}`",
        f"- Row count: `{layer.row_count}`",
        f"- Candidate concepts: `{', '.join(layer.candidate_concepts) or 'none'}`",
        f"- Columns: `{', '.join(layer.columns)}`",
        ""
      ]
    )

  return "\n".join(lines)


def _read_feature_count(info: Mapping[str, object]) -> int | None:
  """Read feature count from pyogrio metadata."""
  value = info.get("features")
  return value if isinstance(value, int) else None


def _classify_layer(
    layer_name: str,
    columns: Sequence[str],
) -> tuple[str, ...]:
  """Classify a BDGD layer as possible feeder-topology concepts."""
  text = " ".join((layer_name, *columns)).upper()
  concepts: list[str] = []
  if "SSDMT" in text or ("PAC_1" in text and "PAC_2" in text):
    concepts.append("medium_voltage_segment")
  if "CTMT" in text:
    concepts.append("feeder")
  if "SUB" in text or "UNIT_TR_AT" in text:
    concepts.append("substation")
  if "TIP_CND" in text or "CND" in text:
    concepts.append("conductor")
  if "UNTR" in text or "POT_NOM" in text or "TEN_PRI" in text:
    concepts.append("transformer")
  if "CHV" in text or "REL" in text or "SECC" in text:
    concepts.append("switch_or_recloser")
  if "UC" in text or "CARGA" in text:
    concepts.append("load")
  if "UC" in text or "GER" in text:
    concepts.append("distributed_generation")
  
  # wrapping dict in tuple returns dict keys and guarantee original order
  return tuple(dict.fromkeys(concepts))