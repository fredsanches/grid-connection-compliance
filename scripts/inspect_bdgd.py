import argparse
from pathlib import Path

from bdgd_tools.core.gdb_inventory import(
  build_inventory,
  render_inventory_markdown
)


def parse_args() -> argparse.Namespace:
  """Parse command-line arguments

  Returns:
    Parsed command-line namespace
  """
  parser = argparse.ArgumentParser(
    description="Inspect an ANEEL BDGD File Geodatabase and write inventory Markdown"
  )
  parser.add_argument("--gdb-path", required=True)
  parser.add_argument("--source", required=True)
  parser.add_argument("--download-date", required=True)
  parser.add_argument("--output", required=True)

  return parser.parse_args()


def main() -> None:
  """Generate a BDGD inventory report.

  Raises:
    IsADirectoryError: If output is a dir, not a file.
"""
   
  args         = parse_args()
  gdb_path     =Path(args.gdb_path)
  output_path  =Path(args.output)

  layers   = build_inventory(gdb_path)
  markdown = render_inventory_markdown(
    gdb_path=gdb_path,
    layers=layers,
    source=str(args.source),
    download_date=str(args.download_date)
  )
  if output_path.exists() and output_path.is_dir():
      raise IsADirectoryError(
         f"Output path points to a directory, expected file: {output_path}"
      )
  output_path.parent.mkdir(parents=True, exist_ok=True)
  output_path.write_text(markdown, encoding="utf-8")


if __name__ == "__main__":
   main()
