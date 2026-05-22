# BDGD Geodatabase Parser Design

## Purpose
To parse ANEEL BDGD (Base de Dados Geográfica da Distribuidora) File Geodatabase (.gdb) files efficiently and extract grid assets for the OpenDSS simulation engine.

## Constraints & Requirements
- **Data Size:** Expected to fit comfortably in standard RAM (16-32GB), allowing for in-memory processing.
- **Performance:** Must be fast and memory-efficient.
- **Architecture:** Must adhere to Clean Architecture, decoupling parsing logic from OpenDSS simulation logic.

## Selected Approach
**GeoPandas + pyogrio**
- **Why:** `pyogrio` uses high-performance GDAL C API bindings via Apache Arrow. It provides the fastest in-memory processing for `.gdb` files, outputs directly to GeoDataFrames, and uses significantly less memory than the traditional Fiona engine.

## Architecture & Data Flow
1. **Module:** A dedicated `GDBParser` module in the `BDGD-Tools` namespace.
2. **Layer Discovery:** Use `pyogrio.list_layers()` to identify available BDGD tables (e.g., Conductors, Transformers, Buses) within the `.gdb` file.
3. **Data Extraction:** Load specific required layers using `geopandas.read_file(path, engine="pyogrio", layer=layer_name)`.
4. **Data Transformation:** Transform the extracted GeoDataFrames into pure Python `dataclasses` (or Pydantic models for runtime validation). Examples: `BusData`, `ConductorSpecs`.
5. **Decoupling:** These dataclasses act as Data Transfer Objects (DTOs), ensuring the OpenDSS simulation engine is strictly fed well-structured pure Python objects, completely agnostic of GeoPandas or GDAL.

## Error Handling
- Validate layer existence before reading.
- Check for missing critical ANEEL attributes within the GeoDataFrames.
- Raise specific, domain-driven exceptions (e.g., `MissingBDGDLayerError`, `InvalidAssetAttributeError`) when validation fails.

## Testing Strategy
- Use `pytest` for all unit testing.
- Utilize small mock GeoDataFrames or a lightweight, mocked `.gdb` fixture to test extraction and transformation logic, avoiding the need to load real, massive datasets during CI/CD.
